#!/usr/bin/env python3
"""Verificador de canon de Chronosia.

Cada dato de la campaña tiene UN dueño (01_Como_Dirigir.md y las fichas);
todo lo demás son copias o etiquetas que este script compara contra el
manifiesto de abajo. Se ejecuta en cada build (informativo) y con --strict
devuelve exit 1 si hay avisos — pensado para CI y para editar sin miedo.

Uso:  python3 exports/check_canon.py [--strict]   (desde la raíz del proyecto o desde exports/)
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ─────────────────────────── EL MANIFIESTO ───────────────────────────
# tipo: etiqueta canónica que debe acompañar al nombre en índices/tablas/cabeceras
# banda: nivel de la región (la ficha puede añadir matices, pero la cifra debe estar)
LUGARTENIENTES = {
    "Serapis":       dict(tipo="Temporal",    cr="5",  banda="4-7",  region="Espiral"),
    "Varrak":        dict(tipo="Temporal",    cr="9",  banda="5-8",  region="Abismo"),
    "Tempus":        dict(tipo="Temporal",    cr="8",  banda="8-10", region="Ruinas"),
    "Thyra":         dict(tipo="Temporal",    cr=None, banda=None,   region="Valle de la Aguja"),
    "Ymir":          dict(tipo="Dimensional", cr="8",  banda="4-7",  region="Glacialis"),
    "Medusa":        dict(tipo="Dimensional", cr="7",  banda="5-8",  region="Jardín"),
    "Gemelas":       dict(tipo="Dimensional", cr="8",  banda="5-8",  region="Jardín"),
    "Dimensionalis": dict(tipo="Dimensional", cr="9",  banda="9-10", region="Llanuras"),
    "Yrindra":       dict(tipo="Dimensional", cr="11", banda="9-10", region="Veldrisza"),
    "Ignis":         dict(tipo="Dimensional", cr="13", banda="8-10", region="Calderas"),
    "Vorthak":       dict(tipo="Vida",        cr="12", banda="8-10", region="Mansión"),
    "Teach":         dict(tipo="Híbrido",     cr="11", banda="7-9",  region="Archipiélago"),
}

# Frases que un tipo NO-canónico haría sospechosas junto al nombre…
TIPOS = ("Temporal", "Dimensional", "Vida", "Híbrido")
# …salvo en estos contextos legítimos (bando/política/negaciones/didáctica).
CONTEXTOS_OK = (
    "bando temporal", "bando dimensional", "líder temporal", "líder dimensional",
    "lugartenientes temporales", "lugartenientes dimensionales",
    "no da pieza", "sin pieza", "drena vida", "drena años", "poder robado",
    "disfraz", "no canaliza", "ni amaunator ni voidar", "política, no conducto",
    "es dimensional", "son dimensionales",  # aclaraciones didácticas de Medusa/Gemelas
    "conducto de amaunator", "conducto de voidar",  # descripciones del sistema
    "núcleo temporal", "carcasa dimensional", "drenaje temporal", "reserva temporal",
    "asesinad", "robado", "bando:", "caída", "caida",
)

# Fósiles prohibidos: (regex, excepción-si-la-línea-contiene, mensaje)
FOSILES = [
    (r"conclave", ("retirad", "no existe", "pre-", "sustituye", "como sistema"), "'Cónclave' es sistema retirado"),
    (r"lugartenientes? supremos?", ("retirad", "no existe", "no hay", "ni lugartenientes"), "'Supremos' es sistema retirado"),
    (r"8/8[^.\n]{0,60}(asalto|se abre|abre la torre)", ("Final D", "derrota", "NO se abre", "no se abre", "ya es tarde", "nunca"), "8/8 nunca abre la Torre (8/8 = Final D)"),
    (r"asalt[oa][^.\n]{0,50}8/8", ("Final D", "derrota", "ya es tarde", "nunca", "NO"), "el asalto no se dispara por el Reloj"),
    (r"balance (temporal|de poder)[ /-]", ("retirad", "ya no"), "'balance temporal/dimensional' es sistema retirado"),
    (r"matrona veldrisza", ("archivo", "\\.md", "se llama"), "la matrona es YRINDRA (Veldrisza es la ciudad)"),
    (r"derrotar \d\+? ?lugartenientes", (), "gating por nº de lugartenientes: retirado (Mapa de Puertas)"),
    (r"retroce\w+ (de )?medio segmento", (), "el Reloj nunca retrocede (salvo Varrak, −1)"),
    (r"la misma noche[^.\n]{0,60}(perla|piezas)", ("exager", "falso"), "Perla (Hito 1, Abysara) y Cronómetro (Hito 2, Cronópolis) no cayeron juntos"),
    (r"santuario suspendido", (), "lugar inexistente (fósil de la Carta/dossier)"),
    (r"ocup[éo] (el hueco|su lugar)", (), "nadie fue suplantado: Kaoros es agente doble, Serapis opera a distancia"),
    (r"bando (\w+ )?esta ganando|segun (el )?bando ganador", ("no hay", "no segun", "no existe"), "no hay sistema de 'bando ganador' (Cap. 1)"),
    (r"recuento que abre", (), "las puertas se abren con piezas, no con recuentos de lugartenientes"),
    (r"(oceanicos|perla)[^.\n]{0,50}milenios|milenios[^.\n]{0,50}(oceanicos|perla)", (), "los Oceánicos existen desde la división (~800 años), no milenios"),
    (r"siglos de (abuso|ocupacion|servicio|drenaje)", ("ochenta", "decadas", "no ", "subjetiv"), "la ocupación/el poder de Aethernus tiene DÉCADAS (~80 años), no siglos"),
]

# Invariantes del Reloj: si una línea habla del efecto de matar a un crítico, debe decir 2.
RELOJ_CRITICO = re.compile(r"cr[ií]tico[^.\n|]{0,80}estanca", re.I)

# Tamaño → dado de golpe (5e)
DADO_POR_TAMANO = [
    (re.compile(r"\bdiminut", re.I), 4), (re.compile(r"\bpequeñ", re.I), 6),
    (re.compile(r"\bmedian", re.I), 8), (re.compile(r"\bgrande?\b|\bGran\b", re.I), 10),
    (re.compile(r"\benorme", re.I), 12), (re.compile(r"\bgargantuesc", re.I), 20),
]
PG_RE = re.compile(r"(?:PG|Puntos de Golpe:?)\**\s*:?\**\s*(\d+)\s*\((\d+)d(\d+)\s*([+−-]\s*\d+)?\)")

SKIP_DIRS = {"exports", "assets", ".git"}
SKIP_FILES = {"agents.md", "70_Ideas_Creativas_DM.md", "00_Esquema_Campana_Mermaid.md", "00_Indice_Campana.md"}


def norm(s):
    s = s.replace("*", "")
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def slugify(h):
    """Slug estilo GitHub/mkdocs para verificar anclas."""
    h = re.sub(r"[*_`]", "", h.strip())
    h = "".join(c for c in h if not (0x1F000 <= ord(c) <= 0x1FAFF or 0x2600 <= ord(c) <= 0x27BF or ord(c) in (0xFE0F, 0x20E3) or 0x2300 <= ord(c) <= 0x23FF or 0x2B00 <= ord(c) <= 0x2BFF))
    h = h.strip().lower()
    h = re.sub(r"[^\w\sáéíóúüñ·-]", "", h, flags=re.UNICODE)
    return re.sub(r"[\s·]+", "-", h).strip("-")


def files():
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS or rel.name in SKIP_FILES:
            continue
        yield rel, p.read_text(encoding="utf-8")


def main():
    problemas = []

    def warn(rel, i, msg, linea=""):
        problemas.append(f"{rel}:{i}: {msg}" + (f"  →  {linea.strip()[:110]}" if linea else ""))

    headings = {}   # archivo → set(slugs)
    all_paths = set()
    corpus = list(files())
    for rel, text in corpus:
        all_paths.add(str(rel))
        headings[str(rel)] = {slugify(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.+)$", text, re.M)}

    for rel, text in corpus:
        for i, linea in enumerate(text.splitlines(), 1):
            lnorm = norm(linea)

            # 1 · Etiquetas de tipo junto a nombres de lugartenientes
            for nombre, d in LUGARTENIENTES.items():
                if norm(nombre) not in lnorm:
                    continue
                for t in TIPOS:
                    if t == d["tipo"] or norm(t) not in lnorm:
                        continue
                    mlab = re.search(rf"(tipo\W{{0,4}}{t}|\|\s*🩸?⚓?\s*{t}\b|\({t}\)|{t}\s*\()", linea, re.I)
                    if not mlab:
                        continue
                    # el nombre debe estar cerca de la etiqueta (mismo sujeto)
                    nidx = lnorm.find(norm(nombre))
                    if abs(nidx - mlab.start()) > 40:
                        continue
                    if any(c in lnorm for c in map(norm, CONTEXTOS_OK)):
                        continue
                    warn(rel, i, f"{nombre} etiquetado '{t}' (canon: {d['tipo']})", linea)

            # 2 · Fósiles (sobre texto normalizado: sin negritas ni acentos)
            for rx, exc, msg in FOSILES:
                if re.search(rx, lnorm, re.I) and not any(norm(e) in lnorm for e in exc):
                    warn(rel, i, f"FÓSIL: {msg}", linea)

            # 3 · Crítico estanca 2
            if RELOJ_CRITICO.search(linea) and "2" not in linea and "dos" not in lnorm:
                warn(rel, i, "un crítico estanca 2 hitos (Cap. 1)", linea)

            # 4 · Aritmética de PG y dado por tamaño
            m = PG_RE.search(linea)
            if m:
                pg, n, dado, mod = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
                mod = int(mod.replace("−", "-").replace(" ", "")) if mod else 0
                media = int(n * (dado + 1) / 2 + mod)
                if abs(media - pg) > 1:
                    warn(rel, i, f"PG {pg} ≠ media de {n}d{dado}{mod:+d} ({media})", linea)
                if mod and n and mod % n != 0:
                    warn(rel, i, f"modificador de PG {mod:+d} no es múltiplo de {n} DG", linea)
                for rx, dsize in DADO_POR_TAMANO:
                    if rx.search(linea):
                        if dado != dsize:
                            warn(rel, i, f"tamaño de la línea pide d{dsize}, statblock usa d{dado}", linea)
                        break

        # 5 · Enlaces y anclas
        for m in re.finditer(r"\]\(([^)#\s]+\.md)(#[^)\s]+)?\)", text):
            target, anchor = m.group(1), m.group(2)
            if target.startswith("http"):
                continue
            resolved = (ROOT / rel).parent.joinpath(target).resolve()
            try:
                relt = resolved.relative_to(ROOT)
            except ValueError:
                warn(rel, 0, f"enlace fuera del proyecto: {target}")
                continue
            if str(relt) not in all_paths and not resolved.exists():
                warn(rel, 0, f"enlace roto: {target}")
            elif anchor and str(relt) in headings:
                slug = anchor[1:].strip("-")
                hs = headings[str(relt)]
                if slug not in hs and slug.rstrip("-") not in hs and not any(h.startswith(slug[:20]) for h in hs):
                    warn(rel, 0, f"ancla no encontrada: {target}{anchor}")

    if problemas:
        print(f"⚠️  {len(problemas)} avisos de canon:")
        for p in problemas:
            print("  " + p)
    else:
        print("✅ Canon coherente: 0 avisos.")
    if "--strict" in sys.argv and problemas:
        sys.exit(1)


if __name__ == "__main__":
    main()

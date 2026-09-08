#!/usr/bin/env python3
"""Genera el índice alfabético del manual con números de página reales.

Uso: python3 gen_indice.py Chronosia_Manual.pdf > partes/indice_alfabetico.md
El build llama a esto entre las dos pasadas del PDF: como el índice es la
última sección del libro, regenerarlo no desplaza ninguna página anterior.
"""
import sys
import unicodedata

# Término del índice -> cadena(s) de búsqueda (si difiere, se busca cada variante)
TERMS = {
    # Personas — aliados y neutrales
    "Aethernus Valcarys": ["Aethernus"], "Amaunator": None, "Aurelius Crane": ["Aurelius"],
    "Balthar Herrumbra": ["Balthar"], "Bram (tabernero)": ["Bram"],
    "Cándano el Penitente": ["Cándano"], "Cerografo (Magistrado)": ["Cerografo"],
    "Cornelius el Inmutable": ["Cornelius"], "Din Goldgear": ["Din Goldgear"],
    "Dimensionalis": None, "Elminster": None, "Galen": None, "Garrett Sin Brújula": ["Garrett"],
    "Gorath": None, "Harlim el Inalterado": ["Harlim"], "Ignis": None,
    "Jarlaxle": None, "Kael (Comandante)": ["Kael"], "Kaelthas": None,
    "Kaoros el Sordo": ["Kaoros"], "Karkesh": None, "Lucienne Rietveldt": ["Lucienne"],
    "Madame Coral": None, "Manshoon": None, "Marcus (Capitán)": ["Marcus"],
    "Medusa la Eterna": ["Medusa"], "Móreve (Capitán)": ["Móreve"],
    "Nereia (Reina)": ["Nereia"], "Oviran (Maestro)": ["Oviran"],
    "Serapis el Retroceso": ["Serapis"], "Teach, Edward (Barbanegra)": ["Teach"],
    "Tempus el Fragmentado": ["Tempus"], "Tessaly Bifronte": ["Tessaly"],
    "Thaddeus Ironwright": ["Thaddeus"], "Tholassa": None, "Thyra la Suspendida": ["Thyra"],
    "Varrak del Horizonte": ["Varrak"], "Velka": None, "Volo": None,
    "Vorthak (Lord)": ["Vorthak"], "Ymir el Eterno Invierno": ["Ymir"],
    "Yrindra (Matrona)": ["Yrindra"], "Zephyr el Saltamundos": ["Zephyr"],
    "Las Gemelas (Lyra y Nyx)": ["Gemelas"], "Voidar": None,
    # Lugares
    "Abysara": None, "Cronópolis": None, "Cronosgate": None,
    "Fortaleza de Acero": None, "Fuerte Negro": None, "Galería de Azogue": None,
    "La Última Hora (taberna)": ["La Última Hora"], "Ojo del Tiempo": None,
    "Plaza del Reloj": None, "Portal de las Estrellas": None,
    "Torre de la Eternidad": None, "Valle de la Aguja": None, "Xal'azar": None,
    "Waterdeep": None, "Barovia": None, "Menzoberranzan": None,
    # Objetos y artefactos
    "Arena del Tiempo": None, "Carcasa Dimensional": None,
    "Cerrador de Portales": None, "Contador del Ritual": None,
    "Cristal de Poder": None, "Cristal Estabilizador": None,
    "Cronómetro de Realidades": None, "Espejo de Realidad Fragmentada": None,
    "Excavadora Dimensional": None, "Llave chroniana": ["llave chroniana"],
    "Motor de Viento": None, "Núcleo Temporal": None,
    "Perla del Vacío": None, "Rifle Anti-Magia": None, "Rotor Infinito": None,
    "Talismán de Interceptación": ["Talismán"],
    # Facciones y pueblos
    "Anacronistas": None, "Bregan D'aerthe": None, "Chronianos": None,
    "Cronófagos": None, "Oceánicos": None, "Resistencia, La": ["La Resistencia"],
    "Zhentarim": None,
    # Conceptos y mecánicas
    "Cronosellado": None, "Final D": None, "Mapa de Puertas": None,
    "Reloj del Ritual": None, "SALTO (de Thyra)": ["SALTO"],
    "Zin-Carla": None, "Hipo del Contador": ["hipo"],
}

MAX_PAGES = 4


def main(pdf_path):
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    pages_text = [(p.extract_text() or "") for p in reader.pages]

    # Saltar portada + índice de contenidos: empezar en la portadilla de la Parte I
    start = 0
    for i, t in enumerate(pages_text):
        if "PARTE I — PREPARACIÓN" in t and i > 2:
            start = i
            break

    entries = []
    for label, variants in sorted(TERMS.items(), key=lambda kv: strip_accents(kv[0]).lower()):
        needles = variants or [label]
        counts = {}
        for i in range(start, len(pages_text)):
            c = sum(pages_text[i].count(n) for n in needles)
            if c:
                counts[i + 1] = c
        if not counts:
            continue
        hits = sorted(counts)
        # primera aparición + las 2-3 páginas con más menciones (la ficha/sección principal, en negrita)
        main = sorted(sorted(counts, key=counts.get, reverse=True)[:MAX_PAGES - 1])
        shown = sorted(set([hits[0]] + main))[:MAX_PAGES]
        parts = [f"**{pg}**" if pg in main and counts[pg] >= 3 else str(pg) for pg in shown]
        pages = ", ".join(parts) + ("…" if len(hits) > MAX_PAGES else "")
        entries.append((label, pages))

    print("\\newpage\n")
    print("# ÍNDICE ALFABÉTICO\n")
    print("*Personas, lugares, artefactos y conceptos — con la página de sus primeras apariciones "
          f"(a partir de la {MAX_PAGES}ª, «…»). Generado automáticamente en cada build.*\n")
    letter = ""
    line = []
    for label, pages in entries:
        first = strip_accents(label)[0].upper()
        if first != letter:
            if line:
                print(" · ".join(line) + "\n")
            letter = first
            line = [f"**{letter}** — *{label}* {pages}"]
        else:
            line.append(f"*{label}* {pages}")
    if line:
        print(" · ".join(line))


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


if __name__ == "__main__":
    main(sys.argv[1])

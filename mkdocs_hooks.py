"""Hooks de MkDocs para la web de Chronosia.

1) Redirige las imágenes a las copias optimizadas para web (assets/web/...);
   los originales (mapas/bestiario/objetos_magicos) están gitignorados.
2) Limpia los emojis DECORATIVOS de los títulos/texto para que la web no se
   vea recargada, CONSERVANDO los semánticos (círculos de color de estado,
   avisos, sí/no) y las flechas «→». La fuente .md no se toca (Obsidian y el
   resto siguen igual).
"""
import re

# Emojis SEMÁNTICOS que se conservan (estado / aviso / sí-no).
_KEEP = {
    "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "⚪", "⚫",
    "⚠", "✅", "❌", "⛔", "❗", "❓", "⭐", "🚫", "✔",
}

# Rangos de emoji a eliminar. NO incluye las flechas (U+2190–U+21FF),
# que se conservan. Captura el emoji (+ selector de variación opcional) y
# se "come" un espacio posterior para no dejar dobles espacios.
_EMOJI = re.compile(
    "([\U0001F300-\U0001FAFF\U00002300-\U000023FF\U00002600-\U000026FF"
    "\U00002700-\U000027BF\U00002B00-\U00002BFF\U0001F1E6-\U0001F1FF]️?)[ \t]?"
)


def _strip_decorative_emojis(text: str) -> str:
    def repl(m):
        core = m.group(1).rstrip("️")
        return m.group(0) if core in _KEEP else ""
    return _EMOJI.sub(repl, text)


def on_page_markdown(markdown, **kwargs):
    md = markdown.replace("assets/bestiario/", "assets/web/bestiario/")
    md = md.replace("assets/objetos_magicos/", "assets/web/objetos_magicos/")
    # los mapas pasan de .png (original) a .jpg (web)
    md = re.sub(r"assets/mapas/([^)\s\"']+)\.png", r"assets/web/mapas/\1.jpg", md)
    md = _strip_decorative_emojis(md)
    return md

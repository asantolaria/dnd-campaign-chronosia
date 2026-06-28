"""Hook de MkDocs: redirige las imágenes a las copias optimizadas para web.

Los originales (assets/mapas, assets/bestiario, assets/objetos_magicos) están
gitignorados y son pesados. En su lugar la web usa assets/web/... (commiteado).
Los mapas se sirven en JPG. La fuente .md no se toca (Obsidian sigue usando los
originales en local).
"""
import re


def on_page_markdown(markdown, **kwargs):
    md = markdown.replace("assets/bestiario/", "assets/web/bestiario/")
    md = md.replace("assets/objetos_magicos/", "assets/web/objetos_magicos/")
    # los mapas pasan de .png (original) a .jpg (web)
    md = re.sub(r"assets/mapas/([^)\s\"']+)\.png", r"assets/web/mapas/\1.jpg", md)
    return md

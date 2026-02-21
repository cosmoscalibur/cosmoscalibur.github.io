from typing import Any, Dict

from sphinx.application import Sphinx


def setup(app: Sphinx) -> Dict[str, Any]:
    app.connect("html-page-context", add_lang_context)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def add_lang_context(app, pagename, templatename, context, doctree):
    lang_map = {"es": ("en", "English"), "en": ("es", "Español")}
    parts = pagename.split("/")

    if len(parts) > 1 and parts[0] in lang_map:
        current_lang = parts[0]
        alt_lang, alt_label = lang_map[current_lang]
        alt_docname = alt_lang + "/" + "/".join(parts[1:])

        if alt_docname in app.env.all_docs:
            context["lang_alt_url"] = context["pathto"](alt_docname)
            context["lang_alt_label"] = alt_label
            context["lang_alt_code"] = alt_lang
            context["lang_current_code"] = current_lang

            base_url = (app.config.html_baseurl or "").rstrip("/")
            alt_uri = app.builder.get_target_uri(alt_docname)
            cur_uri = app.builder.get_target_uri(pagename)
            context["lang_alt_abs_url"] = f"{base_url}/{alt_uri}"
            context["lang_current_abs_url"] = f"{base_url}/{cur_uri}"

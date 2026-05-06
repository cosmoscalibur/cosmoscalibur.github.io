"""Theme i18n — JSON-based translation loader.

Loads translation strings from ``locale/*.json`` files. Built-in ``es``
and ``en`` are shipped with the theme. Custom languages can be added by
placing a JSON file at ``{confdir}/locale/{lang}.json`` (user override
takes priority) or ``themes/cosmoscalibur/locale/{lang}.json``.

Usage in Python::

    from .i18n import get_translation, get_known_langs

    label = get_translation("es", "home", app.confdir)
    langs = get_known_langs(app)

Usage in Jinja2 templates (via ``t()`` injected by ``context.py``)::

    {{ t("home") }}
    {{ t("built_with", sphinx="...", cosmoblog="...") }}
"""

import json
import functools
from pathlib import Path
from typing import Any

from sphinx.application import Sphinx

_THEME_LOCALE_DIR = Path(__file__).parent.parent / "locale"


@functools.lru_cache(maxsize=None)
def _load_translations(lang: str, confdir: str) -> dict[str, Any]:
    """Load translations for a language.

    Priority:
    1. ``{confdir}/locale/{lang}.json`` (user override)
    2. ``themes/cosmoscalibur/locale/{lang}.json`` (theme built-in)
    3. ``themes/cosmoscalibur/locale/en.json`` (fallback)
    """
    user_file = Path(confdir) / "locale" / f"{lang}.json"
    theme_file = _THEME_LOCALE_DIR / f"{lang}.json"
    fallback_file = _THEME_LOCALE_DIR / "en.json"

    # Always start from the English fallback so missing keys degrade gracefully
    try:
        data = json.loads(fallback_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise RuntimeError(
            f"Theme i18n: fallback locale file missing or corrupted: {fallback_file}"
        ) from exc

    if theme_file.exists() and theme_file != fallback_file:
        override = json.loads(theme_file.read_text(encoding="utf-8"))
        data.update(override)

    if user_file.exists():
        override = json.loads(user_file.read_text(encoding="utf-8"))
        data.update(override)

    return data


def get_translation(lang: str, key: str, confdir: str, **kwargs: Any) -> str:
    """Get a translated string by key, with optional format variables.

    Parameters
    ----------
    lang
        Language code (e.g. ``"es"``, ``"en"``).
    key
        Translation key matching a top-level key in the locale JSON.
    confdir
        Path to the Sphinx project's ``conf.py`` directory.
    **kwargs
        Format variables substituted via ``str.format()``.

    Returns
    -------
    str
        Translated string, or *key* itself if not found.
    """
    translations = _load_translations(lang, confdir)
    template = translations.get(key, key)
    if isinstance(template, dict):
        # Nested objects (like "admonitions") are not simple strings
        return str(template)
    if kwargs:
        return template.format(**kwargs)
    return template


def get_admonition_map(lang: str, confdir: str) -> dict[str, str]:
    """Get admonition title translations for a language.

    Returns a dict mapping source titles (in the default build language)
    to target titles for *lang*.  Returns an empty dict if the locale
    file has no ``"admonitions"`` section.
    """
    translations = _load_translations(lang, confdir)
    admonitions = translations.get("admonitions", {})
    if isinstance(admonitions, dict):
        return admonitions
    return {}


def get_known_langs(app: Sphinx) -> set[str]:
    """Derive known languages from cosmoblog's directory discovery.

    Falls back to ``{language}`` if cosmoblog hasn't discovered any.
    """
    engine = getattr(app.env, "cosmoblog", None)
    if engine and engine.languages:
        return engine.languages
    # Fallback: use cosmoblog config or default language
    langs = getattr(app.config, "cosmoblog_languages", None)
    if langs:
        return langs
    default = getattr(app.config, "blog_default_language", None) or app.config.language
    return {default}

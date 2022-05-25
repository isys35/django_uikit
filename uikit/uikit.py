from importlib import import_module

from django.conf import settings

UIKIT_DEFAULTS = {
    "required_css_class": "",
    "error_css_class": "uk-form-danger",
    "success_css_class": "uk-form-success",
    "set_placeholder": True,
    "field_renderers": {
        "default": "uikit.renderers.FieldRenderer",
        "inline": "uikit.renderers.InlineFieldRenderer"
    }
}


def i18n_enabled():
    """Return the projects i18n setting."""
    return getattr(settings, "USE_I18N", False)


def get_uikit_setting(name, default=None):
    """Read a setting."""
    # Start with a copy of default settings
    UIKIT = UIKIT_DEFAULTS.copy()

    # Override with user settings from settings.py
    UIKIT.update(getattr(settings, "UIKIT", {}))

    # Update use_i18n
    UIKIT["use_i18n"] = i18n_enabled()

    return UIKIT.get(name, default)


def get_renderer(renderers, **kwargs):
    layout = kwargs.get("layout", "")
    path = renderers.get(layout, renderers["default"])
    mod, cls = path.rsplit(".", 1)
    return getattr(import_module(mod), cls)


def get_field_renderer(**kwargs):
    renderers = get_uikit_setting("field_renderers")
    return get_renderer(renderers, **kwargs)

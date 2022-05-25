from collections.abc import Mapping

from django.forms.utils import flatatt
from django.template.loader import get_template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .text import text_value


def split_css_classes(css_classes):
    """Turn string into a list of CSS classes."""
    classes_list = text_value(css_classes).split(" ")
    return [c for c in classes_list if c]


def add_css_class(css_classes, css_class, prepend=False):
    """Add a CSS class to a string of CSS classes."""
    classes_list = split_css_classes(css_classes)
    classes_to_add = [c for c in split_css_classes(css_class) if c not in classes_list]
    if prepend:
        classes_list = classes_to_add + classes_list
    else:
        classes_list += classes_to_add
    return " ".join(classes_list)


def render_template_file(template, context=None):
    """Render a Template to unicode."""
    assert isinstance(context, Mapping)
    template = get_template(template)
    return template.render(context)


def render_tag(tag, attrs=None, content=None, close=True):
    """Render a HTML tag."""
    builder = "<{tag}{attrs}>{content}"
    if content or close:
        builder += "</{tag}>"
    return format_html(builder, tag=tag, attrs=mark_safe(flatatt(attrs)) if attrs else "", content=text_value(content))

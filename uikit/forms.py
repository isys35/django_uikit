from django.utils.safestring import mark_safe

from uikit.exceptions import UIkitError
from uikit.text import text_value
from uikit.uikit import get_field_renderer
from uikit.utils import render_tag, add_css_class
from django.forms import EmailInput, NumberInput, PasswordInput, Textarea, TextInput, URLInput

FORM_GROUP_CLASS = "uk-margin"


def render_field(field, **kwargs):
    """Render a field to a UIkit layout."""
    renderer_cls = get_field_renderer(**kwargs)
    return renderer_cls(field, **kwargs).render()


def render_label(content, label_for=None, label_class="uk-form-label", label_title=""):
    """Render a label with content."""
    attrs = {}
    if label_for:
        attrs["for"] = label_for
    if label_class:
        attrs["class"] = label_class
    if label_title:
        attrs["title"] = label_title
    return render_tag("label", attrs=attrs, content=content)


def render_form_group(content, css_class=FORM_GROUP_CLASS):
    """Render a UIkit form group."""
    return '<div class="{css_class}">{content}</div>'.format(css_class=css_class, content=content)


def is_widget_with_placeholder(widget):
    """
    Return whether this widget should have a placeholder.
    Only text, text area, number, e-mail, url, password, number and derived inputs have placeholders.
    """
    return isinstance(widget, (TextInput, Textarea, NumberInput, EmailInput, URLInput, PasswordInput))


def render_button(
        content,
        button_type=None,
        button_class="uk-button",
        size="",
        href="",
        name=None,
        value=None,
        title=None,
        extra_classes="",
        id="",
):
    """Render a button with content."""
    attrs = {}
    classes = button_class
    size = text_value(size).lower().strip()
    if size == "small":
        classes = add_css_class(classes, "uk-button-small")
    elif size == "large":
        classes = add_css_class(classes, "uk-button-large")
    if button_type:
        if button_type not in ("submit", "reset", "button", "link"):
            raise UIkitError(
                (
                    'Parameter "button_type" should be "submit", "reset", "button", "link" or empty '
                    '("{button_type}" given).'
                ).format(button_type=button_type)
            )
        if button_type != "link":
            attrs["type"] = button_type
        if button_type == 'submit':
            classes = add_css_class(classes, "uk-button-primary")
    classes = add_css_class(classes, extra_classes)
    attrs["class"] = classes
    if href:
        tag = "a"
        if button_type and button_type != "link":
            raise UIkitError(
                'Button of type "{button_type}" is not allowed a "href" parameter.'.format(button_type=button_type)
            )
        attrs["href"] = href
        # Specify role for link with button appearance
        attrs.setdefault("role", "button")
    else:
        tag = "button"
    if id:
        attrs["id"] = id
    if name:
        attrs["name"] = name
    if value:
        attrs["value"] = value
    if title:
        attrs["title"] = title
    return render_tag(tag, attrs=attrs, content=mark_safe(content))

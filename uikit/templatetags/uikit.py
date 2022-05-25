from django import template

from uikit.forms import render_field, render_button

register = template.Library()


@register.simple_tag
def uikit_field(*args, **kwargs):
    return render_field(*args, **kwargs)


@register.simple_tag
def uikit_button(*args, **kwargs):
    return render_button(*args, **kwargs)

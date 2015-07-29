"""
Created by Tim Fletcher https://gist.github.com/TimFletcher/034e799c19eb763fa859
"""

from django import template
register = template.Library()
 
@register.filter(name='add_attrs')
def add_attrs(field, css):
    attrs = {}
    definition = css.split(',')
 
    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v
 
    return field.as_widget(attrs=attrs)
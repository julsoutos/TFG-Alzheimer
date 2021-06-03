from django import template
from patient.utils import birth

register = template.Library()


@register.filter()
def age(value):
    return birth(value)

@register.filter()
def category(value):
    if value == "Memory":
        return "Memoria"
    if value == "Attention":
        return "Atención"
    if value == "Calculus":
        return "Cálculo"
    if value == "Perception":
        return "Percepción"
    if value == "Language":
        return "Lenguaje"
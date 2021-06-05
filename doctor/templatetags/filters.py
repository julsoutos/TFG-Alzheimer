from django import template
from patient.utils import birth
from principal.models import Activity_Training

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

@register.filter()
def activities_all(training):
    all_activities = Activity_Training.objects.filter(patient_training__pk=training)
    return all_activities.count()

@register.filter()
def activities_pending(training):
    all_activities = Activity_Training.objects.filter(patient_training__pk=training)
    pending_activities = Activity_Training.objects.filter(patient_training__pk=training, is_completed=False)
    return all_activities.count() -  pending_activities.count()

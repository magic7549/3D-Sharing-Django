from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def subtract_days(value, days):
    return value - timezone.timedelta(days=days)


@register.filter
def add_days(value, days):
    return value + timezone.timedelta(days=days)
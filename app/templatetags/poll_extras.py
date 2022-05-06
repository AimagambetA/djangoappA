from django import template
from app.models import *


register = template.Library()

@register.simple_tag()
def get_comment2():
    return Comment.objects.all()
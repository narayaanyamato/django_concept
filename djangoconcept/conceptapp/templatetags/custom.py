from django import template
register = template.Library()

def first_five_upper(value):
    result = value[:3].upper()
    return result

def first_n_upper(value,n):
    result = value[:n].upper()
    return result

register.filter('ffu',first_five_upper)
register.filter('fnu',first_n_upper)

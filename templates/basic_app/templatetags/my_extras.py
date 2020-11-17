from django import template
register = template.Library()

@register.filer(name='cut')
def cut(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut)

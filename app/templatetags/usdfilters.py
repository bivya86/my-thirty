from django import template
register=template.Library()

def swapping(value):
    return value.swapcase()
register.filter('swap',swapping)

@register.filter()
def counting(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')
import datetime
from django import template
register = template.Library()

@register.filter(name='StartOfActive',expects_localtime=True)
def DateStartOfActive(value):
    html_date = datetime.datetime.strftime(value, '%Y-%m-%dT%H:%M')
    return(html_date)


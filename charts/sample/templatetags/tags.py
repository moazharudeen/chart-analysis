from django import template
from django.utils.safestring import SafeString
from django.db import connections
from sample.models import dashboard


register = template.Library()

@register.simple_tag
def render_dashboard_tabs(request):
    ids = dashboard.objects.all().values_list('id','dashboard_name' )
    print(dict(ids))
    
    
    # quried_data = dict(zip(ids, dashboard_name))
    # print('data', quried_data)
    result = ''
    for i,j in dict(ids).items():
        print(i)
        result = result + f'''<li><a class="dropdown-item" target="_blank" href="/dashboard/?id={str(i)}">{str(j)}</a></li>'''
        # result = result + f'''<li><a class="dropdown-item" href="open_flower% url 'dashboard' {i} %close_flower">{quried_data[i]}</a></li>'''

    # result = result.replace('open_flower', '{').replace('close_flower', '}')
    return SafeString(result)

@register.filter
def types(value):
    return str(value)
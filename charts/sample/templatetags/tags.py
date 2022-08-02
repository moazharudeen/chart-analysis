from django import template
from django.utils.safestring import SafeString
from django.db import connections
from sample.models import dashboard


register = template.Library()

@register.simple_tag
def render_dashboard_tabs(request):
    ids = dashboard.objects.all().values_list('id', flat=True)
    dashboard_name = dashboard.objects.all().values_list('dashboard_name', flat=True)
    
    # quried_data = dict(zip(ids, dashboard_name))
    # print('data', quried_data)
    result = ''
    for i,j in zip(ids, dashboard_name):
        result = result + f'''<li><a class="dropdown-item" href="/dashboard/?id={i}">{j}</a></li>'''
        # result = result + f'''<li><a class="dropdown-item" href="open_flower% url 'dashboard' {i} %close_flower">{quried_data[i]}</a></li>'''

    # result = result.replace('open_flower', '{').replace('close_flower', '}')
    return SafeString(result)
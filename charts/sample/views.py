import uuid

import string
import random
import pandas as pd

from django.shortcuts import render, redirect
from .models import ChartName, ChartSheet, chartData, data_column, aggregate_functions, dashboard
from .forms import charttypeform
from django.db import connections
from .chartdata import chart_dict
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.middleware import csrf
# Create your views here.
import sqlite3 as sq
from .filter_template import *

def col_names(t_name):
    cursor = connections['default'].cursor()
    cursor.execute("PRAGMA table_info({}) ".format(t_name))
    data = cursor.fetchall()
    return [i[1] for i in data]




@login_required()
def select_chart(request):
    if request.method == 'POST':
        post_data = dict(request.POST)
        print(post_data)
        if 'csrfmiddlewaretoken' in post_data and 'chart_type' in post_data:
            
            if post_data.get('chart_type')[0] == 'column2d':
                request.session['chart_type'] = post_data.get('chart_type')[0]
                
                return redirect('/create-chart/')
    return render(request, 'index.html', {})

@login_required()      
def create_chart(request):
    
    chart_type = request.session.get('chart_type')
    if request.method == 'POST':
        post_data = dict(request.POST)
        print(post_data)
        if 'csrfmiddlewaretoken' in post_data:
            chart_type = request.session.get('chart_type')
            if chart_type in chart_dict:
                if chart_type == 'column2d':
                    chartid = uuid.uuid4()
                    raw_script = chart_dict.get(chart_type)
                    x_axis = post_data.get('x_axis')[0]
                    y_axis = post_data.get('y_axis')[0]
                    aggregated = post_data.get('aggregation')[0]
                    title  = post_data.get('chart_title')[0],
                    sub_title = post_data.get('chart_sub_title')[0],
                    x_axis_name = post_data.get('x_axis_name')[0],
                    y_axis_name = post_data.get('y_axis_name')[0],
                    number_suffix = post_data.get('number_suffix')[0],
                    query = f''' select {x_axis}, {aggregated}({y_axis}) from {settings.DATA_TABLE} group by {x_axis}'''
                    print("query", query)
                    cursor = connections['default'].cursor()
                    cursor.execute(query)
                    quried_data = dict(cursor.fetchall())
                    data = []
                    for i in quried_data:
                        sub_data_dict = {}
                        sub_data_dict['label'] = i
                        sub_data_dict['value'] = quried_data[i]
                        data.append(sub_data_dict)
                    res = ''.join(random.choices(string.ascii_letters, k=7))
                    script = raw_script.format(data, title[0], sub_title[0], x_axis_name[0],y_axis_name[0], number_suffix[0], chartid, res )
                    filter_chart_data = raw_script.format('replaceable_data', title[0], sub_title[0], x_axis_name[0],y_axis_name[0], number_suffix[0], chartid, res )
                    print("====================script======================")
                    print(script)
                    filter_chart_data = filter_chart_data.replace('flower_close', '}').replace('flower_open', '{')
                    script = script.replace('flower_close', '}').replace('flower_open', '{')
                    print("====================new script======================")
                    print(script)
                    request.session['script'] = script
                    request.session['chart_type'] = chart_type
                    request.session['query'] = query
                    request.session['filter_chart_data'] = filter_chart_data
                    
                    request.session['title'] = title[0]
                    # print(script)
                    context = {
                        'script': script,
                       
                        # 'data' : data,
                        'chart_type': chart_type,
                        'fields':data_column,
                        'aggregate_functions':aggregate_functions,
                    }
                    return render(request, 'creat_chart.html', context)
    context = {
        'chart_type': chart_type,
        'fields':data_column,
        'aggregate_functions':aggregate_functions,
    }
    return render(request, 'creat_chart.html', context)

@login_required()
def chart_save(request):
    print(request.session.get('script'))
    if request.method == 'POST':
        post_data = dict(request.POST)
        if 'csrfmiddlewaretoken' in post_data:
            chartData.objects.create(
                chart_name = request.session.get('title'),
                chart_data = request.session.get('script'),
                user = request.user,
                chart_type = request.session.get('chart_type'),
                chart_query = request.session.get('query'),
                filter_chart_data = request.session.get('filter_chart_data'),
            )
            pass

    script = request.session.get('script')
    chart_type = request.session.get('chart_type')

    context = {
        'script': script,
    
        # 'data' : data,
        'chart_type': chart_type,
        'fields':data_column,
        'aggregate_functions':aggregate_functions,
    }
    return render(request, 'creat_chart.html', context)

@login_required()
def chart_list(request):
    charts = chartData.objects.all()
    if request.method == 'GET':
        id_name = request.GET.get('id', None)
    if id_name:
        single_chart = chartData.objects.filter(id=id_name).values_list('chart_data', flat=True)[0]
    else:
        single_chart= None

    context = {
        'charts':charts,
        'single_chart':single_chart,
        'id_name':id_name
    }
    return render(request, 'chart_list.html', context)

@login_required()
def create_dashboard(request):
    final_script = ''
    per_row = {
        '1':12,
        '2':6,
        '3':4,
        '4':3
    }
    charts_name = chartData.objects.all().values_list('chart_name', flat=True)
    table_name = settings.DATA_TABLE
    query = f'select * from {table_name}'
    cursor = connections['default'].cursor()
    cursor.execute(query)
    quried_data = cursor.fetchall()

    df = pd.DataFrame(quried_data)
    df.columns = col_names(table_name)
    
    object_columns = list(df.select_dtypes(include=['object']).columns)
    
    




    # print(request.POST)
    # {'csrfmiddlewaretoken': ['5Djq7QVBLvZ6e9AxQLQEOe5a7Eoc8ntnegZZiWzx82oesk2lcxZ5QNSf3GpOhLEu'], 'dashboard_name': ['litgation'], 'per_row_chart': ['1', '2'], 'chart_name': ['new title', 'title']}
    if request.method == 'POST':
        post_data = dict(request.POST)
        print(post_data)
        if 'csrfmiddlewaretoken' in post_data:
            dashboard_name = post_data.get('dashboard_name')[0]
            filters = post_data.get('filters')
            filter_dict = {}
            for i in filters:
                filter_dict[i] = df[i].unique()

            form = '' + f"""<input type="hidden" name="csrfmiddlewaretoken" value="{csrf.get_token(request)}"> """
            for i in filter_dict:
                main_div = f"""

                            <div class="col-sm-2" style="margin-right: 50px;">
                                <div class="form-group">
                                    <label for="{i}_select">{i}</label><br/>
                                    <select class="form-control form-control-lg" name="{i}" multiple="multiple"
                                            id="{i}_select" style="border: 2px solid #20BCAE;">
                                            """
                form = form + main_div
                for j in filter_dict.get(i, ''):

                    option = f"""<option value="{j}">{j}</option>"""
                    form = form + option


                end =                            """
                                    </select>
                                </div>
                            </div> """
                form = form + end
            form = form + """<script type="text/javascript">"""
            for i in filter_dict:
                script = f"""
                    $('#{i}_select').selectize();
                """
                form = form + script

            form = form + "</script>"

            final_script = final_script + template_top + form + template_bottom
            filter_script = final_script
            per_row_chart_list = post_data.get('per_row_chart')
            chart_name_list = post_data.get('chart_name')
            query = 'select chart_name, chart_data from chartdata'
            cursor = connections['default'].cursor()
            cursor.execute(query)
            quried_data = dict(cursor.fetchall())
            # print(quried_data)
            
            for i,j in zip(chart_name_list, per_row_chart_list):
                # print(i)
                if i in quried_data:
                    # print(quried_data[i])
                    final_script = final_script + f'<div class="col-md-{per_row[j]}">' + quried_data[i] + '</div>'

            request.session['final_script'] = final_script
            request.session['dashboard_name'] = dashboard_name

            print('final_script', final_script)
            context = {
                'final_script':final_script,
                'charts_name':charts_name,
                'per_row':per_row,
                'object_columns':object_columns,
                'filter_dict':filter_dict
                
            }
            return render(request, 'create_dashboard.html', context)
            


    context = {
        'final_script':final_script,
        'charts_name':charts_name,
        'per_row':per_row,
        'object_columns':object_columns
    }
    return render(request, 'create_dashboard.html', context)

@login_required()
def dashboard_save(request):
    per_row = {
        '1':12,
        '2':6,
        '3':4,
        '4':3
    }
    charts_name = chartData.objects.all().values_list('chart_name', flat=True)
    dashboard_name = request.session.get('dashboard_name')
    final_script = request.session.get('final_script').replace('disabled', '')
    if request.method == 'POST':
        post_data = dict(request.POST)
        if 'csrfmiddlewaretoken' in post_data:
            dashboard.objects.create(
                dashboard_name = dashboard_name,
                dashboard_data = final_script
            )
            pass

    
    

    context = {
       
    
        # 'data' : data,
        'final_script': final_script,
        'charts_name':charts_name,
        'per_row':per_row
    }
    return render(request, 'create_dashboard.html', context)

@login_required()
def dashboard_view(request):
    if request.method == 'GET':
        uuid = request.GET.get('id')
        get_data = dict(request.GET)
        print(get_data)
        # get_data = {'id': ['fbe98e06-b354-4dde-a3ce-5e7356e62c6f'], 'filter_status': ['True'], 'csrfmiddlewaretoken': ['FlEtpxer7oqf2D4OfGs5Haygy1clVHwvqRG42HpvooVms5Yezfq15eTTZyKZzaNO'], 'varity': ['Setosa', 'Virginica']}
        if 'filter_status' in get_data:
            quried_data = dashboard.objects.filter(
                id=uuid
            ).values_list('dashboard_data', 'dashboard_name')
        else:
            # print('uuid', uuid)
            quried_data = dashboard.objects.filter(
                id=uuid
            ).values_list('dashboard_data', 'dashboard_name')
            # print(quried_data)
            context = {
                'data':quried_data[0][0],
                'id':uuid,
                'dashboard_name':quried_data[0][1],
                'val':'6e3c71db-3990-45d9-940d-4ebac70f3e4d'
            }

            return render(request, 'dashboard.html', context)

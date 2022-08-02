import uuid
from django.urls import path
from .views import *

urlpatterns = [
    path('', select_chart, name='select_chart'),
    path('create-chart/', create_chart, name='create_chart'),
    path('chart-save/', chart_save, name='chart_save'),
    path('chart-list/', chart_list, name='chart_list'),
    path('create-dashboard/', create_dashboard, name='create_dashboard'),
    path('dashboard-save/', dashboard_save, name='dashboard_save'),
    path('dashboard/', dashboard_view, name='dashboard_view'),


]
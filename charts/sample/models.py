import uuid
from django.db import models

# Create your models here.
class ChartName(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         db_index=True,
         editable = False
         )
    chart_type = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
         return self.chart_type



class ChartSheet(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         db_index=True,
         editable = False
         )
#     chart_type = models.ForeignKey(ChartName, on_delete=models.CASCADE)
    chart_title = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='chart_title')
    chart_sub_title = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='chart_sub_title')
    x_axis_name = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='x_axis_name')
    y_axis_name = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='y_axis_name')
    number_suffix = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='number_suffix')
    labels = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='labels')
    values =  models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='values')

    def __str__(self):
         return self.chart_title

class chartData(models.Model):
     id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         db_index=True,
         editable = False
         )
     chart_name = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='chart_name')
     chart_data = models.TextField()

     class Meta:
        db_table = 'chartdata'

     def __str__(self):
          return self.chart_name

class dashboard(models.Model):
     id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         db_index=True,
         editable = False
         )
     dashboard_name = models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='dashboard_name')
     dashboard_data = models.TextField()

     class Meta:
        db_table = 'dashboarddata'

     def __str__(self):
          return self.dashboard_name + str(self.id)

data_column = [
     'sepal_length',
     'sepal_width',
     'petal_length',
     'petal_length',
     'varity'
]
aggregate_functions = [
     'Count',
     'Sum',
     'Avg'
]

class Data(models.Model):
    sepal_length = models.IntegerField(blank=True, null=True, db_column='sepal_length')
    sepal_width = models.IntegerField(blank=True, null=True, db_column='sepal_width')
    petal_length = models.IntegerField(blank=True, null=True, db_column='petal_length')
    petal_width = models.IntegerField(blank=True, null=True, db_column='petal_width')
    varity =  models.CharField(max_length=255, db_index=True, blank=True, null=True, db_column='varity')

    class Meta:
        db_table = 'data'
    def __str__(self):
         return self.varity


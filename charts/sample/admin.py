from import_export import resources
from import_export.admin import ImportExportModelAdmin


from .models import Data, chartData, dashboard
from django.contrib import admin

# Register your models here.
class DataResource(resources.ModelResource):

    class Meta:
        model = Data

class DataAdmin(ImportExportModelAdmin):
    resource_class = DataResource

admin.site.register(Data, DataAdmin)
admin.site.register(chartData)
admin.site.register(dashboard)

# Generated by Django 4.0.6 on 2022-08-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0014_chartdata_chart_type_chartdata_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartdata',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
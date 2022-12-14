# Generated by Django 4.0.6 on 2022-08-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0005_alter_data_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartsheet',
            name='chart_type',
        ),
        migrations.AlterField(
            model_name='chartsheet',
            name='chart_sub_title',
            field=models.CharField(blank=True, db_column='chart_sub_title', db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chartsheet',
            name='chart_title',
            field=models.CharField(blank=True, db_column='chart_title', db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chartsheet',
            name='labels',
            field=models.CharField(blank=True, db_column='labels', db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chartsheet',
            name='number_suffix',
            field=models.CharField(blank=True, db_column='number_suffix', db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chartsheet',
            name='values',
            field=models.CharField(blank=True, db_column='values', db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chartsheet',
            name='x_axis_name',
            field=models.CharField(blank=True, db_column='x_axis_name', db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chartsheet',
            name='y_axis_name',
            field=models.CharField(blank=True, db_column='y_axis_name', db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='petal_length',
            field=models.IntegerField(blank=True, db_column='petal_length', null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='petal_width',
            field=models.IntegerField(blank=True, db_column='petal_width', null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sepal_length',
            field=models.IntegerField(blank=True, db_column='sepal_length', null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sepal_width',
            field=models.IntegerField(blank=True, db_column='sepal_width', null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='varity',
            field=models.CharField(blank=True, db_column='varity', db_index=True, max_length=255, null=True),
        ),
    ]

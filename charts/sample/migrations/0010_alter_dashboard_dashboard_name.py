# Generated by Django 4.0.6 on 2022-08-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0009_dashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='dashboard_name',
            field=models.CharField(blank=True, db_column='dashboard_name', db_index=True, max_length=255, null=True),
        ),
    ]
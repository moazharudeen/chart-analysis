# Generated by Django 4.0.6 on 2022-08-02 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0006_remove_chartsheet_chart_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartdata',
            name='chart_sheet',
        ),
        migrations.AlterField(
            model_name='chartdata',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
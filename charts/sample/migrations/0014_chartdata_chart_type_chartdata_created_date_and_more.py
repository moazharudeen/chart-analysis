# Generated by Django 4.0.6 on 2022-08-16 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sample', '0013_chartdata_chart_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartdata',
            name='chart_type',
            field=models.CharField(blank=True, db_column='chart_type', db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chartdata',
            name='created_date',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chartdata',
            name='filter_chart_data',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chartdata',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
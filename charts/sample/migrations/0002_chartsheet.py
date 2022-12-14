# Generated by Django 4.0.6 on 2022-08-01 06:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartSheet',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('chart_title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('chart_sub_title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('x_axis_name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('y_axis_name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('number_suffix', models.CharField(db_index=True, max_length=255, unique=True)),
                ('labels', models.CharField(db_index=True, max_length=255, unique=True)),
                ('values', models.CharField(db_index=True, max_length=255, unique=True)),
                ('chart_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.chartname')),
            ],
        ),
    ]

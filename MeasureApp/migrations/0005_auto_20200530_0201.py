# Generated by Django 3.0.3 on 2020-05-30 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeasureApp', '0004_auto_20200529_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasureHistory',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('width', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'measure_history',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='upload',
            options={'managed': False},
        ),
    ]

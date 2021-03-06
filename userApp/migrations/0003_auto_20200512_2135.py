# Generated by Django 3.0.3 on 2020-05-12 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20200512_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationWasteInformation',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('dong', models.CharField(blank=True, max_length=45, null=True)),
                ('discharge_day', models.CharField(blank=True, max_length=45, null=True)),
                ('house_start', models.IntegerField(blank=True, null=True)),
                ('house_end', models.IntegerField(blank=True, null=True)),
                ('food_start', models.IntegerField(blank=True, null=True)),
                ('food_end', models.IntegerField(blank=True, null=True)),
                ('house_method', models.CharField(blank=True, max_length=100, null=True)),
                ('food_method', models.CharField(blank=True, max_length=100, null=True)),
                ('recycle_method', models.CharField(blank=True, max_length=100, null=True)),
                ('house_day', models.CharField(blank=True, max_length=45, null=True)),
                ('food_day', models.CharField(blank=True, max_length=45, null=True)),
                ('recycle_day', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'location_waste_information',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='location_idx',
            field=models.ForeignKey(blank=True, db_column='location_idx', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='userApp.LocationWasteInformation'),
        ),
        migrations.DeleteModel(
            name='LocationInformation',
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-26 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='setting_details',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('pid', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=2000)),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settingsApi.settings')),
            ],
        ),
    ]
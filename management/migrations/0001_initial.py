# Generated by Django 3.0.8 on 2020-07-22 10:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('doa', models.DateField(default=django.utils.timezone.now)),
                ('address', models.TextField()),
            ],
        ),
    ]
# Generated by Django 3.0.8 on 2021-12-18 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supporters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('sms', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialsAids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('supporters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supporters.Supporters')),
            ],
        ),
    ]

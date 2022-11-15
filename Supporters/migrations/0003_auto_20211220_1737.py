# Generated by Django 3.0.8 on 2021-12-20 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supporters', '0002_auto_20211220_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialsaids',
            name='supporters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supporters.supporters'),
        ),
        migrations.AlterField(
            model_name='supporters',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]

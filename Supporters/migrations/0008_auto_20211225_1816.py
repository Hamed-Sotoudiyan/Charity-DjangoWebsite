# Generated by Django 3.0.8 on 2021-12-25 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supporters', '0007_auto_20211225_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialsaids',
            name='supporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supporters.supporters'),
        ),
    ]

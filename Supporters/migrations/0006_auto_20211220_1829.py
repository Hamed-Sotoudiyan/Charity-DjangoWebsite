# Generated by Django 3.0.8 on 2021-12-20 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supporters', '0005_auto_20211220_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financialsaids',
            old_name='supporters',
            new_name='supporter',
        ),
        migrations.AlterField(
            model_name='financialsaids',
            name='supporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supporters.supporters'),
        ),
    ]

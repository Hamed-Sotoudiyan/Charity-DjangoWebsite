# Generated by Django 3.0.8 on 2021-12-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NonCashAssistance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noncashassistances',
            name='action',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='response',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
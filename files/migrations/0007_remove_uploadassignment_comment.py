# Generated by Django 4.1.6 on 2023-03-02 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_uploadassignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadassignment',
            name='comment',
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_remove_coursematerials_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerials',
            name='file',
            field=models.FileField(upload_to='course_materials/'),
        ),
        migrations.AlterField(
            model_name='coursematerials',
            name='title',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]

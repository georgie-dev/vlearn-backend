# Generated by Django 4.1.6 on 2023-03-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_alter_coursematerials_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=225, unique=True)),
                ('due_date', models.DateTimeField()),
                ('file', models.FileField(upload_to='upload_assignments/')),
                ('comment', models.TextField(null=True)),
                ('lecturer', models.CharField(max_length=225)),
            ],
        ),
    ]

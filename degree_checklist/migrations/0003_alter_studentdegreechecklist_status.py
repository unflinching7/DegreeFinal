# Generated by Django 4.2.5 on 2023-10-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degree_checklist', '0002_alter_courseenrollment_enrollmentstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdegreechecklist',
            name='Status',
            field=models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('inactive', 'Inactive')], default='active', max_length=10),
        ),
    ]

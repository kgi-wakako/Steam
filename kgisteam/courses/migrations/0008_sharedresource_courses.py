# Generated by Django 2.2.5 on 2019-09-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_rename_resource_20190911_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedresource',
            name='courses',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]
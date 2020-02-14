# Generated by Django 2.2.4 on 2019-08-31 08:51

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import martor.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2019, validators=[django.core.validators.MinValueValidator(2019, message='No courses before 2019.')])),
                ('name', models.CharField(max_length=30)),
                ('school', models.CharField(choices=[('MS', 'Middle School'), ('HS', 'High School')], max_length=2)),
                ('nen', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], verbose_name='nen (year)')),
                ('kumi', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator(message='Middle School classes: A-E or High School classes: 1-8', regex='[A-E]|[1-8]')], verbose_name='kumi (class)')),
                ('description', models.TextField(blank=True, max_length=200)),
                ('image_source_url', models.CharField(blank=True, max_length=200)),
                ('image_path', models.ImageField(blank=True, upload_to='courses')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('IC', 'In Class'), ('LL', 'Language Learning'), ('FS', 'Further Study')], max_length=2)),
                ('link_URL', models.URLField(blank=True)),
                ('link_text', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=datetime.datetime.now, max_length=50, unique=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Syllabi',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', martor.models.MartorField(default='Your question here.', max_length=500)),
                ('answer', models.FloatField()),
                ('solution', martor.models.MartorField(default='Your solution here.', max_length=1000)),
                ('worksheet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Worksheet')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('quiz', models.CharField(blank=True, max_length=30)),
                ('topics', models.CharField(blank=True, max_length=60)),
                ('reading', models.CharField(blank=True, max_length=60)),
                ('homework', models.CharField(blank=True, max_length=60)),
                ('link0_URL', models.URLField(blank=True)),
                ('link0_text', models.CharField(blank=True, max_length=30)),
                ('link1_URL', models.URLField(blank=True)),
                ('link1_text', models.CharField(blank=True, max_length=30)),
                ('link2_URL', models.URLField(blank=True)),
                ('link2_text', models.CharField(blank=True, max_length=30)),
                ('link3_URL', models.URLField(blank=True)),
                ('link3_text', models.CharField(blank=True, max_length=30)),
                ('syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Resource')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            bases=('courses.resource',),
        ),
    ]

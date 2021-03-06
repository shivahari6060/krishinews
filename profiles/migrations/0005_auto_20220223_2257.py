# Generated by Django 3.2.9 on 2022-02-23 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='author_rating',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='editor_rating',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='major_field',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=200, null=True)),
                ('major_field', models.CharField(blank=True, max_length=200, null=True)),
                ('author_rating', models.FloatField(blank=True, null=True)),
                ('editor_rating', models.FloatField(blank=True, null=True)),
                ('author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]

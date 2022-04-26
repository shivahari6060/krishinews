# Generated by Django 3.2.9 on 2022-04-22 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0004_auto_20220223_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogsite.basemodel')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
            ],
            bases=('blogsite.basemodel',),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogsite.basemodel')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
            ],
            bases=('blogsite.basemodel',),
        ),
        migrations.CreateModel(
            name='Subsector',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blogsite.basemodel')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
            ],
            bases=('blogsite.basemodel',),
        ),
    ]
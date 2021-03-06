# Generated by Django 3.2.9 on 2022-04-22 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0005_basemodel_category_subcategory_subsector'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='catgory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogsite.category'),
        ),
        migrations.AddField(
            model_name='subsector',
            name='catgory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogsite.category'),
        ),
        migrations.AddField(
            model_name='subsector',
            name='subcatgory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogsite.subcategory'),
        ),
    ]

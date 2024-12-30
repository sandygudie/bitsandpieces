# Generated by Django 5.1.4 on 2024-12-23 07:57

import django_summernote.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=django_summernote.fields.SummernoteTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]

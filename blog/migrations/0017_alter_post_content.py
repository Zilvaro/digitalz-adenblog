# Generated by Django 3.2.14 on 2022-08-29 12:54

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_rename_slug_herocontent_hero_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True),
        ),
    ]

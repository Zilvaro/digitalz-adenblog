# Generated by Django 3.2.14 on 2022-08-27 04:07

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_herocontent_image_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True),
        ),
    ]

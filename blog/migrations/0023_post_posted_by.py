# Generated by Django 3.2.14 on 2022-09-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_rename_hero_slug_herocontent_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted_by',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.14 on 2022-08-28 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='herocontent',
            old_name='hero_slug',
            new_name='slug',
        ),
    ]

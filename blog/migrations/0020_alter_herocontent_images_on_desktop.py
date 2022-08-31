# Generated by Django 3.2.14 on 2022-08-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20220830_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herocontent',
            name='images_on_desktop',
            field=models.IntegerField(choices=[(12, 'Whole Page'), (8, '2/3 of Page'), (6, 'Half of Page'), (4, '1/3 of Page'), (3, '1/4 of Page')], default=6),
        ),
    ]

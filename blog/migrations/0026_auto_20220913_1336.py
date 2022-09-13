# Generated by Django 3.2.14 on 2022-09-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_rename_text_backround_herocontent_text_background'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='herocontent',
            options={'ordering': ['image_order']},
        ),
        migrations.AlterField(
            model_name='herocontent',
            name='image_height',
            field=models.IntegerField(choices=[(40, '400px'), (32, '320px'), (27, '270px'), (20, '220px'), (16, '160px'), (8, '88px'), (5, '50px')], default=27),
        ),
        migrations.AlterField(
            model_name='herocontent',
            name='image_place',
            field=models.IntegerField(choices=[(1, 'Image-as-background'), (2, 'Image-on-side'), (3, 'Image-on-top')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]

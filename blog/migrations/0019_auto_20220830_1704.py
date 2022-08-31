# Generated by Django 3.2.14 on 2022-08-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='herocontent',
            name='hero_card',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='herocontent',
            name='image_order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='herocontent',
            name='image_height',
            field=models.IntegerField(choices=[(32, '320px'), (27, '270px'), (16, '160px'), (8, '88px'), (5, '50px')], default=27),
        ),
        migrations.AlterField(
            model_name='herocontent',
            name='image_place',
            field=models.IntegerField(choices=[(1, 'Image-as-background'), (2, 'Image-on-side'), (3, 'Image-on-top')], default=2),
        ),
    ]
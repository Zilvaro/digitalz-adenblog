# Generated by Django 3.2.14 on 2022-08-23 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_contactus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactUs',
            new_name='ContactMessage',
        ),
    ]

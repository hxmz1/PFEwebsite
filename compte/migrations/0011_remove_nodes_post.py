# Generated by Django 4.2 on 2023-05-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0010_nodes_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodes',
            name='Post',
        ),
    ]

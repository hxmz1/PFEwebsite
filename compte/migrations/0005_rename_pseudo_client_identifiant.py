# Generated by Django 4.2 on 2023-04-20 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0004_remove_client_image_remove_superviseur_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='pseudo',
            new_name='identifiant',
        ),
    ]

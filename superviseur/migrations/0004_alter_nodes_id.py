# Generated by Django 4.2 on 2023-05-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superviseur', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

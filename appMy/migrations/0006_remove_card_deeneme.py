# Generated by Django 4.1.5 on 2023-03-22 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0005_alter_card_deeneme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='deeneme',
        ),
    ]

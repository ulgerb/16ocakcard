# Generated by Django 4.1.5 on 2023-03-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0006_remove_card_deeneme'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='brand',
            field=models.CharField(max_length=50, null=True, verbose_name='Marka'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-03-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_card_deeneme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='deeneme',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Deneme'),
        ),
    ]

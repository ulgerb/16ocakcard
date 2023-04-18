# Generated by Django 4.1.5 on 2023-03-27 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('text', models.TextField(max_length=2000, verbose_name='Yorum')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Tarih- Saat')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.card', verbose_name='Ürün')),
            ],
        ),
    ]
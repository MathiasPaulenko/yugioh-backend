# Generated by Django 4.0.4 on 2022-05-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_alter_historicalgeneralmonster_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmagictrapcard',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalskillcard',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='magictrapcard',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='skillcard',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Description'),
        ),
    ]

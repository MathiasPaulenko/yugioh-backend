# Generated by Django 4.0.4 on 2022-04-16 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_alter_historicalmagictrapcard_race_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmagictrapcard',
            name='archetype',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Archetype'),
        ),
        migrations.AddField(
            model_name='magictrapcard',
            name='archetype',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Archetype'),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0016_card_banned_historicalcard_banned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrarity',
            name='name',
            field=models.CharField(choices=[('1', 'Common'), ('2', 'Rare'), ('3', 'Super rare'), ('4', 'Ultra rare'), ('5', 'Ultimate rare'), ('6', 'Secret rare'), ('7', 'Prismatic secret rare'), ('8', 'Ghost rare'), ('9', 'Parallel rarity'), ('10', 'Duel terminal'), ('11', 'Gold rare'), ('12', 'Premium gold rare'), ('13', 'Extra Secret Rare'), ('14', 'N/A'), ('15', 'Other'), ('16', 'Gold secret rare')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rarity',
            name='name',
            field=models.CharField(choices=[('1', 'Common'), ('2', 'Rare'), ('3', 'Super rare'), ('4', 'Ultra rare'), ('5', 'Ultimate rare'), ('6', 'Secret rare'), ('7', 'Prismatic secret rare'), ('8', 'Ghost rare'), ('9', 'Parallel rarity'), ('10', 'Duel terminal'), ('11', 'Gold rare'), ('12', 'Premium gold rare'), ('13', 'Extra Secret Rare'), ('14', 'N/A'), ('15', 'Other'), ('16', 'Gold secret rare')], max_length=50),
        ),
    ]

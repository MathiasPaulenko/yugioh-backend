# Generated by Django 4.0.4 on 2022-05-02 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_alter_card_rarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='subtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtype', to='card.subtype'),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='card.type'),
        ),
    ]

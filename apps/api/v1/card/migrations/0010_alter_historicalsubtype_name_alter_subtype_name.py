# Generated by Django 4.0.4 on 2022-05-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_alter_historicalmagictrapcard_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubtype',
            name='name',
            field=models.CharField(choices=[('1', 'Effect Monster'), ('2', 'Flip Effect Monster'), ('3', 'Flip Tuner Effect Monster'), ('4', 'Gemini Monster'), ('5', 'Normal Monster'), ('6', 'Normal Tuner Monster'), ('7', 'Pendulum Effect Monster'), ('8', 'Pendulum Flip Effect Monster'), ('9', 'Pendulum Normal Monster'), ('10', 'Pendulum Tuner Effect Monster'), ('11', 'Ritual Effect Monster'), ('12', 'Ritual Monster'), ('13', 'Skill Card'), ('14', 'Spell Card'), ('15', 'Spirit Monster'), ('16', 'Toon Monster'), ('17', 'Trap Card'), ('18', 'Tuner Monster'), ('19', 'Union Effect Monster'), ('20', 'Fusion Monster'), ('21', 'Link Monster'), ('22', 'Pendulum Effect Fusion Monster'), ('23', 'Synchro Monster'), ('24', 'Synchro Pendulum Effect Monster'), ('25', 'Synchro Tuner Monster'), ('26', 'XYZ Monster'), ('27', 'XYZ Pendulum Effect Monster'), ('28', 'Token')], max_length=50),
        ),
        migrations.AlterField(
            model_name='subtype',
            name='name',
            field=models.CharField(choices=[('1', 'Effect Monster'), ('2', 'Flip Effect Monster'), ('3', 'Flip Tuner Effect Monster'), ('4', 'Gemini Monster'), ('5', 'Normal Monster'), ('6', 'Normal Tuner Monster'), ('7', 'Pendulum Effect Monster'), ('8', 'Pendulum Flip Effect Monster'), ('9', 'Pendulum Normal Monster'), ('10', 'Pendulum Tuner Effect Monster'), ('11', 'Ritual Effect Monster'), ('12', 'Ritual Monster'), ('13', 'Skill Card'), ('14', 'Spell Card'), ('15', 'Spirit Monster'), ('16', 'Toon Monster'), ('17', 'Trap Card'), ('18', 'Tuner Monster'), ('19', 'Union Effect Monster'), ('20', 'Fusion Monster'), ('21', 'Link Monster'), ('22', 'Pendulum Effect Fusion Monster'), ('23', 'Synchro Monster'), ('24', 'Synchro Pendulum Effect Monster'), ('25', 'Synchro Tuner Monster'), ('26', 'XYZ Monster'), ('27', 'XYZ Pendulum Effect Monster'), ('28', 'Token')], max_length=50),
        ),
    ]
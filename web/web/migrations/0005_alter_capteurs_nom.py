# Generated by Django 5.0.6 on 2024-06-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_capteurs_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capteurs',
            name='Nom',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

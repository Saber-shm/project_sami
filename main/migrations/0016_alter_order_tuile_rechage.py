# Generated by Django 4.2.4 on 2023-08-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_nombre_ppv_toiture3_order_nombre_ppv_toiture_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tuile_rechage',
            field=models.CharField(blank=True, choices=[('oui', 'Oui'), ('non', 'Non')], max_length=120, null=True),
        ),
    ]

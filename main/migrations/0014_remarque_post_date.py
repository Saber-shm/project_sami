# Generated by Django 4.2.4 on 2023-08-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_remarque_order_remarque_1_remarque'),
    ]

    operations = [
        migrations.AddField(
            model_name='remarque',
            name='post_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]

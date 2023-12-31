# Generated by Django 4.2.4 on 2023-08-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=120)),
                ('adresse', models.CharField(max_length=300)),
                ('cp', models.CharField(max_length=200)),
                ('localite', models.CharField(max_length=200)),
                ('ngsm', models.CharField(max_length=200)),
                ('ntel', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('nom_de_societe', models.CharField(max_length=200)),
                ('forme_juridique', models.CharField(max_length=200)),
                ('date_de_visite', models.DateField()),
                ('date_de_signature', models.DateField()),
                ('ean54145', models.CharField(max_length=200)),
                ('ncompte', models.CharField(max_length=200)),
                ('bic', models.CharField(max_length=200)),
                ('grd', models.CharField(max_length=200)),
                ('ncompteur', models.CharField(max_length=200)),
                ('ntva', models.CharField(max_length=200)),
                ('adress_de_facturation_adress', models.CharField(max_length=200)),
                ('adress_de_facturation_cp', models.CharField(max_length=200)),
                ('adress_de_facturation_localite', models.CharField(max_length=200)),
                ('adress_de_livraison_adress', models.CharField(max_length=200)),
                ('adress_de_livraison_cp', models.CharField(max_length=200)),
                ('adress_de_livraison_localite', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures')),
            ],
        ),
    ]

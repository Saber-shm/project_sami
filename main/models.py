from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    
    nom = models.CharField(max_length=120,blank = True,null = True)
    prenom = models.CharField(max_length=120,blank = True,null = True)
    adresse = models.CharField(max_length=300,blank = True,null = True)
    cp = models.CharField(max_length=200,blank = True,null = True)
    localite = models.CharField(max_length=200,blank = True,null = True) 
    ngsm = models.CharField(max_length=200,blank = True,null = True)
    ntel = models.CharField(max_length=200,blank = True,null = True)
    email = models.EmailField(blank = True,null = True)
    nom_de_societe = models.CharField(max_length=200,blank = True,null = True)
    forme_juridique = models.CharField(max_length= 200,blank = True,null = True)
    date_de_visite = models.DateField(blank = True,null = True)
    date_de_signature = models.DateField(blank = True,null = True)
    ean54145 = models.CharField(max_length=200,blank = True,null = True)
    ncompte = models.CharField(max_length=200,blank = True,null = True)
    bic = models.CharField(max_length=200,blank = True,null = True)
    grd = models.CharField(max_length=200,blank = True,null = True)
    ncompteur = models.CharField(max_length=200,blank = True,null = True)
    ntva = models.CharField(max_length=200,blank = True,null = True)
    adress_de_facturation_adress = models.CharField(max_length=200,blank = True,null = True)
    adress_de_facturation_cp = models.CharField(max_length=200,blank = True,null = True)
    adress_de_facturation_localite = models.CharField(max_length=200,blank = True,null = True)
    adress_de_livraison_adress = models.CharField(max_length=200,blank = True,null = True)
    adress_de_livraison_cp = models.CharField(max_length=200,blank = True,null = True)
    adress_de_livraison_localite = models.CharField(max_length=200,blank = True,null = True)
    remarque_1 = models.TextField(blank = True,null = True)



    nombre_ppv = models.FloatField(blank = True, null = True) 
    type_ppv = models.CharField(max_length=120,blank = True, null = True)
    nombre_de_range_ppv = models.FloatField(blank = True, null = True) 
    nombre_pan_de_toiture = models.FloatField(blank = True, null = True)
    nombre_ppv_toiture_1 = models.FloatField(blank=True,null=True)
    toiture = models.CharField(max_length=120,blank = True, null = True)
    toiture_3 = models.CharField(max_length=120,blank = True, null = True)

    sous_toiture = models.CharField(max_length=120, blank = True, null = True)
    type_de_corniche = models.CharField(max_length=120, blank = True, null = True)
    tuile_rechage = models.CharField(max_length=120,choices=[("oui","Oui"),("non","Non")], blank = True, null = True)
    nombre_ppv_toiture_2 = models.FloatField(max_length=120,blank = True, null = True)
    orientation = models.CharField(max_length=120, blank = True, null = True,choices=[
    ('N', 'Nord'),
    ('NE', 'Nord-Est'),
    ('E', 'Est'),
    ('SE', 'Sud-Est'),
    ('S', 'Sud'),
    ('SW', 'Sud-Ouest'),
    ('W', 'Ouest'),
    ('NW', 'Nord-Ouest'),
])
    hauteur_sous_corniche = models.FloatField(max_length=120,blank = True, null = True)
    si_de7m_nacelle = models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    etat_du_toit = models.CharField(max_length=120,blank=True,null = True)
    les_panneaux_doivent_etre_installes =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    acces_par_arriere_pour_passé =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    si_pas_dacces_decrire_la_situation= models.CharField(max_length=120,blank = True, null = True)
    acces_libre_le_jour_du_chantier = models.CharField(max_length=200,blank=True,null=True)
    nombre_ppv_toiture_3 = models.FloatField(blank=True,null=True)

    type_de_compteur = models.CharField(max_length=120,blank=True,null=True)
    onduleur_1 = models.CharField(max_length=200,blank=True,null=True)
    onduleur_2 = models.CharField(max_length=200,blank=True,null=True)
    onduleur_3 = models.CharField(max_length=200,blank=True,null=True)

    Nombre_doptimiseur = models.FloatField(blank=True,null=True)
    enphase = models.CharField(max_length=200,blank=True,null=True)
    gaine_technique_present =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    espace_pres_du_coffret_pour_onduleur_meme_piece =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    etat_de_linstallation = models.CharField(max_length=200,blank=True,null=True)
    prise_de_terre_controle_5_derniere_annes =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    pressence_differentiel_general =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    passage_de_cable_nbre_piece_a_traverser = models.CharField(max_length=120,blank=True,null=True)
    coffret_20_cm_disponible = models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    tranche =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    nombre_de_metre_de_tranche = models.FloatField(blank=True,null=True)
    le_client_se_charge_de_gaine =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    nombre_de_metres_entre_onduleur_et_panneaux = models.FloatField(blank=True,null=True)

    le_client_souheite_il_le_monitoring =  models.CharField(max_length=120,blank = True, null = True, choices=[("non","Non"),("oui",'Oui')])
    le_modem_est_il_dans_la_meme_piece_que_londuleur = models.CharField(max_length=200,blank=True,null=True)
    nombres_de_metres_du_modem_a_lonuduleur = models.FloatField(blank=True,null=True)

    le_projet_sera_finance_par = models.CharField(max_length=200,blank=True,null=True)
    condition_de_paiement = models.CharField(max_length=300,blank=True,null=True)

    date_de_la_vt = models.CharField(max_length=300,blank=True,null=True)
    vt_effectue_par= models.CharField(max_length=300,blank=True,null=True)
    commentaire_technicien =  models.CharField(max_length=300,blank=True,null=True)
    statut_vt =  models.CharField(max_length=300,blank=True,null=True)
    coffret_general_conforme =  models.CharField(max_length=300,blank=True,null=True)
    type_de_cable = models.CharField(max_length=300,blank=True,null=True)
    ajout_coffret_supp =  models.CharField(max_length=300,blank=True,null=True)
    type_de_compteur=   models.CharField(max_length=300,blank=True,null=True)
    differenciel_general =  models.CharField(max_length=300,blank=True,null=True)
    prevoir_un_differentiel_general =  models.CharField(max_length=300,blank=True,null=True)
    limiteur =  models.CharField(max_length=300,blank=True,null=True)
    prevoir_un_limiteur =  models.CharField(max_length=300,blank=True,null=True)
    test_de_la_terre =  models.CharField(max_length=300,blank=True,null=True)
    nbr_de_metre_de_cable_a_prevoir =  models.CharField(max_length=300,blank=True,null=True)
    monitoring =  models.CharField(max_length=300,blank=True,null=True)
    modem_est_dans_la_meme_piece_que_londuleur =  models.CharField(max_length=300,blank=True,null=True)
    analyse_modem =  models.CharField(max_length=300,blank=True,null=True)


    type_de_toitur_prevu =  models.CharField(max_length=300,blank=True,null=True)
    type_toiture_prevu_a_la_vt =  models.CharField(max_length=300,blank=True,null=True)
    nbr_de_ppv =  models.CharField(max_length=300,blank=True,null=True)
    nbr_de_ppv_a_la_vt =  models.CharField(max_length=300,blank=True,null=True)
    ppv_en_portait =  models.CharField(max_length=300,blank=True,null=True)
    ppv_en_paysage =  models.CharField(max_length=300,blank=True,null=True)
    ppv_en_toiture_plate =  models.CharField(max_length=300,blank=True,null=True)
    ppv_en_chevalet_jardin =  models.CharField(max_length=300,blank=True,null=True)
    ppv_en_structure_jardin =  models.CharField(max_length=300,blank=True,null=True)
    sous_toiture_2 =  models.CharField(max_length=300,blank=True,null=True)
    le_client_a_des_ardoise_tuiles_de_rechange =  models.CharField(max_length=300,blank=True,null=True)
    nbr_dardoises_tuiles_rechange =  models.CharField(max_length=300,blank=True,null=True)

    remarque_du_chantier = models.TextField(blank= True,null = True)




    posted_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    post_date = models.DateField(auto_now=True,null = True,blank = True)
    def __str__(self):
        return str(self.nom) + " " + str(self.prenom)


class SAV(models.Model):
    posted_by = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    Nom_et_prenom_du_client = models.CharField(max_length=200)
    date_de_l_intallation  = models.DateField() 
    equipe_qui_installe_toiture = models.TextField()
    Raccordement_electiricien = models.CharField(max_length=200)
    nom_sou_traitant = models.CharField(max_length=200)
    description_de_la_panne = models.TextField(max_length=200)
    heure_darrive = models.CharField(max_length=120)
    heure_de_depart = models.CharField(max_length=120)
    temps_intervention = models.CharField(max_length=120)
    materiel_utilise = models.TextField()
    remarque = models.TextField(blank = True, null = True)
    ordre = models.OneToOneField(Order,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Nom_et_prenom_du_client)



class Remarque(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank = True,null = True)
    text = models.TextField()
    ordre =models.ForeignKey(Order, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now=True,null = True,blank = True)

    def ___str__(self):
        return str(self.ordre)


class Image(models.Model):
    pic = models.ImageField(upload_to="ordre_image/")
    ordre = models.ForeignKey(Order,on_delete=models.CASCADE)
    post_date = models.DateField(auto_now=True,null = True, blank = True)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE, null = True,blank = True)
    post_date = models.DateField(auto_now=True,null = True,blank = True)

    def __str__(self):
        return str(self.ordre)

class Administrateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=120) 
    prenom = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    picture = models.ImageField(upload_to='profile_pictures', blank = True, null = True)
    password = models.CharField(max_length=200,blank = True,null = True)
    def __str__(self):
        return str(self.nom) + " " + str(self.prenom)


class Comercial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=120) 
    prenom = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    picture = models.ImageField(upload_to='profile_pictures', blank = True, null = True)
    password = models.CharField(max_length=200,blank = True,null = True)
    def __str__(self):
        return str(self.nom) + " " + str(self.prenom)


class Tech(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=120) 
    prenom = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    picture = models.ImageField(upload_to='profile_pictures', blank = True, null = True)
    password = models.CharField(max_length=200,blank = True,null = True)
    def __str__(self):
        return str(self.nom) + " " + str(self.prenom)


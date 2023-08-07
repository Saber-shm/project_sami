from django import forms
from main.models import *
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class add_sav_form(forms.ModelForm):
    class Meta:
        model = SAV
        fields = "__all__"
        exclude = ["posted_by","ordre"]
        widgets = {
            'Nom_et_prenom_du_client': forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_l_intallation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'equipe_qui_installe_toiture': forms.Textarea(attrs={'class': 'form-control'}),
            'Raccordement_electiricien': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_sou_traitant': forms.TextInput(attrs={'class': 'form-control'}),
            'description_de_la_panne': forms.Textarea(attrs={'class': 'form-control'}),
            'heure_darrive': forms.TextInput(attrs={'class': 'form-control'}),
            'heure_de_depart': forms.TextInput(attrs={'class': 'form-control'}),
            'temps_intervention': forms.TextInput(attrs={'class': 'form-control'}),
            'materiel_utilise': forms.Textarea(attrs={'class': 'form-control'}),
            'remarque': forms.Textarea(attrs={'class': 'form-control'}),
        }
    def save(self,commit = True,posted_by = None,ordre = None):
        instance = super().save(commit = False)
        instance.posted_by = posted_by
        instance.ordre = ordre
        if commit:
            instance.save()
        return instance
class add_remarque_form(forms.ModelForm):
    class Meta:
        model = Remarque
        fields = "__all__"
        exclude = ["posted_by", "ordre"]
        widgets = {
            "text": forms.Textarea(attrs= {"class":"form-control"})
        }

    def save(self,commit = True,posted_by = None,ordre = None):
        instance = super().save(commit = False)
        instance.posted_by = posted_by
        instance.ordre = ordre
        if commit:
            instance.save()
        return instance
class add_ordre_form(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["posted_by"]
        widgets = {
                'date_de_visite': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'date_de_signature': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                'sous_toiture': forms.Select(attrs={'class': 'form-control'}, choices=[("oui", "Oui"), ("non", "Non")]),
                'orientation': forms.Select(attrs={'class': 'form-control'}, choices=[
                    ('N', 'Nord'),
                    ('NE', 'Nord-Est'),
                    ('E', 'Est'),
                    ('SE', 'Sud-Est'),
                    ('S', 'Sud'),
                    ('SW', 'Sud-Ouest'),
                    ('W', 'Ouest'),
                    ('NW', 'Nord-Ouest'),
                ]),
                'si_de7m_nacelle': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'les_panneaux_doivent_etre_installes': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'acces_par_arriere_pour_passé': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'gaine_technique_present': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'espace_pres_du_coffret_pour_onduleur_meme_piece': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'prise_de_terre_controle_5_derniere_annes': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'pressence_differentiel_general': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'coffret_20_cm_disponible': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'tranche': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'le_client_se_charge_de_gaine': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'le_client_souheite_il_le_monitoring': forms.Select(attrs={'class': 'form-control'}, choices=[("non", "Non"), ("oui", "Oui")]),
                'nom': forms.TextInput(attrs={'class': 'form-control'}),
                'prenom': forms.TextInput(attrs={'class': 'form-control'}),
                'adresse': forms.TextInput(attrs={'class': 'form-control'}),
                "remarque_1": forms.Textarea(attrs = {"class": "form-control"}),
                "nombre_ppv_toiture_1":forms.TextInput(attrs={'class': 'form-control'}),
                "toiture_3":forms.TextInput(attrs={'class': 'form-control'}),
                "tuile_rechage" : forms.TextInput(attrs={'class': 'form-control'}),
                "nombre_ppv_toiture_2": forms.TextInput(attrs={'class': 'form-control'}),
                "si_pas_dacces_decrire_la_situation" : forms.TextInput(attrs={'class': 'form-control'}),
                "nombre_ppv_toiture_3" : forms.TextInput(attrs={'class': 'form-control'}),
                "onduleur_1": forms.TextInput(attrs={'class': 'form-control'}),
                "onduleur_2": forms.TextInput(attrs={'class': 'form-control'}),
                "onduleur_3": forms.TextInput(attrs={'class': 'form-control'}),
                "type_de_cable":forms.TextInput(attrs={'class': 'form-control'}),
                "sous_toiture_2": forms.TextInput(attrs={'class': 'form-control'}),
                'cp': forms.TextInput(attrs={'class': 'form-control'}),
                'localite': forms.TextInput(attrs={'class': 'form-control'}),
                'ngsm': forms.TextInput(attrs={'class': 'form-control'}),
                'ntel': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'nom_de_societe': forms.TextInput(attrs={'class': 'form-control'}),
                'forme_juridique': forms.TextInput(attrs={'class': 'form-control'}),
                'ean54145': forms.TextInput(attrs={'class': 'form-control'}),
                'ncompte': forms.TextInput(attrs={'class': 'form-control'}),
                'bic': forms.TextInput(attrs={'class': 'form-control'}),
                'grd': forms.TextInput(attrs={'class': 'form-control'}),
                'ncompteur': forms.TextInput(attrs={'class': 'form-control'}),
                'ntva': forms.TextInput(attrs={'class': 'form-control'}),
                'adress_de_facturation_adress': forms.TextInput(attrs={'class': 'form-control'}),
                'adress_de_facturation_cp': forms.TextInput(attrs={'class': 'form-control'}),
                'adress_de_facturation_localite': forms.TextInput(attrs={'class': 'form-control'}),
                'adress_de_livraison_adress': forms.TextInput(attrs={'class': 'form-control'}),
                'adress_de_livraison_cp': forms.TextInput(attrs={'class': 'form-control'}),
                'adress_de_livraison_localite': forms.TextInput(attrs={'class': 'form-control'}),
                'remarque': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                'nombre_ppv': forms.NumberInput(attrs={'class': 'form-control'}),
                'type_ppv': forms.TextInput(attrs={'class': 'form-control'}),
                'nombre_de_range_ppv': forms.NumberInput(attrs={'class': 'form-control'}),
                'nombre_pan_de_toiture': forms.NumberInput(attrs={'class': 'form-control'}),
                'nombre_ppv_toiture': forms.NumberInput(attrs={'class': 'form-control'}),
                'toiture': forms.TextInput(attrs={'class': 'form-control'}),
                'type_de_corniche': forms.TextInput(attrs={'class': 'form-control'}),
                'hauteur_sous_corniche': forms.NumberInput(attrs={'class': 'form-control'}),
                'etat_du_toit': forms.TextInput(attrs={'class': 'form-control'}),
                'acces_libre_le_jour_du_chantier': forms.TextInput(attrs={'class': 'form-control'}),
                'nombre_ppv_toiture3': forms.NumberInput(attrs={'class': 'form-control'}),
                'type_de_compteur': forms.TextInput(attrs={'class': 'form-control'}),
                'onduleurs': forms.TextInput(attrs={'class': 'form-control'}),
                'Nombre_doptimiseur': forms.NumberInput(attrs={'class': 'form-control'}),
                'enphase': forms.TextInput(attrs={'class': 'form-control'}),
                'etat_de_linstallation': forms.TextInput(attrs={'class': 'form-control'}),
                'passage_de_cable_nbre_piece_a_traverser': forms.TextInput(attrs={'class': 'form-control'}),
                'nombre_de_metre_de_tranche': forms.NumberInput(attrs={'class': 'form-control'}),
                'nombre_de_metres_entre_onduleur_et_panneaux': forms.NumberInput(attrs={'class': 'form-control'}),
                'le_modem_est_il_dans_la_meme_piece_que_londuleur': forms.TextInput(attrs={'class': 'form-control'}),
                'nombres_de_metres_du_modem_a_lonuduleur': forms.NumberInput(attrs={'class': 'form-control'}),
                'le_projet_sera_finance_par': forms.TextInput(attrs={'class': 'form-control'}),
                'condition_de_paiement': forms.TextInput(attrs={'class': 'form-control'}),
                'date_de_la_vt': forms.TextInput(attrs={'class': 'form-control'}),
                'vt_effectue_par': forms.TextInput(attrs={'class': 'form-control'}),
                'commentaire_technicien': forms.TextInput(attrs={'class': 'form-control'}),
                'statut_vt': forms.TextInput(attrs={'class': 'form-control'}),
                'coffret_general_conforme': forms.TextInput(attrs={'class': 'form-control'}),
                'ajout_coffret_supp': forms.TextInput(attrs={'class': 'form-control'}),
                'differenciel_general': forms.TextInput(attrs={'class': 'form-control'}),
                'prevoir_un_differentiel_general': forms.TextInput(attrs={'class': 'form-control'}),
                'limiteur': forms.TextInput(attrs={'class': 'form-control'}),
                'prevoir_un_limiteur': forms.TextInput(attrs={'class': 'form-control'}),
                'test_de_la_terre': forms.TextInput(attrs={'class': 'form-control'}),
                'nbr_de_metre_de_cable_a_prevoir': forms.TextInput(attrs={'class': 'form-control'}),
                'monitoring': forms.TextInput(attrs={'class': 'form-control'}),
                'modem_est_dans_la_meme_piece_que_londuleur': forms.TextInput(attrs={'class': 'form-control'}),
                'analyse_modem': forms.TextInput(attrs={'class': 'form-control'}),
                'type_de_toitur_prevu': forms.TextInput(attrs={'class': 'form-control'}),
                'type_toiture_prevu_a_la_vt': forms.TextInput(attrs={'class': 'form-control'}),
                'nbr_de_ppv': forms.TextInput(attrs={'class': 'form-control'}),
                'nbr_de_ppv_a_la_vt': forms.TextInput(attrs={'class': 'form-control'}),
                'ppv_en_portait': forms.TextInput(attrs={'class': 'form-control'}),
                'ppv_en_paysage': forms.TextInput(attrs={'class': 'form-control'}),
                'ppv_en_toiture_plate': forms.TextInput(attrs={'class': 'form-control'}),
                'ppv_en_chevalet_jardin': forms.TextInput(attrs={'class': 'form-control'}),
                'ppv_en_structure_jardin': forms.TextInput(attrs={'class': 'form-control'}),
                'le_client_a_des_ardoise_tuiles_de_rechange': forms.TextInput(attrs={'class': 'form-control'}),
                'nbr_dardoises_tuiles_rechange': forms.TextInput(attrs={'class': 'form-control'}),
                'remarque_du_chantier': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            }
    def save(self,commit = True,posted_by = None):
        instance = super().save(commit = False)
        instance.posted_by = posted_by
        if commit:
            instance.save()
        return instance

class add_image_form(forms.ModelForm):

    class Meta:
        model = Image
        fields = "__all__"
        exclude = ["ordre","posted_by"]

    def save(self,commit = True,ordre = None,posted_by = None):
        instance = super().save(commit = False)
        instance.ordre = ordre
        instance.posted_by = posted_by
        if commit:
            instance.save()
        return instance 
        
class edit_profile_form(forms.ModelForm):
    class Meta:
        model = Administrateur
        fields = "__all__"
        exclude = ["user"]

    def save(self,commit = True,user = None):
        instance = super().save(commit = False)
        instance.user = user
        if commit:
            instance.save()
        return instance 
    
class add_comercial_form(forms.ModelForm):
    class Meta:
        model = Comercial
        fields = "__all__"
        exclude = ["email","user","password"]

    def save(self,commit = True, user = None,email = None,password = None):
        instance = super().save(commit = False) 
        instance.user = user
        instance.email = email
        instance.password = password
        if commit:
            instance.save()
        return instance
class add_tech_form(forms.ModelForm):
    class Meta:
        model = Tech
        fields = "__all__"
        exclude = ["email","user","password"]

    def save(self,commit = True, user = None,email = None,password = None):
        instance = super().save(commit = False) 
        instance.user = user
        instance.email = email
        instance.password = password
        if commit:
            instance.save()
        return instance
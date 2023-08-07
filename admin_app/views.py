from django.shortcuts import render
from django.http import FileResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import *
from .forms import *
from django.template import Context
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet

from django.template.loader import get_template




from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def create_order_info_pdf(order_data,buf):
    # Create a PDF document
    c = canvas.Canvas(buf, pagesize=letter)

    # Define colors
    light_grey = colors.lightgrey

    # Set font styles
    title_font = "Helvetica-Bold"
    normal_font = "Helvetica"

    # Draw "Fiche project" on the left
    c.setFont(title_font, 18)
    c.drawString(100, 750, "Fiche project:")

    # Draw line
    c.setLineWidth(1)
    c.line(100, 747, 250, 747)

    # Draw Date and Vendeur (Seller) information
    c.setFont(normal_font, 12)
    c.drawString(300, 750, f"Date: {order_data.get('date_de_visite', '')}")
    c.drawString(300, 735, f"Vendeur: {order_data.get('posted_by', '')}")

    # Draw "Information client" title
    c.setFont(title_font, 16)
    c.drawString(210, 690, "Information client:")
    c.rect(45, 340, 500, 300)  # Increased height to fit all fields
    c.rect(45, 210, 500, 115)  # Increased height to fit all fields


    # Draw rectangle borders for client data
    c.setStrokeColor(light_grey)
    c.setLineWidth(1)

    # Draw client data within the rectangle
    c.setFont(normal_font, 12)


    c.drawString(50, 610, f"Name:")
    c.setFillColor("blue")
    c.drawString(180,610, f"{order_data.get('nom', '')}")
    c.setFillColor("black")

    c.drawString(50, 590, f"Address:")
    c.setFillColor("blue")
    c.drawString(180,590, f"{order_data.get('adresse', '')}")
    c.setFillColor("black")
    c.drawString(50, 570, f"CP:")
    c.setFillColor("blue")
    c.drawString(180,570,f"{order_data.get('cp', '')}")
    c.setFillColor("black")

    c.drawString(50, 550, f"Localite:")
    c.setFillColor("blue")
    c.drawString(180,550, f"{order_data.get('localite', '')}")
    c.setFillColor("black")
    c.drawString(50, 530, f"NGSM:")
    c.setFillColor("blue")
    c.drawString(180,530, f"{order_data.get('ngsm', '')}")
    c.setFillColor("black")

    c.drawString(50, 510, f"NTel:")
    c.setFillColor("blue")
    c.drawString(180,510,f"{order_data.get('ntel', '')}")
    c.setFillColor("black")

    c.drawString(50, 490, f"Email:")
    c.setFillColor("blue")
    c.drawString(180, 490,f"{order_data.get('email', '')}")
    c.setFillColor("black")


    c.drawString(300, 610, f"Nom de Societe:")
    c.setFillColor("blue")
    c.drawString(430, 610,f"{order_data.get('nom_de_societe', '')}")
    c.setFillColor("black")
    
    c.drawString(300, 590, f"Forme Juridique:")
    c.setFillColor("blue")
    c.drawString(430, 590,f"{order_data.get('forme_juridique', '')}")
    c.setFillColor("black")
    
    c.drawString(300, 570, f"Date de Visite:")

    c.setFillColor("blue")
    c.drawString(430, 570,f"{order_data.get('date_de_visite', '')}")
    c.setFillColor("black")
    
    c.drawString(300, 550, f"Date de Signature:")
    c.setFillColor("blue")
    c.drawString(430, 550,f"{order_data.get('date_de_signature', '')}")
    c.setFillColor("black")
    c.drawString(300, 370, f"Nom de societe:")

    c.setFillColor("blue")
    c.drawString(430, 370,f"{order_data.get('nom_de_societe', '')}")
    c.setFillColor("black")

    c.drawString(300, 530, f"EAN54145:")
    c.setFillColor("blue")
    c.drawString(430, 530,f"{order_data.get('ean54145', '')}")
    c.setFillColor("black")
    c.drawString(300, 500, f"NCompte:")
    c.setFillColor("blue")
    c.drawString(430, 500,f"{order_data.get('ncompte', '')}")
    c.setFillColor("black")
    
    c.drawString(300, 470, f"BIC:")
    c.setFillColor("blue")
    c.drawString(430, 470,f"{order_data.get('bic', '')}")
    c.setFillColor("black")

    c.drawString(300, 450, f"GRD:")
    c.setFillColor("blue")
    c.drawString(430, 450,f"{order_data.get('nom_de_societe', '')}")
    c.setFillColor("black")
    c.drawString(300, 430, f"NCompteur:")
    c.setFillColor("blue")
    c.drawString(430, 430,f"{order_data.get('ncompteur', '')}")
    c.setFillColor("black")
    c.drawString(300, 400, f"NTVA:")
    c.setFillColor("blue")
    c.drawString(430, 400,f"{order_data.get('ntva', '')}")
    c.setFillColor("black")
    
    
    c.setFont(title_font, 16)

    c.drawString(70, 300, "Adresse de Facturation:")
    c.setFont(normal_font, 12)


    c.drawString(50, 270, f"Adresse:")
    c.setFillColor("blue")
    c.drawString(180, 270,f"{order_data.get('adress_de_facturation_adress', '')}")
    c.setFillColor("black")


    c.drawString(50, 250, f"CP :")
    c.setFillColor("blue")
    c.drawString(180, 250,f"{order_data.get('adress_de_facturation_cp', '')}")
    c.setFillColor("black")

    c.drawString(50, 230, f"Localite:")
    c.setFillColor("blue")
    c.drawString(180, 230,f"{order_data.get('adress_de_facturation_localite', '')}")
    c.setFillColor("black")
    c.drawString(300, 270, f"Adresse de Livraison:")
    c.setFillColor("blue")
    c.drawString(430, 270,f"{order_data.get('adress_de_facturation_localite', '')}")


    c.setFillColor("black")
    c.setFont(title_font, 16)

    c.drawString(300, 300, "Adresse de Livraison:")
    c.setFont(normal_font, 12)
    c.drawString(300, 250, f"CP:")
    c.setFillColor("blue")
    c.drawString(430, 250,f"{order_data.get('adress_de_livraison_cp', '')}")
    c.setFillColor("black")
    c.drawString(300, 230, f"Localite:")
    c.setFillColor("blue")
    c.drawString(430, 230,f"{order_data.get('adress_de_livraison_localite', '')}")
    c.setFillColor("black")
    c.drawString(210, 150, f"Remarque:                  {order_data.get('remarque', '')}")


    c.showPage()
    c.setFont(title_font, 16)
    c.rect(40, 80, 500, 560)  

    c.drawString(210, 690, "Information chantier:")
    c.setFont(normal_font, 12)


    c.drawString(50, 610, f"Nombre PPV:")
    c.setFillColor("blue")
    c.drawString(300,610, f"{order_data.get('nombre_ppv', '')}")
    c.setFillColor("black")

    c.drawString(50, 590, f"Type PPV:")
    c.setFillColor("blue")
    c.drawString(300,590, f"{order_data.get('type_pvv', '')}")
    c.setFillColor("black")
    c.drawString(50, 570, f"Type de range PPV:")
    c.setFillColor("blue")
    c.drawString(300,570,f"{order_data.get('type_de_range_ppv', '')}")
    c.setFillColor("black")

    c.drawString(50, 550, f"nombre_pan_de_toiture:")
    c.setFillColor("blue")
    c.drawString(300,550, f"{order_data.get('nombre_pan_de_toiture', '')}")
    c.setFillColor("black")
    c.drawString(50, 530, f"nombre_ppv_toiture_1:")
    c.setFillColor("blue")
    c.drawString(300,530, f"{order_data.get('nombre_ppv_toiture_1', '')}")
    c.setFillColor("black")

    c.drawString(50, 510, f"toiture 1:")
    c.setFillColor("blue")
    c.drawString(300,510,f"{order_data.get('toiture_1', '')}")
    c.setFillColor("black")

    c.drawString(50, 490, f"sous toiture:")
    c.setFillColor("blue")
    c.drawString(300, 490,f"{order_data.get('sous_toiture', '')}")
    c.setFillColor("black")


    c.drawString(50, 460, f"type de corniche:")
    c.setFillColor("blue")
    c.drawString(300, 460,f"{order_data.get('type_de_corniche', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 430, f"tuile rechange:")
    c.setFillColor("blue")
    c.drawString(300, 430,f"{order_data.get('tuile_rechange', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 400, f"nombre ppv toiture 2:")

    c.setFillColor("blue")
    c.drawString(300, 400,f"{order_data.get('nombre ppv toiture_2', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 370, f"orientation:")
    c.setFillColor("blue")
    c.drawString(300, 370,f"{order_data.get('orientation', '')}")
    c.setFillColor("black")
    c.drawString(50, 340, f"hauteur sous corniche:")


    c.setFillColor("blue")
    c.drawString(300, 340,f"{order_data.get('hauteur_sous_corniche', '')}")
    c.setFillColor("black")

    c.drawString(50, 310, f"si 7m nacelle:")
    c.setFillColor("blue")
    c.drawString(300, 310,f"{order_data.get('si_7m_nacelle', '')}")
    c.setFillColor("black")
    c.drawString(50, 280, f"etat du toit:")
    c.setFillColor("blue")
    c.drawString(300, 280,f"{order_data.get('etat_du_toit', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 250, f"les panneaux doivent etre installe:")
    c.setFillColor("blue")
    c.drawString(300, 250,f"{order_data.get('les_panneaux_doivent_etre_installe', '')}")
    c.setFillColor("black")

    c.drawString(50, 210, f"si a larriere yatil un acces:")
    c.setFillColor("blue")
    c.drawString(300, 210,f"{order_data.get('si_a_larriere_yatil_un_acces', '')}")
    c.setFillColor("black")
    c.drawString(50, 190, f"si non decrire la situation:")
    c.setFillColor("blue")
    c.drawString(300, 190,f"{order_data.get('si non decrir la situation', '')}")
    c.setFillColor("black")
    c.drawString(50, 160, f"acces libre le jour du chantier:")
    c.setFillColor("blue")
    c.drawString(300, 160,f"{order_data.get('acces_libre_le_jour_du_chantier', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 130, f"toiture 3:")
    c.setFillColor("blue")
    c.drawString(300, 130,f"{order_data.get('toiture_3', '')}")
    c.setFillColor("black")

    c.drawString(50, 100, f"nombre ppv toiture 3:")
    c.setFillColor("blue")
    c.drawString(300, 100,f"{order_data.get('nombre_ppv_toiture_3', '')}")
    c.setFillColor("black")



    c.showPage()
    c.setFont(title_font, 16)
    c.rect(40, 180, 500, 460)  

    c.drawString(170, 690, "Informations onduleurs et électricité:")
    c.setFont(normal_font, 12)


    c.drawString(50, 610, f"Type de compteur:")
    c.setFillColor("blue")
    c.drawString(300,610, f"{order_data.get('type_de_compteur', '')}")
    c.setFillColor("black")

    c.drawString(50, 590, f"Onduleur 1:")
    c.setFillColor("blue")
    c.drawString(300,590, f"{order_data.get('onduleur_1', '')}")
    c.setFillColor("black")
    c.drawString(50, 570, f"Onduleur 2:")
    c.setFillColor("blue")
    c.drawString(300,570,f"{order_data.get('onduleur_2', '')}")
    c.setFillColor("black")

    c.drawString(50, 550, f"Onduleur 3:")
    c.setFillColor("blue")
    c.drawString(300,550, f"{order_data.get('onduleur_3', '')}")
    c.setFillColor("black")
    c.drawString(50, 530, f"Nombre doptimiseur:")
    c.setFillColor("blue")
    c.drawString(300,530, f"{order_data.get('Nombre_doptimiseur', '')}")
    c.setFillColor("black")

    c.drawString(50, 510, f"Enphase :")
    c.setFillColor("blue")
    c.drawString(300,510,f"{order_data.get('Enphase', '')}")
    c.setFillColor("black")

    c.drawString(50, 490, f"Gaine technique present:")
    c.setFillColor("blue")
    c.drawString(300, 490,f"{order_data.get('gaine_technique_present', '')}")
    c.setFillColor("black")


    c.drawString(50, 460, f"Espace pres du coffret pour l'onduleur :")
    c.setFillColor("blue")
    c.drawString(300, 460,f"{order_data.get('Espace_pres_du_coffret_pour_londuleur_meme_piece', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 430, f"Etat de linstalation:")
    c.setFillColor("blue")
    c.drawString(300, 430,f"{order_data.get('etat_de_linstalation', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 400, f"prise de terre controlee ces 5 dernier annes:")

    c.setFillColor("blue")
    c.drawString(300, 400,f"{order_data.get('prise_de_terre_controlee_ces_5_dernier_annes', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 370, f"Presence differentiel general:")
    c.setFillColor("blue")
    c.drawString(300, 370,f"{order_data.get('presence_differentiel_general', '')}")
    c.setFillColor("black")
    c.drawString(50, 340, f"Coffret 20cm disponible:")


    c.setFillColor("blue")
    c.drawString(300, 340,f"{order_data.get('coffret_20cm_disponible', '')}")
    c.setFillColor("black")

    c.drawString(50, 310, f"Tranchee:")
    c.setFillColor("blue")
    c.drawString(300, 310,f"{order_data.get('tranchee', '')}")
    c.setFillColor("black")
    c.drawString(50, 280, f"Nombre de metres de tranche:")
    c.setFillColor("blue")
    c.drawString(300, 280,f"{order_data.get('nombre_de_metres_de_tranche', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 250, f"Le client se charge de gaine:")
    c.setFillColor("blue")
    c.drawString(300, 250,f"{order_data.get('le_client_se_charge_de_gaine', '')}")
    c.setFillColor("black")

    c.drawString(50, 210, f"Nombre de metre entre onduleur et panneaux:")
    c.setFillColor("blue")
    c.drawString(300, 210,f"{order_data.get('nombre_de_metre_entre_onduleur_et_panneaux', '')}")
    c.setFillColor("black")
    
    c.showPage()
    c.setFont(title_font, 16)
    c.rect(40, 610, 500, 70)  

    c.drawString(210, 690, "Informations Monitoring :")
    c.setFont(normal_font, 12)


    c.drawString(50, 660, f"Client monitoring:")
    c.setFillColor("blue")
    c.drawString(300,660, f"{order_data.get('client_monitoring', '')}")
    c.setFillColor("black")

    c.drawString(50, 640, f"Modem meme piece que l'onduleur:")
    c.setFillColor("blue")
    c.drawString(300,640, f"{order_data.get('modem_meme_piece_que_loduleur', '')}")
    c.setFillColor("black")
    c.drawString(50, 620, f"Nombre de metres modem onduleur:")
    c.setFillColor("blue")
    c.drawString(300,620,f"{order_data.get('nombre_de_metres_modem_onduleur', '')}")
    c.setFillColor("black")
    c.setFont(title_font, 16)

    c.drawString(210, 590, "Informations Finance :")

    c.rect(40, 500, 500, 80)  

    c.setFont(normal_font, 12)


    c.drawString(50, 560, f"Finance:")
    c.setFillColor("blue")
    c.drawString(300,560, f"{order_data.get('finance', '')}")
    c.setFillColor("black")

    c.drawString(50, 540, f"Condition de paiement:")
    c.setFillColor("blue")
    c.drawString(300,540, f"{order_data.get('condition_de_paiement', '')}")
    c.setFillColor("black")

    c.setFont(title_font, 16)
    c.rect(40, 45, 500, 400)  

    c.drawString(210, 460, "Visite technique Electricité:")
    c.setFont(normal_font, 12)
    

    c.drawString(50, 360, f"Date de la vt:")
    c.setFillColor("blue")
    c.drawString(300, 360,f"{order_data.get('date_de_la_vt', '')}")
    c.setFillColor("black")
    c.drawString(50, 340, f"vteffectue:")
    c.setFillColor("blue")
    c.drawString(300, 340,f"{order_data.get('vt_effectue_par', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 320, f"Commentaire technicien")
    c.setFillColor("blue")
    c.drawString(300, 320,f"{order_data.get('commentaire_technicien', '')}")
    c.setFillColor("black")

    c.drawString(50, 300, f"Statut vt:")
    c.setFillColor("blue")
    c.drawString(300, 300,f"{order_data.get('statut_vt', '')}")
    c.setFillColor("black")

    c.drawString(50, 280, f"Coffret general conforme:")
    c.setFillColor("blue")
    c.drawString(300, 280,f"{order_data.get('coffret_general_conforme', '')}")
    c.setFillColor("black")

    c.drawString(50, 260, f"Ajout coffret supp:")
    c.setFillColor("blue")
    c.drawString(300, 260,f"{order_data.get('ajout_coffret_supp', '')}")
    c.setFillColor("black")

    c.drawString(50, 240, f"Differencial general:")
    c.setFillColor("blue")
    c.drawString(300, 240,f"{order_data.get('differencial_general', '')}")
    c.setFillColor("black")

    c.drawString(50, 220, f"Statut vt:")
    c.setFillColor("blue")
    c.drawString(300, 220,f"{order_data.get('statut_vt', '')}")
    c.setFillColor("black")

    c.drawString(50, 200, f"Prevoir un differential general:")
    c.setFillColor("blue")
    c.drawString(300, 200,f"{order_data.get('prevoir_un_differential_general', '')}")
    c.setFillColor("black")

    c.drawString(50, 180, f"Limiteur:")
    c.setFillColor("blue")
    c.drawString(300, 180,f"{order_data.get('limiteur', '')}")
    c.setFillColor("black")

    c.drawString(50, 160, f"Prevoir un limiteur:")
    c.setFillColor("blue")
    c.drawString(300, 160,f"{order_data.get('prevoir_un_limiteur', '')}")
    c.setFillColor("black")

    c.drawString(50, 140, f"test_de_la_terre:")
    c.setFillColor("blue")
    c.drawString(300, 140,f"{order_data.get('test_de_la_terre', '')}")
    c.setFillColor("black")

    c.drawString(50, 120, f"nbr de metre de cable a prevoir:")
    c.setFillColor("blue")
    c.drawString(300, 120,f"{order_data.get('nbr_de_metre_de_cable_a_prevoir', '')}")
    c.setFillColor("black")

    c.drawString(50, 100, f"Type de cable:")
    c.setFillColor("blue")
    c.drawString(300, 100,f"{order_data.get('type_de_cable', '')}")
    c.setFillColor("black")

    c.drawString(50, 80, f"Tranche:")
    c.setFillColor("blue")
    c.drawString(300, 80,f"{order_data.get('tranche', '')}")
    c.setFillColor("black")

    c.drawString(50, 60, f"nbr de metre de tranchee:")
    c.setFillColor("blue")
    c.drawString(300, 60,f"{order_data.get('nbr_de_metre_de_tranchee', '')}")
    c.setFillColor("black")

    c.drawString(50, 380, f"Monitoring:")
    c.setFillColor("blue")
    c.drawString(300, 380,f"{order_data.get('monitoring', '')}")
    c.setFillColor("black")

    c.drawString(50, 400, f"Modem est dans la meme piece que londuleur:")
    c.setFillColor("blue")
    c.drawString(300, 400,f"{order_data.get('modem_est_dans_la_meme_piece_que_londuleur', '')}")
    c.setFillColor("black")

    c.drawString(50, 420, f"Analyse modem:")
    c.setFillColor("blue")
    c.drawString(300, 420,f"{order_data.get('analyse_modem', '')}")
    c.setFillColor("black")






    c.showPage()
    c.setFont(title_font, 16)
    c.rect(40, 340, 500, 400)  

    c.drawString(210, 690, "Visite technique Toiture:")
    c.setFont(normal_font, 12)


    c.drawString(50, 610, f"Type toiture prevu:")
    c.setFillColor("blue")
    c.drawString(300,610, f"{order_data.get('type_toiture_prevu', '')}")
    c.setFillColor("black")


    c.setFillColor("black")
    c.drawString(50, 570, f"Type toiture prevu a la vt:")
    c.setFillColor("blue")
    c.drawString(300,570,f"{order_data.get('type_toiture_prevu_a_la_vt', '')}")
    c.setFillColor("black")

    c.drawString(50, 550, f"Nbr de ppv:")
    c.setFillColor("blue")
    c.drawString(300,550, f"{order_data.get('nb_de_ppv_a_la_vt', '')}")
    c.setFillColor("black")
    c.drawString(50, 530, f"ppv en portrait:")
    c.setFillColor("blue")
    c.drawString(300,530, f"{order_data.get('ppv_en_portrait', '')}")
    c.setFillColor("black")

    c.drawString(50, 510, f"Ppv en chevalet jardin:")
    c.setFillColor("blue")
    c.drawString(300,510,f"{order_data.get('ppv_en_chevalet_jardin', '')}")
    c.setFillColor("black")

    c.drawString(50, 490, f"Ppv en structure jardin:")
    c.setFillColor("blue")
    c.drawString(300, 490,f"{order_data.get('ppv_en_structure_jardin', '')}")
    c.setFillColor("black")


    c.drawString(50, 460, f"Sous toiture:")
    c.setFillColor("blue")
    c.drawString(300, 460,f"{order_data.get('sous_toiture', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 430, f"Le client a des adroises:")
    c.setFillColor("blue")
    c.drawString(300, 430,f"{order_data.get('le_client_a_des_adroises', '')}")
    c.setFillColor("black")
    
    c.drawString(50, 400, f"Nbr dadroises:")

    c.setFillColor("blue")
    c.drawString(300, 400,f"{order_data.get('nbr_dadroises', '')}")
    c.setFillColor("black")


    return c
    
# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        data = Order.objects.all()

        data = reversed(data)
        if request.method == "POST":
            search_ = request.POST["search"]
            return redirect("search_result", search = search_)

        return render(request,"home.html",{"data":data})
    else:
        return redirect("login_user")

def search_result(request,search):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        search_query = Order.objects.filter(nom__contains = search)
        
        if request.method == "POST":
            search_ = request.POST["search"]
            return redirect("search_result", search = search_)
        return render(request,"home.html",{"result":search_query})

def details_view(request,ordre_id):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        sav = SAV.objects.filter(ordre = ordre_id)
        sav_bool = False
        ordre_data = Order.objects.get(pk = ordre_id)

        if len(list(sav)) > 0:
            sav_bool = True
        return render(request,'details_view.html',{"data":ordre_data,"sav": sav_bool})
    else:
        return redirect("login_user")
def delete_ordre(request, id_ordre):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        ordre_data = Order.objects.get(pk = id_ordre)
        ordre_data.delete()
        return redirect("home_page")
    else:
        return redirect("login_user")
def add_ordre(request):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        if request.method == "POST":
            form = add_ordre_form(request.POST)
            if form.is_valid():
                ordre = form.save(commit=False)
                ordre.posted_by = request.user
                ordre.save()
                return redirect("home_page")
        else:
            form = add_ordre_form

        return render(request,"add_ordre_form.html",{"form":form})
    else:
        return redirect("login_user")
def edit_ordre(request,ordre_id):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        ordre_data = Order.objects.get(pk = ordre_id)
        form = add_ordre_form(request.POST or None, instance=ordre_data)
        if form.is_valid():
            form.save()
            return redirect("details_view",ordre_id)
        return render(request,"edit_ordre.html",{"form": form})
    else:
        return redirect("login_user")
def add_image(request,ordre_id):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        ordre = Order.objects.get(pk = ordre_id)
        if request.method == "POST":
            form = add_image_form(request.POST,request.FILES)
            if form.is_valid():
                img = form.save(commit=False)
                img.ordre = ordre
                img.posted_by = request.user
                img.save()
                return redirect("details_view",ordre_id = ordre_id)

        else:
            form = add_image_form
        return render(request,"add_image.html",{"form":form})
    else:
        return redirect("login_user")
def images(request,ordre_id):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        ordre = Order.objects.get(pk = ordre_id)
        data = Image.objects.filter(ordre = ordre_id)
        return render(request,"imgs.html",{'data': data})
    else:
        return redirect("login_user")
def delete_pic(request,img_id):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        img = Image.objects.get(pk = img_id)
        ordre_id = img.ordre.id
        img.delete()
        return redirect("images",ordre_id = ordre_id)
    else:
        return redirect("login_user")


def profile_view(request):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        return render(request,"profile_a.html",{"data":admin_user_info, "status": "Admin"})
    else:
        return redirect("login_user")
def edit_profile(request,profile_id):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        form = edit_profile_form(request.POST or None, instance=admin_user_info)
        if form.is_valid():
            adm = form.save(commit = False)
            adm.user = request.user
            return redirect("profile_view")
        return render(request,"edit_profile.html",{"form": form})
    else:
        return redirect("login_user")
def create_accout(request,type):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                # Log the user in
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get('password1')
                print(raw_password)

                info = f"{username},{raw_password},{email}"
                if type == "comercial": # Redirect to the desired page
                    return redirect("create_commercial",info = info)
                elif type == "tech":
                    return redirect("create_tech", info = info)
        else:
            form = RegistrationForm()
        return render(request, 'create_acc_stp1.html', {'form': form})
    else:
        return redirect("login_user")
    
def create_commercial(request,info):
    if request.user.is_authenticated:
        info = info.split(",")

        user = User.objects.get(username = info[0])
        if request.method == "POST":
            form = add_comercial_form(request.POST,request.FILES)
            if form.is_valid():
                comercial = form.save(commit = False)
                comercial.user = user
                comercial.email = info[-1]
                comercial.password = info[1]
                comercial.save()
                return redirect("home_page")

        else:
            form = add_comercial_form
        return render(request,"add_commercial.html",{"form":form})
    else:
        return redirect("login_user")
    
def create_tech(request,info):
    if request.user.is_authenticated:
        info = info.split(",")

        user = User.objects.get(username = info[0])
        if request.method == "POST":
            form = add_tech_form(request.POST,request.FILES)
            if form.is_valid():
                comercial = form.save(commit = False)
                comercial.user = user
                comercial.email = info[-1]
                comercial.password = info[1]
                comercial.save()
                return redirect("home_page")

        else:
            form = add_comercial_form
        return render(request,"add_commercial.html",{"form":form})
    else:
        return redirect("login_user")
def users_view(request,type):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        if type == "commercial":
            data = Comercial.objects.all()
            return render(request,"see_users.html",{"data":data})
        elif type == "tech":
            data = Tech.objects.all()
            return render(request,"see_users.html",{"data":data})
    else:
        return redirect("login_user")
def search_methods(request):
    if request.user.is_authenticated:
        return render(request,"search_methods.html",{})

    else:
        return redirect(request,"login_user")
def search_form(request,method):
    if request.user.is_authenticated:
        admin_user_info = Administrateur.objects.get(user = request.user)
        if request.method == "POST":
            search = request.POST["search"]
            if method == "email":
                data_email = f"{search}|{method}"
                return redirect("search_method_result",result = data_email)
            elif method == "nom":
                data_nom = f"{search}|{method}"
                return redirect("search_method_result",result = data_nom)
            elif method =="pn":
                data_pn = f"{search}|{method}"
                return redirect("search_method_result", result = data_pn)
        return render(request,"search/search_form.html",{"method" : method})
    else:
        return redirect("login_user")
def search_method_result(request,result):
    if request.user.is_authenticated:
        result1 = result.split('|')
        print(result)
        method = result1[-1]
        if method == "email":
            resulte = Order.objects.filter(email__contains = result[0])
        elif method == "pn":
            resulte = Order.objects.filter(ntel = result[0])
        elif method == "nom":
            resulte = Order.objects.filter(nom__contains = result[0])
        return render(request,'search_result.html',{"result":resulte})

    else:
        return redirect("login_user")
def add_remarque(request,ordre_id):
    if request.user.is_authenticated:
        ordre = Order.objects.get(pk = ordre_id)
        if request.method == "POST":
            form = add_remarque_form(request.POST)
            if form.is_valid():
                remarque = form.save(commit = False)
                remarque.posted_by = request.user
                remarque.ordre = ordre
                remarque.save()
                return redirect("details_view",ordre_id = ordre_id)
        else:
            form = add_remarque_form
        return render(request,'add_remarque_form.html',{"form": form})
    else:
        return redirect("login_user")
def see_remarque(request,ordre_id):
    if request.user.is_authenticated:
        ordre = Order.objects.get(pk = ordre_id)
        data = Remarque.objects.filter(ordre = ordre)
        return render(request,"remarque.html",{"data":data})
    else:
        return redirect("login_user")

def add_sav(request,ordre_id):
    if request.user.is_authenticated:
        
        ordre = Order.objects.get(pk = ordre_id)
        if request.method == "POST":
            form = add_sav_form(request.POST)
            if form.is_valid():
                sav = form.save(commit = False)
                sav.posted_by = request.user
                sav.ordre = ordre
                sav.save()
                return redirect("details_view", ordre_id = ordre_id)
        else:
            form = add_sav_form
        return render(request,'add_sav_form.html',{"form":form})
    else:
        return redirect("login_user")
                



from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
import io
def create_sav_pdf(order_data, output_file):
    # Create a PDF document
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    # Create a list to hold the elements of the document
    elements = []

    # Define colors
    light_grey = colors.lightgrey

    # Set custom font styles
    title_style = getSampleStyleSheet()["Title"]
    title_style.fontName = "Helvetica-Bold"
    title_style.textColor = colors.blue

    normal_style = getSampleStyleSheet()["Normal"]
    normal_style.fontName = "Helvetica"
    normal_style.leading = 20  # Increase line spacing

    # Add the title
    title = Paragraph("<b>Fiche d’intervention SAV</b>", title_style)
    elements.append(title)

    # Add a space
    elements.append(Spacer(2, 56))  # Add vertical space

    # Add the data fields
    for field_name, field_value in order_data.items():
        field_name = field_name.replace('_', ' ').capitalize()
        field_paragraph = Paragraph(f"<b>{field_name}:</b> {field_value}", normal_style)
        elements.append(field_paragraph)
        elements.append(Spacer(2,10))
    elements.append(Spacer(1,40))
    centered_style = ParagraphStyle(name="Centered", alignment=1, parent=normal_style)
    centered_style.fontName = "Helvetica-Bold" 
    elements.append(Paragraph("Signature client:", style=centered_style))
    # Create the document
    return doc,elements
    

def generate_sav(request,ordre_id):
    if request.user.is_authenticated:
        ordre = Order.objects.get(pk = ordre_id)
        sav = SAV.objects.get(ordre = ordre)    
        data = {
            "Nom_et_prenom_du_client": f"{sav.Nom_et_prenom_du_client}",
            "date_de_l_intallation": f"{sav.date_de_l_intallation}",
            "equipe_qui_installe_toiture": f"{sav.equipe_qui_installe_toiture}",
            "Raccordement_electiricien": f"{sav.Raccordement_electiricien}",
            "nom_sou_traitant": f"{sav.nom_sou_traitant}",
            "description_de_la_panne": f"{sav.description_de_la_panne}",
            "heure_darrive": f"{sav.heure_darrive}",
            "heure_de_depart": f"{sav.heure_de_depart}",
            "temps_intervention": f"{sav.temps_intervention}",
            "materiel_utilise": f"{sav.materiel_utilise}",
            "remarque": f"{sav.remarque}",
        }
        buf = io.BytesIO()

        doc,elements = create_sav_pdf(order_data=data,output_file=buf)
        doc.build(elements)

        buf.seek(0)
        
        return FileResponse(buf,as_attachment=True, filename = f"{sav.Nom_et_prenom_du_client}_sav.pdf" )

def generate_pdf(request, ordre_id):
    # Fetch the order using the provided order_id
    if request.user.is_authenticated:
        order = Order.objects.get(pk=ordre_id)
        
        # Create a BytesIO buffer to store the PDF
        order_data = {
        "date_de_visite": f"{order.date_de_visite}",
        "posted_by": f"{order.posted_by}",
        "nom": f"{order.nom}",
        "prenom": f"{order.prenom}",
        "adresse": f"{order.adresse}",
        "cp": f"{order.cp}",
        "localite": f"{order.localite}",
        "ngsm": f"{order.ngsm}",
        "ntel": f"{order.ntel}",
        "email": f"{order.email}",
        "nom_de_societe": f"{order.nom_de_societe}",
        "forme_juridique": f"{order.forme_juridique}",
        "date_de_signature": f"{order.date_de_signature}",
        "ean54145": f"{order.ean54145}",
        "ncompte": f"{order.ncompte}",
        "bic": f"{order.bic}",
        "grd": f"{order.grd}",
        "ncompteur": f"{order.ncompte}",
        "ntva": f"{order.ntva}",
        "adress_de_facturation_adress": f"{order.adress_de_facturation_adress}",
        "adress_de_facturation_cp": f"{order.adress_de_facturation_cp}",
        "adress_de_facturation_localite": f"{order.adress_de_facturation_localite}",
        "adress_de_livraison_adress": f"{order.adress_de_livraison_adress}",
        "adress_de_livraison_cp": f"{order.adress_de_livraison_cp}",
        "adress_de_livraison_localite": f"{order.adress_de_livraison_localite}",
        "remarque": f"{order.remarque_1}",


        "nombre_ppv": f"{order.nombre_ppv}",
        "type_pvv":  f"{order.type_ppv}",
        "type_de_range_ppv":  f"{order.nombre_de_range_ppv}",
        "nombre_pan_de_toiture":f"{order.nombre_pan_de_toiture}",
        "nombre_ppv_toiture_1": f"{order.nombre_ppv_toiture_1}",
        "toiture_1": f"{order.toiture}",
        "sous_toiture": f"{order.sous_toiture}",
        "type_de_corniche":  f"{order.type_de_corniche}",
        "tuile_rechange" : f"{order.tuile_rechage}",
        "nombre_ppv_toiture_2":f"{order.nombre_ppv_toiture_2}",
        "orientation":f"{order.orientation}",
        "hauteur_sous_corniche": f"{order.hauteur_sous_corniche}",
        "si_7m_nacelle": f"{order.si_de7m_nacelle}",
        "etat_du_toit" : f"{order.etat_du_toit}",
        "les_panneaux_doivent_etre_installe": f"{order.les_panneaux_doivent_etre_installes}",
        "si_a_larriere_yatil_un_acces": f"{order.si_pas_dacces_decrire_la_situation}",
        "si_non_decrire_la_situation": f"{order.si_pas_dacces_decrire_la_situation}",
        "acces_libre_le_jour_du_chantier": f"{order.acces_libre_le_jour_du_chantier}",
        "nombre_ppv_toiture_3": f"{order.nombre_ppv_toiture_3}",
        "toiture_3": f"{order.toiture_3}",


        "type_de_compteur": f"{order.type_de_compteur}",
        "onduleur_1" : f"{order.onduleur_1}",
        "onduleur_2": f"{order.onduleur_2}",
        "onduleur_3": f"{order.onduleur_3}",
        "Nombre_doptimiseur" : f"{order.Nombre_doptimiseur}",
        "Enphase": f"{order.enphase}",
        "gaine_technique_present": f"{order.gaine_technique_present}",
        "Espace_pres_du_coffret_pour_londuleur_meme_piece": f"{order.espace_pres_du_coffret_pour_onduleur_meme_piece}",
        "etat_de_linstalation": f"{order.etat_de_linstallation}",
        "prise_de_terre_controlee_ces_5_dernier_annes": f"{order.prise_de_terre_controle_5_derniere_annes}",
        "presence_differentiel_general": f"{order.pressence_differentiel_general}",
        "coffret_20cm_disponible": f"{order.coffret_20_cm_disponible}",
        "tranchee": f"{order.tranche}",
        "nombre_de_metres_de_tranche":  f"{order.nombre_de_metre_de_tranche}",
        "le_client_se_charge_de_gaine": f"{order.le_client_se_charge_de_gaine}",
        "nombre_de_metre_entre_onduleur_et_panneaux":f"{order.nombre_de_metres_entre_onduleur_et_panneaux}",

        "client_monitoring": f"{order.le_client_souheite_il_le_monitoring}",
        "modem_meme_piece_que_loduleur": f"{order.modem_est_dans_la_meme_piece_que_londuleur}",
        "nombre_de_metres_modem_onduleur": f"{order.nombres_de_metres_du_modem_a_lonuduleur}",
        "finance": f"{order.le_projet_sera_finance_par}",
        "condition_de_paiement": f"{order.condition_de_paiement}",

        "date_de_la_vt": f"{order.date_de_la_vt}",
        "vt_effectue_par": f"{order.vt_effectue_par}",
        "commentaire_technicien":f"{order.commentaire_technicien}",
        "statut_vt": f"{order.statut_vt}",
        "coffret_general_conforme": f"{order.coffret_general_conforme}",
        "ajout_coffret_supp": f"{order.ajout_coffret_supp}",
        "differencial_general": f"{order.differenciel_general}",
        "prevoir_un_differential_general": f"{order.prevoir_un_differentiel_general}",
        "limiteur": f"{order.limiteur}",
        "prevoir_un_limiteur": f"{order.prevoir_un_limiteur}",
        "test_de_la_terre": f"{order.test_de_la_terre}",
        "nbr_de_metre_de_cable_a_prevoir": f"{order.nbr_de_metre_de_cable_a_prevoir}",
        "type_de_cable": f"{order.type_de_cable}",
        "tranche": f"{order.tranche}",
        "nbr_de_metre_de_tranchee": f"{order.nombre_de_metre_de_tranche}",
        "monitoring": f"{order.monitoring}",
        "modem_est_dans_la_meme_piece_que_londuleur": f"{order.modem_est_dans_la_meme_piece_que_londuleur}",
        "analyse_modem" : f"{order.analyse_modem}",

        "type_toiture_prevu" : f"{order.type_de_toitur_prevu}",
        "type_toiture_prevu_a_la_vt": f"{order.type_toiture_prevu_a_la_vt}",
        "nbr_de_ppv": f"{order.nbr_de_ppv}",
        "nb_de_ppv_a_la_vt": f"{order.nbr_de_ppv_a_la_vt}",
        "ppv_en_portrait":f"{order.ppv_en_portait}",
        "ppv_en_chevalet_jardin": f"{order.ppv_en_chevalet_jardin}",
        "ppv_en_structure_jardin": f"{order.ppv_en_structure_jardin}",
        "sous_toiture": f"{order.sous_toiture_2}",
        "le_client_a_des_adroises": f"{order.le_client_a_des_ardoise_tuiles_de_rechange}",
        "nbr_dadroises": f"{order.nbr_dardoises_tuiles_rechange}"

    }
        buf = io.BytesIO()
        c = create_order_info_pdf(order_data,buf)
        c.save()
        buf.seek(0)
        
        return FileResponse(buf,as_attachment=True, filename = f"{order.nom}_ordre.pdf" )

"""
  if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        lesson = Lesson.objects.get(pk = lesson_id)
        form = add_lesson_forms(request.POST or None,request.FILES or None,instance=lesson)
        print(lesson.classroom.id)
        classroomr = Classroom.objects.get(pk = lesson.classroom.id)
        print(lesson.classroom)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.teacher = teacher_info
            lesson.module = teacher_info.module
            lesson.classroom = classroomr
            lesson.save()
            return redirect("teacher_home_page")

"""
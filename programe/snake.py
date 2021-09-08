##      A FAIRE:        ####################################################################################################################################################
##      faire une bande annonce pour le jeu
##      baisser le son de 1 game over qui est trop fort
##      compiler py2exe
##  -modifier dossier
#####      -mettre les bons sons/icon/image(bonus/malus)
##      -ajouter bouton change de couleur ou taille augmente quand on passe dessus avec souris
##      -ajouter des succes au jeu
##  -faire page 5(page jouer)
##      -ajouter un easter egg (combinaison d'objet mangé(exemple:pomme,pomme,pomme,coffre,piece,piece,pomme,vie))
##      -verifier quil reste de la place sur le terrain pour faire pop un objet
##      -verifier que quand il ne reste qu'une place l'objet qui spawn soit une pomme et les autre objet soit desactiver
##      -gerer la victoire
##      -gerer l'intro avec les fps et pas les wait
##      -differente couleur pour piege , j1, j2
##      -aleatoir
##  -faire shop achat bonus
##      -amelioration % chance objet
##      -posibilité de commencee avec 1 vie en plus que d'habitude au tour suivant
##      -posibilité de commencer avec 1 vie en plus a tous les tours
##      -possibilite de commencer avec piece x2 pendant toute la partie
##      -skin
##      -theme
##      -objet
##      -mode
##      -faire positionement rubrique en fonction des achat restant
##      -verifier que les item sont pas tous unlock
##      -verifier que la rubrique est presente pour verifier les zones
############################################################################################################################################################################
#######################################################################################################################################################################
#
#                    URGENCE
#   -mettre image (coffre,multiplicateur point)
#
#   -ajouter des aliments random qui quand on en mange 3 donne une vie
#   -aleatoire
#
#   -gerer item/skin en fonction des locks
#
#   -vitesse normal dans le shop au lieux de lente
#   -ajouter barre de niveau
#   -gerer bouton upgrade achat , pour l'instant on peut que debloquer
#   -faire systeme actualise info des achats
#   -stocker les infos qui s'ameliore
#   -gerer les options dispo en fonction des locks(surtout mode special)
#
#   -choisir les couleurs definitive
#   -image des themes : carree de 2 couleur(ceux du theme) avec un contour .
#
#   -gerer la victoir/nbr de place etc
#   -enlever les wait de lanimation fondu
#
############################################################################################################################################################################
############################################################################################################################################################################
#importation et initialisation de pygame
import pygame
from os import environ
from random import *
from pygame.locals import *
from math import*
pygame.init()

#importation des valeurs du fichier valeur.py
from valeur import *

#creation de la fenetre
pygame.display.set_caption(titre)   #titre
icon_insertion = pygame.image.load(icon)  #icone
pygame.display.set_icon(icon_insertion)
environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%position_fen_wind
fenetre = pygame.display.set_mode(taille_fenetre)

#initialisation fps
fps=fps_admin
#initialisation intro
intro_fondu=intro_fondu_admin
#initialisation numero fenetre
number_create_fen=num_admin_page
#inittialisation moment fondu
moment_fondu=moment_fondu_admin
#initialisation action_quitt
action_quitt=False

tete=tete_admin
#initialisation parametre option
init_fichier = open(src_sauvegarde, "r")        
contenu =init_fichier.readlines()


num_txt4_bouton=int((contenu[0])[:-1])
num_txt5_bouton=int((contenu[1])[:-1])
num_txt9_bouton=int((contenu[2])[:-1])

num_case1=bool(int((contenu[3])[:-1]))
num_case2=bool(int((contenu[4])[:-1]))

num_score_txt_mode=int((contenu[5])[:-1])

num_case3=bool(int((contenu[6])[:-1]))
num_case4=bool(int((contenu[7])[:-1]))
num_case5=bool(int((contenu[8])[:-1]))
num_case6=bool(int((contenu[9])[:-1]))

num_case7=bool(int((contenu[10])[:-1]))
num_case8=bool(int((contenu[11])[:-1]))

num_case9=bool(int((contenu[12])[:-1]))
num_case10=bool(int((contenu[13])[:-1]))
num_case11=bool(int((contenu[14])[:-1]))
num_case12=bool(int((contenu[15])[:-1]))

argent=int((contenu[16])[:-1])

num_case13=bool(int((contenu[17])[:-1]))
num_case14=bool(int((contenu[18])[:-1]))
num_case15=bool(int((contenu[19])[:-1]))

init_fichier.close()



#definition de fenetre
def draw_fenetre():
    global fond_shop,r_col,g_col,b_col,compteur_time_invers_j1,compteur_time_invers_j2,invers_touche_j1,invers_touche_j2,compt_spawn_invers_touche,compt_spawn_div_pts,compt_spawn_moins_pts,compt_spawn_coffre,bouclier_actif2,bouclier_actif1,compt_spawn_bouclier,compteur_time_boost_point_actif2,compteur_time_boost_point_actif1,multiplicateur_point1,multiplicateur_point2,boost_point1,boost_point2,multiplicateur_piece,compteur_time_boost_piece_actif,boost_piece,compt_spawn_boost_piece,validation_creation,comp_app_pomme_multi,time_spawn_pomme,agrandir_serpent,gain_point,numero_joueur,position_pomme_gold,position_pomme,position_bonus_plus_pts,compt_spawn_plus_pts,position_piece,argent,compt_spawn_piece,position_bonus_vie,compt_bonus_vie,vie_perdu,nbr_vie_draw,fond,terrain_jeu_snake,direction_p,direction_p2,pomme_draw,pomme_draw_time,serpent1,serpent2,number_create_fen,vie_serpent1,vie_serpent2,stop_game_over,txt2_1_titre,txt2_2_titre,fps









    #fenetre connectionpage     page0
    if number_create_fen==0:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))

        police = pygame.font.Font(police1,taille1_police)
        texte = police.render(txt1_titre,True,color2)
        fond.blit(texte,position1_titre)









    #fenetre creation compte    page1
    if number_create_fen==1:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))

        police = pygame.font.Font(police1,taille1_police)
        texte = police.render(txt1_titre,True,color2)
        fond.blit(texte,position1_titre)











    #fenetre menu jeu   page2
    elif number_create_fen==2:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))

        #titre
        police = pygame.font.Font(police1,taille1_police)
        texte = police.render(txt1_titre,True,color2)
        fond.blit(texte,position1_titre)

        #bouton1
        bouton_1=pygame.draw.rect(fond,color2,position1_bouton)

        police = pygame.font.Font(police1,taille2_police)
        texte = police.render(txt1_bouton,True,color1)
        fond.blit(texte,position1_txt_bouton)

        #bouton2
        bouton_2=pygame.draw.rect(fond,color2,position2_bouton)

        police = pygame.font.Font(police1,taille2_police)
        texte = police.render(txt2_bouton,True,color1)
        fond.blit(texte,position2_txt_bouton)

        #bouton3
        bouton_3=pygame.draw.rect(fond,color2,position3_bouton)

        police = pygame.font.Font(police1,taille2_police)
        texte = police.render(txt3_bouton,True,color1)
        fond.blit(texte,position3_txt_bouton)

        #shop
        load_img(img_shop)
        m,p,o=color2
        fill(img, pygame.Color (m,p,o))
        fond.blit(img, position_shop)

        #skin
        load_img(img_menu_skin)
        m,p,o=color2
        fill(img, pygame.Color (m,p,o))
        fond.blit(img, position_skin_menu)









    #fenetre option   page3
    elif number_create_fen==3:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))
            
        if num_fen_option==0:

            #titre option
            police = pygame.font.Font(police1,taille1_police)
            texte = police.render(txt3_titre,True,color2)
            fond.blit(texte,position3_titre)
            

            #texte/bouton 1 vitesse
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt1,True,color2)
            fond.blit(texte,position1_txt)

            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt4_bouton,True,color2)
            fond.blit(texte,position4_txt_bouton)

            #texte/bouton 2 mode
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt2,True,color2)
            fond.blit(texte,position2_txt)

            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt5_bouton,True,color2)
            fond.blit(texte,position5_txt_bouton)

            #texte/bouton 3 son
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt3,True,color2)
            fond.blit(texte,position3_txt)

            if num_case1==True:
                txt_case1=symbole_valide
            else :
                txt_case1=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case1,True,color2)
            fond.blit(texte,position1_case)

            #texte/bouton 4  musique
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt4,True,color2)
            fond.blit(texte,position4_txt)

            if num_case2==True:
                txt_case2=symbole_valide
            else :
                txt_case2=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case2,True,color2)
            fond.blit(texte,position2_case)

            #texte/bouton 6 theme
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt5,True,color2)
            fond.blit(texte,position5_txt)

            if num_txt9_bouton==0:
                txt9_bouton=txt6_0_bouton
            elif num_txt9_bouton==1:
                txt9_bouton=txt6_1_bouton
            elif num_txt9_bouton==2:
                txt9_bouton=txt6_2_bouton
            elif num_txt9_bouton==3:
                txt9_bouton=txt6_3_bouton
            elif num_txt9_bouton==4:
                txt9_bouton=txt6_4_bouton
            elif num_txt9_bouton==5:
                txt9_bouton=txt6_5_bouton
            elif num_txt9_bouton==6:
                txt9_bouton=txt6_6_bouton
            elif num_txt9_bouton==7:
                txt9_bouton=txt6_7_bouton
            elif num_txt9_bouton==8:
                txt9_bouton=txt6_8_bouton

            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt9_bouton,True,color2)
            fond.blit(texte,position9_txt_bouton)

            #bonus
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt18,True,color2)
            fond.blit(texte,position18_txt)

            if num_case7==True:
                txt_case7=symbole_valide
            else :
                txt_case7=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case7,True,color2)
            fond.blit(texte,position7_case)

            #malus
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt19,True,color2)
            fond.blit(texte,position19_txt)

            if num_case8==True:
                txt_case8=symbole_valide
            else :
                txt_case8=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case8,True,color2)
            fond.blit(texte,position8_case)

        elif num_fen_option==1:
            #titre special
            police = pygame.font.Font(police1,taille4_police)
            texte = police.render(txt5_titre,True,color2)
            fond.blit(texte,position5_titre)
        
            #texte/bouton bordure
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt14,True,color2)
            fond.blit(texte,position14_txt)

            if num_case3==True:
                txt_case3=symbole_valide
            else :
                txt_case3=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case3,True,color2)
            fond.blit(texte,position3_case)

            #texte/bouton piege
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt15,True,color2)
            fond.blit(texte,position15_txt)

            if num_case4==True:
                txt_case4=symbole_valide
            else :
                txt_case4=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case4,True,color2)
            fond.blit(texte,position4_case)

            #texte/bouton multiproie
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt16,True,color2)
            fond.blit(texte,position16_txt)

            if num_case5==True:
                txt_case5=symbole_valide
            else :
                txt_case5=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case5,True,color2)
            fond.blit(texte,position5_case)

            #texte/bouton multijoueur
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt17,True,color2)
            fond.blit(texte,position17_txt)

            if num_case6==True:
                txt_case6=symbole_valide
            else :
                txt_case6=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case6,True,color2)
            fond.blit(texte,position6_case)
            
        elif num_fen_option==2:
            #titre bonus
            police = pygame.font.Font(police1,taille1_police)
            texte = police.render(txt6_titre,True,color2)
            fond.blit(texte,position6_titre)

        
            #texte/bouton point x2
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt20,True,color2)
            fond.blit(texte,position20_txt)

            if num_case9==True:
                txt_case9=symbole_valide
            else :
                txt_case9=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case9,True,color2)
            fond.blit(texte,position9_case)

            #texte/bouton + points
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt21+(str(bonus_plus_pts_point)+txt21_bis),True,color2)
            fond.blit(texte,position21_txt)
            
            if num_case10==True:
                txt_case10=symbole_valide
            else :
                txt_case10=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case10,True,color2)
            fond.blit(texte,position10_case)

            #texte/bouton vie
            if mode_multijoueur==False:
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt22,True,color2)
                fond.blit(texte,position22_txt)

                if num_case11==True:
                    txt_case11=symbole_valide
                else :
                    txt_case11=symbole_non_valide

                police = pygame.font.Font(police2,taille2_police)
                texte = police.render(txt_case11,True,color2)
                fond.blit(texte,position11_case)

            #texte/bouton bouclier
            if mode_piege==True:
                if mode_multijoueur==False:
                    y_position23_txt=y1_position23_txt
                    y_position12_case=y1_position12_case
                else:
                    y_position23_txt=y2_position23_txt
                    y_position12_case=y2_position12_case
                    
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt23,True,color2)
                fond.blit(texte,(x_position23_txt,y_position23_txt))

                if num_case12==True:
                    txt_case12=symbole_valide
                else :
                    txt_case12=symbole_non_valide

                police = pygame.font.Font(police2,taille2_police)
                texte = police.render(txt_case12,True,color2)
                fond.blit(texte,(x_position12_case,y_position12_case))
        elif num_fen_option==3:
            #titre malus
            police = pygame.font.Font(police1,taille1_police)
            texte = police.render(txt7_titre,True,color2)
            fond.blit(texte,position7_titre)
        
            #texte/bouton div pts
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt24,True,color2)
            fond.blit(texte,position24_txt)
            
            if num_case13==True:
                txt_case13=symbole_valide
            else :
                txt_case13=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case13,True,color2)
            fond.blit(texte,position13_case)

            #texte/bouton -pts
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render((txt25+str(malus_moins_pts_point)+txt25_bis),True,color2)
            fond.blit(texte,position25_txt)
            
            if num_case14==True:
                txt_case14=symbole_valide
            else :
                txt_case14=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case14,True,color2)
            fond.blit(texte,position14_case)

            #texte/bouton inversement
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt26,True,color2)
            fond.blit(texte,position26_txt)
        
            if num_case15==True:
                txt_case15=symbole_valide
            else :
                txt_case15=symbole_non_valide

            police = pygame.font.Font(police2,taille2_police)
            texte = police.render(txt_case15,True,color2)
            fond.blit(texte,position15_case)

        #>
        if num_txt5_bouton==5:
            police = pygame.font.Font(None,taille1_police)
            texte = police.render(txt11_bouton,True,color2)
            fond.blit(texte,position_txt11_1_bouton)
                
        #bouton 5 menu
        bouton_6=pygame.draw.rect(fond,color2,position6_bouton)
        
        police = pygame.font.Font(police1,taille2_police)
        texte = police.render(txt6_bouton,True,color1)
        fond.blit(texte,position6_txt_bouton)




    #fenetre score   page4
    elif number_create_fen==4:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))

        initialiser_mode_score()
        #titre
        police = pygame.font.Font(police1,taille1_police)
        texte = police.render(txt2_titre,True,color2)
        fond.blit(texte,position2_titre)

        #<
        police = pygame.font.Font(None,taille1_police)
        texte = police.render(txt10_bouton,True,color2)
        fond.blit(texte,position_txt10_bouton)

        #>
        police = pygame.font.Font(None,taille1_police)
        texte = police.render(txt11_bouton,True,color2)
        fond.blit(texte,position_txt11_bouton)

        #1-
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt9,True,color2)
        fond.blit(texte,position9_txt)

        #2-
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt10,True,color2)
        fond.blit(texte,position10_txt)

        #3-
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt11,True,color2)
        fond.blit(texte,position11_txt)

        #4-
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt12,True,color2)
        fond.blit(texte,position12_txt)

        #5-
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt13,True,color2)
        fond.blit(texte,position13_txt)

        #mode
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt2,True,color2)
        fond.blit(texte,position14_0_txt)

        #mode variable
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(score_txt_mode,True,color2)
        fond.blit(texte,position_txt2_1_1_titre)

        init_record()

        #1- variable
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt_record1,True,color2)
        fond.blit(texte,position_txt_record1)

        #2- variable
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt_record2,True,color2)
        fond.blit(texte,position_txt_record2)

        #3- variable
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt_record3,True,color2)
        fond.blit(texte,position_txt_record3)

        #4- variable
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt_record4,True,color2)
        fond.blit(texte,position_txt_record4)

        #5- variable
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt_record5,True,color2)
        fond.blit(texte,position_txt_record5)





        #bouton menu
        bouton_6=pygame.draw.rect(fond,color2,position6_bouton)

        police = pygame.font.Font(police1,taille2_police)
        texte = police.render(txt6_bouton,True,color1)
        fond.blit(texte,position6_txt_bouton)










###################################################################################################################################################################
###################################################################################################################################################################

#################################           JOUER           FENETRE 5               ###############################################################################

###################################################################################################################################################################
###################################################################################################################################################################

        
    elif number_create_fen==5:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))        
        terrain_jeu_snake=pygame.Surface(taille_terrain_jeu_snake)
        terrain_jeu_snake.fill((color2))


###########################################################################
#############                                           ###################
#############       REDIMENSIONNER LE SERPENT           ###################
#############                                           ###################
###########################################################################
        
        if pause==True:
            menu_pause_surface=pygame.Surface(taille_menu_pause_surface)
            menu_pause_surface.fill((color2))
            fond_menu_pause=pygame.draw.rect(menu_pause_surface,color1,position_fond_menu_pause)

            bouton_menu1=pygame.draw.rect(menu_pause_surface,color2,position_menu_bouton1)
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt1_menu_pause,True,color1)
            menu_pause_surface.blit(texte,position_txt_bouton_menu1)
        
            bouton_menu2=pygame.draw.rect(menu_pause_surface,color2,position_menu_bouton2)
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt2_menu_pause,True,color1)
            menu_pause_surface.blit(texte,position_txt_bouton_menu2)
            
        else:
            #changement du serpent (joueur 1)
            if vie_serpent1>0:
                numero_joueur=1
                
                #faire avancer le serpent
                avance_serpent1()
                
                agrandir_serpent=False
                
                #colision pomme
                colision_pomme()

                #colision pomme or
                colision_pomme_gold()
                
                #suprimer la queue
                if agrandir_serpent==False:
                    del serpent1[-1]
                    
            #changement du serpent(joueur 2)
            if mode_multijoueur==True:
                if vie_serpent2>0:
                    numero_joueur=2
                    
                    #faire avancer le serpent
                    avance_serpent2()
                    
                    agrandir_serpent=False
                    #colision pomme
                    colision_pomme()

                    #colision pomme or
                    colision_pomme_gold()

                    #suprimer la queue
                    if agrandir_serpent==False:
                        del serpent2[-1]
            
            

    ###########################################################################
    #############                                           ###################
    #############               VIE EN MOINS                ###################
    #############                                           ###################
    ###########################################################################
                        

            #colision qui ne concerne que le joueur 1
            if vie_serpent1>0:
                #colision avec son propre corp
                if serpent1[0] in serpent1[1:]:
                    verification_serpent1_mort()

                #colision avec la bordure
                if mode_ouvert==False:
                    if (serpent1[0])[0]==-1 or (serpent1[0])[0]==20 or (serpent1[0])[1]==-1 or (serpent1[0])[1]==20:        
                        verification_serpent1_mort()

                #colision avec un piege
                if mode_piege==True:
                    x=0
                    for a in position_piege:
                        if serpent1[0] ==a:
                            if bonus_bouclier==True:
                                if bouclier_actif1==True:
                                    bouclier_actif1=False
                                    del position_piege[x]
                                    play_son_bouclier_perdu()
                                else:
                                    verification_serpent1_mort()
                            else:
                                verification_serpent1_mort()
                        x+=1

            #colision qui s'ajoute a cause du mode multijoueur
            if mode_multijoueur==True:
                #colision qui concerne les deux joueurs 
                if vie_serpent1>0 and vie_serpent2>0:
                    colision_1_in_2=False
                    colision_2_in_1=False
                    
                    #colision avec corp (tete du serpent 1 dans le corp du serpent 2 )
                    if serpent1[0] in serpent2:       
                        colision_1_in_2=True
                        vie_serpent1-=1
                    #colision avec corp (tete du serpent 2 dans le corp du serpent 1 )
                    if serpent2[0] in serpent1:      
                        colision_2_in_1=True
                        vie_serpent2-=1

                    #ajout des points gagner en tuant l'adversaire
                    if colision_1_in_2==False or colision_2_in_1==False:
                        if colision_2_in_1==True:
                            numero_joueur=1
                            gain_point=bonus_mort_autre_serpent
                            score_up()
                            play_son_mort()
                        elif colision_1_in_2==True:
                            numero_joueur=2
                            gain_point=bonus_mort_autre_serpent
                            score_up()
                            play_son_mort()

                #colision qui ne concerne que le joueur 2
                if vie_serpent2>0 :
                    #colision avec son propre corp
                    if serpent2[0] in serpent2[1:]:     
                        mort_serp2()
                            
                    #colision avec la bordure
                    if mode_ouvert==False:
                        if (serpent2[0])[0]==-1 or (serpent2[0])[0]==20 or (serpent2[0])[1]==-1 or (serpent2[0])[1]==20:        
                            mort_serp2()
                        
                    #colision avec un piege
                    if mode_piege==True:
                        x=0
                        for a in position_piege:
                            if serpent2[0] ==a:
                                if bonus_bouclier==True:
                                    if bouclier_actif2==True:
                                        bouclier_actif2=False
                                        del position_piege[x]
                                        play_son_bouclier_perdu()
                                    else:
                                        mort_serp2()
                                else:
                                    mort_serp2()
                            x+=1
                            
                                
            
                    
            #on verifie si le jeu peu continuer
            if mode_multijoueur==False:
                if vie_serpent1==0:
                    stop_game_over=True
            else :
                if vie_serpent1==0 and vie_serpent2==0:
                    stop_game_over=True
                    
                #on supprime le corp du serpent mort
                if vie_serpent1==0:
                    serpent1=[]
                if vie_serpent2==0:
                    serpent2=[]
                

                
    ###########################################################################
    #############                                           ###################
    #############               SAUVEGARDE                  ###################
    #############                                           ###################
    ###########################################################################

                    
            if stop_game_over==True:
                sauvegarde_partie()

                #initialisation de la fenetre suivante
                init_score_record()
                number_create_fen=6
                fps=fps_admin
                draw_fenetre

            else:


    ###########################################################################
    #############                                           ###################
    #############               COLISION OBJET              ###################
    #############                                           ###################
    ###########################################################################

                if vie_serpent1>0:
                    
                    #colision qui ne concerne que le joueur 1
                    numero_joueur=1
                    
                    #colision avec un bonus de "plus point"
                    colision_plus_pts()

                    #colision avec un malus de "moins point"
                    colision_moins_pts()

                    #colision avec un malus div point
                    colision_div_pts()
                    
                    #colision avec une piece
                    colision_piece()

                    #colision avec un coffre(argent)
                    colision_coffre()

                    #colision avec un malus inversement touche
                    colision_invers_touche()

                    #colision avec une vie
                    colision_vie()

                    #colision avec un bouclier
                    colision_bouciler()
                            
                if mode_multijoueur==True:
                    if vie_serpent2>0:
                        
                        #colision qui ne concerne que le joueur 2
                        numero_joueur=2
                        
                        #colision avec un bonus de "plus point"
                        colision_plus_pts()

                        #colision avec un malus de "moins point"
                        colision_moins_pts()

                        #colision avec un malus div point
                        colision_div_pts()
                    
                        #colision avec une piece
                        colision_piece()

                        #colision avec un coffre(argent)
                        colision_coffre()

                        #colision avec un malus inversement touche
                        colision_invers_touche()

                        #colision avec un bouclier
                        colision_bouciler()

                        #colision avec un boost piece
                        colision_boost_piece()

                        #colision avec un boost point
                        colision_boost_point()

                if vie_serpent1>0:
                    
                    #colision qui ne concerne que le joueur 1
                    numero_joueur=1
                    
                    #colision avec un boost piece
                    colision_boost_piece()

                    #colision avec un boost point
                    colision_boost_point()


    ###########################################################################
    #############                                           ###################
    #############           MISE A JOUR DES ELEMENT         ###################
    #############                                           ###################
    ###########################################################################


                if boost_piece==True:
                    if compteur_time_boost_piece_actif==time_boost_piece_actif:
                        boost_piece=False
                        multiplicateur_piece=multiplicateur_piece_admin
                    compteur_time_boost_piece_actif+=1
                    
                if bonus_xpts==True:
                    if boost_point1==True:
                        if compteur_time_boost_point_actif1==time_boost_point_actif1:
                            boost_point1=False
                            multiplicateur_point1=multiplicateur_point_admin
                        compteur_time_boost_point_actif1+=1

                    if mode_multijoueur==True:
                        if boost_point2==True:
                            if compteur_time_boost_point_actif2==time_boost_point_actif2:
                                boost_point2=False
                                multiplicateur_point2=multiplicateur_point_admin
                            compteur_time_boost_point_actif2+=1

                if malus_invers_touche==True:
                    if invers_touche_j1==True:
                        if compteur_time_invers_j1==time_invers_touche_actif_j1:
                            invers_touche_j1=False
                        compteur_time_invers_j1+=1
                    if mode_multijoueur==True:
                        if invers_touche_j2==True:
                            if compteur_time_invers_j2==time_invers_touche_actif_j2:
                                invers_touche_j2=False
                            compteur_time_invers_j2+=1
                
                #creation pomme tous les x tick
                if mode_multiproie==True:
                    verification_validation_creation(position_pomme,limite_pomme)
                    if validation_creation==True:
                        comp_app_pomme_multi+=1
                        if comp_app_pomme_multi==time_spawn_pomme:
                            time_spawn_pomme=randint(chance1_pomme_plus,chance2_pomme_plus)
                            pomme_draw_time=False
                            pomme_draw+=1
                            comp_app_pomme_multi=0

                #ajout des nouvelles pommes
                for pppp in range(0,pomme_draw):     
                    new_pomme()
                    pomme_draw-=1

                #ajout de la nouvelle vie
                if bonus_vie==True:
                    verification_validation_creation(position_bonus_vie,limite_vie_instant)
                    if vie_serpent1+(len(position_bonus_vie))*bonus_vie_plus>=limite_vie:
                        validation_creation=False
                    if validation_creation==True:
                        compt_bonus_vie+=1
                        if compt_bonus_vie==time_bonus_vie:
                            new_bonus_vie()
                            compt_bonus_vie=0

                #ajout de la nouvelle piece
                verification_validation_creation(position_piece,limite_piece)
                verification_validation_piece()
                if validation_creation==True:
                    compt_spawn_piece+=1
                    if compt_spawn_piece==time_spawn_piece:
                        new_piece()
                        compt_spawn_piece=0

                #ajout du nouveau coffre
                verification_validation_creation(position_coffre,limite_coffre)
                verification_validation_coffre()
                if validation_creation==True:
                    compt_spawn_coffre+=1
                    if compt_spawn_coffre==time_spawn_coffre:
                        new_coffre()
                        compt_spawn_coffre=0

                #ajout du nouveau malus inversement touche
                verification_validation_creation(position_invers_touche,limite_invers_touche)
                if validation_creation==True:
                    compt_spawn_invers_touche+=1
                    if compt_spawn_invers_touche==time_spawn_invers_touche:
                        new_malus_invers_touche()
                        compt_spawn_invers_touche=0

                #ajout du nouveau boost de piece
                verification_validation_creation(position_boost_piece,limite_boost_piece)
                verification_validation_piece()
                verification_validation_boost_argent(multiplicateur_piece,limite_max_boost_piece)
                if validation_creation==True:
                    a=randint(chance1_spawn_boost_piece,chance2_spawn_boost_piece)
                    if a>=limite_autorisation_spawn_boost_piece:
                        new_boost_piece()

                #ajout du nouveau bonus de point
                if bonus_xpts==True:
                    verification_validation_creation(position_boost_point,limite_boost_point)
                    verification_validation_boost_point(multiplicateur_point1,limite_max_boost_point)
                    if mode_multijoueur==True:
                        verification_validation_boost_point(multiplicateur_point2,limite_max_boost_point)
                    if validation_creation==True:
                        a=randint(chance1_spawn_boost_point,chance2_spawn_boost_point)
                        if a>=limite_autorisation_spawn_boost_point:
                            new_boost_point()

                #ajout du nouveau bonus "plus point"
                if bonus_plus_pts==True:         
                    verification_validation_creation(position_bonus_plus_pts,limite_bonus_plus_point)
                    if validation_creation==True:
                        compt_spawn_plus_pts+=1
                        if compt_spawn_plus_pts==time_bonus_plus_pts:
                            new_bonus_plus_pts()
                            compt_spawn_plus_pts=0

                #ajout du nouveau malus "moins point"
                if malus_moins_pts==True:         
                    verification_validation_creation(position_malus_moins_pts,limite_malus_moins_point)
                    if validation_creation==True:
                        compt_spawn_moins_pts+=1
                        if compt_spawn_moins_pts==time_malus_moins_pts:
                            new_malus_moins_pts()
                            compt_spawn_moins_pts=0

                #ajout du nouveau malus "div point"
                if malus_div_pts==True:         
                    verification_validation_creation(position_malus_div_pts,limite_malus_div_point)
                    if validation_creation==True:
                        compt_spawn_div_pts+=1
                        if compt_spawn_div_pts==time_malus_div_pts:
                            new_malus_div_pts()
                            compt_spawn_div_pts=0

                #ajout du nouveau bouclier
                if bonus_bouclier==True:
                    verification_validation_creation(position_bonus_bouclier,limite_bouclier)
                    verification_validation_bouclier()
                    if validation_creation==True:
                        compt_spawn_bouclier+=1
                        if compt_spawn_bouclier==time_bonus_bouclier:
                            new_bonus_bouclier()
                            compt_spawn_bouclier=0

                #restart serpent
                if mode_multijoueur==False:         
                    if vie_perdu==True:     
                        vie_perdu=False
                        for cor in serpent[1:]:
                            x=cor[0]
                            y=cor[1]
                            pygame.draw.rect(terrain_jeu_snake,(color2),(x*25,y*25,25,25))
                        restart_position_serpent()
                        draw_fenetre()

    ### dessin objet ###
        if stop_game_over==False:
            #on affiche les pieges
            draw_piege()
            draw_pomme()
            draw_pomme_gold()
            draw_bonus_vie()
            draw_piece()
            draw_boost_piece()
            draw_boost_point()
            draw_bonus_plus_pts()
            draw_bonus_bouclier()
            draw_coffre()
            draw_malus_moins_pts()
            draw_malus_div_pts()
            draw_malus_invers_touche()

            if vie_serpent1>0:
                draw_serpent()
            if mode_multijoueur==True:
                if vie_serpent2>0:
                    draw_serpent2()

            

    ###limite point###
            if int(txt2_1_titre)>limite_pts:       #limite point
                txt2_1_titre=limite_pts
            if mode_multijoueur==True:
                if int(txt2_2_titre)>limite_pts:
                    txt2_2_titre=limite_pts

            

            if mode_multijoueur==False:
                #dessin coeur restant         
                for nbr_vie_draw in range(0,vie_serpent1):
                    draw_vie()
                    
                #titre score
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt2_titre,True,color2)
                fond.blit(texte,position5_bis0_titre)
                #score valeur
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt2_1_titre,True,color2)
                x_taille_txt_score_point1=texte.get_width()
                y_taille_txt_score_point1=texte.get_height()
                fond.blit(texte,position5_1_titre)

                x_boucl=position5_1_titre[0]+x_taille_txt_score_point1+10
                
                if multiplicateur_point1>multiplicateur_point_admin:
                    police = pygame.font.Font(police1,taille5_police)
                    texte = police.render("x"+str(multiplicateur_point1),True,color2)
                    y_taille_txt_boost_point1=texte.get_height()
                    x_taille_txt_boost_point1=texte.get_width()
                    fond.blit(texte, (position5_1_titre[0]+x_taille_txt_score_point1+5,position5_1_titre[1]+(y_taille_txt_score_point1-y_taille_txt_boost_point1+3)))
                    x_boucl+=x_taille_txt_boost_point1

                if bonus_bouclier==True:
                    if bouclier_actif1==True:
                        load_img(img_bouclier)
                        fond.blit(img, (x_boucl,position5_1_titre[1]+2))                

            else:
                #titre score j1
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt2_bis_titre,True,color2)
                fond.blit(texte,position5_bis_titre)
                #score j1 valeur
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt2_1_titre,True,color2)
                x_taille_txt_score_point1=texte.get_width()
                y_taille_txt_score_point1=texte.get_height()
                fond.blit(texte,position5_1_bis_titre)

                x_boucl=position5_1_bis_titre[0]+x_taille_txt_score_point1+10
                
                if multiplicateur_point1>multiplicateur_point_admin:
                    police = pygame.font.Font(police1,taille5_police)
                    texte = police.render("x"+str(multiplicateur_point1),True,color2)
                    y_taille_txt_boost_point1=texte.get_height()
                    x_taille_txt_boost_point1=texte.get_width()
                    fond.blit(texte, (position5_1_bis_titre[0]+x_taille_txt_score_point1+5,position5_1_bis_titre[1]+(y_taille_txt_score_point1-y_taille_txt_boost_point1+3)))
                    x_boucl+=x_taille_txt_boost_point1
                    
                if bonus_bouclier==True:
                    if bouclier_actif1==True:
                        load_img(img_bouclier)
                        fond.blit(img, (x_boucl,position5_1_bis_titre[1]+2))
                        
                #titre score j2
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt2_bis2_titre,True,color2)
                fond.blit(texte,position5_bis2_titre)
                #score j2 valeur
                police = pygame.font.Font(police1,taille3_police)
                texte = police.render(txt2_2_titre,True,color2)
                x_taille_txt_score_point2=texte.get_width()
                y_taille_txt_score_point2=texte.get_height()
                fond.blit(texte,position5_1_bis2_titre)

                x_bouc2=position5_1_bis2_titre[0]+x_taille_txt_score_point2+10
                
                if multiplicateur_point2>multiplicateur_point_admin:
                    police = pygame.font.Font(police1,taille5_police)
                    texte = police.render("x"+str(multiplicateur_point2),True,color2)
                    y_taille_txt_boost_point2=texte.get_height()
                    x_taille_txt_boost_point2=texte.get_width()
                    fond.blit(texte, (position5_1_bis2_titre[0]+x_taille_txt_score_point2+5,position5_1_bis2_titre[1]+(y_taille_txt_score_point2-y_taille_txt_boost_point2+3)))
                    x_bouc2+=x_taille_txt_boost_point2

                if bonus_bouclier==True:
                    if bouclier_actif2==True:
                        load_img(img_bouclier)
                        fond.blit(img, (x_bouc2,position5_1_bis2_titre[1]+2))

            #argent
            load_img(img_piece)
            fond.blit(img, (x_position_argent,y_position_argent))
            
        
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(str(argent),True,color2)
            x_position_txt_argent=texte.get_width()
            fond.blit(texte,((x_position_argent-x_position_txt_argent-espace_txt_argent),y_position_argent))

            if multiplicateur_piece>multiplicateur_piece_admin:
                police = pygame.font.Font(police1,taille5_police)
                texte = police.render("x"+str(multiplicateur_piece),True,color2)
                fond.blit(texte, (x_position_argent+10,y_position_argent+10))
            
            #mode
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt2,True,color2)
            fond.blit(texte,position5_0_txt)
            #mode valeur
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt5_bouton,True,color2)
            fond.blit(texte,position5_1_txt)

            pygame.draw.rect(fond,color2,taille_bande)


            



            fond.blit(terrain_jeu_snake,position_terrain_jeu_snake)
            if pause==True:
                fond.blit(menu_pause_surface,position_menu_pause_surface)

    #fenetre perdu   page6
    elif number_create_fen==6:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))

        if mode_multijoueur==False:
            position6_0_txt_good=position6_0_txt
            position7_txt_good=position7_txt
            position_txt5_0_bouton_good=position_txt5_0_bouton
            position_txt2_1_0_titre_good=position_txt2_1_0_titre
            position8_txt_good=position8_txt
            position_record_txt_good=position_record_txt
            txt7_good=txt7
        else:
            position6_0_txt_good=position6_0_bis_txt
            position7_txt_good=position7_bis_txt
            position_txt5_0_bouton_good=position_txt5_0_bis_bouton
            position_txt2_1_0_titre_good=position_txt2_1_0_bis_titre
            position8_txt_good=position8_bis_txt
            position_record_txt_good=position_record_bis_txt
            txt7_good=txt7_bis
            
        #titre
        police = pygame.font.Font(police1,taille1_police)
        texte = police.render(txt4_titre,True,color2)
        fond.blit(texte,position4_titre)

        #mode
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt2,True,color2)
        fond.blit(texte,position6_0_txt_good)
        
        #score/j1
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt7_good,True,color2)
        fond.blit(texte,position7_txt_good)
        
        #mode valeur
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt5_bouton,True,color2)
        fond.blit(texte,position_txt5_0_bouton_good)

        #score valeur
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt2_1_titre,True,color2)
        fond.blit(texte,position_txt2_1_0_titre_good)

        #record
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(txt8,True,color2)
        fond.blit(texte,position8_txt_good)
        
        #record valeur
        if num_txt5_bouton==0:
            record_txt=record_normale_1
        elif num_txt5_bouton==1:
            record_txt=record_ouvert_1
        elif num_txt5_bouton==2:
            record_txt=record_piege_1
        elif num_txt5_bouton==3:
            record_txt=record_multiproie_1
        elif num_txt5_bouton==4:
            record_txt=record_multijoueur_1
        elif num_txt5_bouton==5:
            record_txt=record_special_1

        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(record_txt,True,color2)
        fond.blit(texte,position_record_txt_good)

        if mode_multijoueur==True:
            #score j2
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt7_bis2,True,color2)
            fond.blit(texte,position7_bis2_txt)
            
            #score valeur j2
            police = pygame.font.Font(police1,taille3_police)
            texte = police.render(txt2_2_titre,True,color2)
            fond.blit(texte,position_txt2_2_0_titre)
            
        #bouton menu
        bouton_6=pygame.draw.rect(fond,color2,position6_bouton)

        police = pygame.font.Font(police1,taille2_police)
        texte = police.render(txt6_bouton,True,color1)
        fond.blit(texte,position6_txt_bouton)

    #fenetre shop   page7
    elif number_create_fen==7:
        fond=pygame.Surface(taille_fond)
        fond.fill((color1))
        fond_shop=pygame.Surface(taille_fond_shop)
        fond_shop.fill((color2))

        init_all_lock()
        
        #menu
        if num_fen_shop==1:
            #titre
            police = pygame.font.Font(police1,taille6_police)
            texte = police.render(txt8_titre,True,color2)
            fond.blit(texte,position8_titre)

        if num_fen_shop==2 or num_fen_shop==3:
            #skin
            if num_fen_shop_plus==1:
                #titre
                police = pygame.font.Font(police1,taille6_police)
                texte = police.render(txt9_titre,True,color2)
                fond.blit(texte,position9_titre)

            #objet
            elif num_fen_shop_plus==2:
                #titre
                police = pygame.font.Font(police1,taille6_police)
                texte = police.render(txt10_titre,True,color2)
                fond.blit(texte,position10_titre)

            #theme
            elif num_fen_shop_plus==3:
                #titre
                police = pygame.font.Font(police1,taille6_police)
                texte = police.render(txt11_titre,True,color2)
                fond.blit(texte,position11_titre)

            #mode
            elif num_fen_shop_plus==4:
                #titre
                police = pygame.font.Font(police1,taille6_police)
                texte = police.render(txt12_titre,True,color2)
                fond.blit(texte,position12_titre)           

            #vitesse
            elif num_fen_shop_plus==5:
                #titre
                police = pygame.font.Font(police1,taille6_police)
                texte = police.render(txt13_titre,True,color2)
                fond.blit(texte,position13_titre)
                
        if num_fen_shop==2 or num_fen_shop==1:
            impres_shop_img(image_load_shop_menu)

        if num_fen_shop==3:
            police = pygame.font.Font(police1,taille7_police)
            mot_description=""
            ligne_description_final=""
            description_final=[]
            i=0
            for j in description_achat:
                i+=1
                if not j==" ":
                    mot_description+=j
                if j==" " or  i==len(description_achat):
                    if len(ligne_description_final)>0 :
                        mot_description="   "+mot_description
                    texte = police.render((ligne_description_final+mot_description),True,color1)
                    if (texte.get_width())<=480:
                        ligne_description_final+=mot_description
                        mot_description=""
                    else:
                        description_final+=[ligne_description_final]
                        mot_description_retour=""
                        for h in mot_description:
                            if not h==" ":
                                mot_description_retour+=h
                        ligne_description_final=mot_description_retour
                        mot_description=""
            if len(ligne_description_final)>0:
                description_final+=[ligne_description_final]
            
            for i in range(0,len(description_final)):
                texte = police.render(description_final[i],True,color1)
                fond_shop.blit(texte,(position1_txt_description[0],position1_txt_description[1]+30*i))

            bouton7=pygame.draw.rect(fond_shop,color1,position7_bouton)

            police = pygame.font.Font(police1,taille2_police)
            texte = police.render(str(prix_achat),True,color2)
            position_txt_bouton7_x=(500-(texte.get_width()+30))//2
            fond_shop.blit(texte,(position_txt_bouton7_x,position_txt_bouton7_y))

            load_img(img_piece2)
            fond_shop.blit(img, ((position_txt_bouton7_x+texte.get_width()),position_txt_bouton7_y+5))
            
        #retour
        load_img(img_retour)
        m,p,o=color2
        fill(img, pygame.Color (m,p,o))
        fond.blit(img, position_retour)
        
        #argent
        load_img(img_piece)
        fond.blit(img, (x_position_argent,y_position_argent+10))
        
        police = pygame.font.Font(police1,taille3_police)
        texte = police.render(str(argent),True,color2)
        x_position_txt_argent=texte.get_width()
        fond.blit(texte,((x_position_argent-x_position_txt_argent-espace_txt_argent),y_position_argent+10))

        #bouton menu
        bouton_6=pygame.draw.rect(fond,color2,position6_bouton)

        police = pygame.font.Font(police1,taille2_police)
        texte = police.render(txt6_bouton,True,color1)
        fond.blit(texte,position6_txt_bouton)

        fond.blit(fond_shop,position_fond_shop)

def det_chaine_img_mode_option_bis():
    global image_load1_shop_bis
    image_load1_shop_bis=[]
    if lock_mode_normal < niveau_mode_normal_maximum:
        image_load1_shop_bis+=[img_mode_normal_shop]
    if lock_mode_ouvert < niveau_mode_ouvert_maximum:
        image_load1_shop_bis+=[img_mode_ouvert_shop]
    if lock_mode_piege < niveau_mode_piege_maximum:
        image_load1_shop_bis+=[img_mode_piege_shop]
    if lock_mode_multiproie < niveau_mode_multiproie_maximum:
        image_load1_shop_bis+=[img_mode_multiproie_shop]
    if lock_mode_multijoueur < niveau_mode_multijoueur_maximum:
        image_load1_shop_bis+=[img_mode_multijoueur_shop]
    if lock_mode_special < niveau_mode_special_maximum:
        image_load1_shop_bis+=[img_mode_special_shop]
    det_chaine_img_option(image_load1_shop_bis)

def det_chaine_img_theme_option_bis():
    global image_load1_shop_bis
    image_load1_shop_bis=[]
    if lock_theme_ninja < niveau_theme_ninja_maximum:
        image_load1_shop_bis+=[img_theme_ninja_shop]
    if lock_theme_negatif < niveau_theme_negatif_maximum:
        image_load1_shop_bis+=[img_theme_negatif_shop]
    if lock_theme_ikeo < niveau_theme_ikeo_maximum:
        image_load1_shop_bis+=[img_theme_ikeo_shop]
    if lock_theme_doume < niveau_theme_doume_maximum:
        image_load1_shop_bis+=[img_theme_doume_shop]
    if lock_theme_deadpoule < niveau_theme_deadpoule_maximum:
        image_load1_shop_bis+=[img_theme_deadpoule_shop]
    if lock_theme_epm < niveau_theme_epm_maximum:
        image_load1_shop_bis+=[img_theme_epm_shop]
    if lock_theme_girly < niveau_theme_girly_maximum:
        image_load1_shop_bis+=[img_theme_girly_shop]
    if lock_theme_dark_girly < niveau_theme_dark_girly_maximum:
        image_load1_shop_bis+=[img_theme_dark_girly_shop]
    if lock_theme_zeldo < niveau_theme_zeldo_maximum:
        image_load1_shop_bis+=[img_theme_zeldo_shop]
    det_chaine_img_option(image_load1_shop_bis)

def det_chaine_img_vitesse_option_bis():
    global image_load1_shop_bis
    image_load1_shop_bis=[]
    if lock_vitesse_lent < niveau_vitesse_lente_maximum:
        image_load1_shop_bis+=[img_vitesse_lent_shop]
    if lock_vitesse_normal < niveau_vitesse_normal_maximum:
        image_load1_shop_bis+=[img_vitesse_normal_shop]
    if lock_vitesse_rapide < niveau_vitesse_rapide_maximum:
        image_load1_shop_bis+=[img_vitesse_rapide_shop]
    if lock_vitesse_expert < niveau_vitesse_expert_maximum:
        image_load1_shop_bis+=[img_vitesse_expert_shop]
    if lock_vitesse_acceleration < niveau_vitesse_acceleration_maximum:
        image_load1_shop_bis+=[img_vitesse_acceleration_shop]
    det_chaine_img_option(image_load1_shop_bis)

def det_chaine_img_option(u):
    global image_load_shop_menu_bis
    image_load1_shop_menu=[]
    image_load2_shop_menu=[]
    l=0
    for i in u:
        if len(u)<=6:
            image_load1_shop_menu+=[i]
        else:
            if l<5:
                image_load1_shop_menu+=[i]
            elif l==5:
                image_load1_shop_menu+=[img_fleche_droite_shop]
                l+=1
                
            if l>5 and len(u)<=11:
                if l==6:
                    image_load2_shop_menu+=[img_fleche_gauche_shop]
                    l+=1
                if l>6 :
                    image_load2_shop_menu+=[i]
            else:
                if l==6:
                    image_load2_shop_menu+=[img_fleche_gauche_shop]
                    l+=1
                if l>6 and l<11:
                    image_load2_shop_menu+=[i]
                elif l==11:
                    image_load2_shop_menu+=[img_fleche_droite_shop]
                    l+=1
        l+=1
    image_load_shop_menu_bis=[image_load1_shop_menu]+[image_load2_shop_menu]

def det_chaine_mode_option():
    global chaine_mode_option
    chaine_mode_option=[]
    if lock_mode_normal>0:
        chaine_mode_option+=[0]
    if lock_mode_ouvert>0:
        chaine_mode_option+=[1]
    if lock_mode_piege>0:
        chaine_mode_option+=[2]
    if lock_mode_multiproie>0:
        chaine_mode_option+=[3]
    if lock_mode_multijoueur>0:
        chaine_mode_option+=[4]
    if lock_mode_special>0:
        chaine_mode_option+=[5]

def det_chaine_vitesse_option():
    global chaine_vitesse_option
    chaine_vitesse_option=[]
    if lock_vitesse_lent>0:
        chaine_vitesse_option+=[0]
    if lock_vitesse_normal>0:
        chaine_vitesse_option+=[1]
    if lock_vitesse_rapide>0:
        chaine_vitesse_option+=[2]
    if lock_vitesse_expert>0:
        chaine_vitesse_option+=[3]
    if lock_vitesse_acceleration>0:
        chaine_vitesse_option+=[4]

def det_chaine_theme_option():
    global chaine_theme_option
    chaine_theme_option=[]
    if lock_theme_ninja>0:
        chaine_theme_option+=[0]
    if lock_theme_negatif>0:
        chaine_theme_option+=[1]
    if lock_theme_ikeo>0:
        chaine_theme_option+=[2]
    if lock_theme_doume>0:
        chaine_theme_option+=[3]
    if lock_theme_deadpoule>0:
        chaine_theme_option+=[4]
    if lock_theme_epm>0:
        chaine_theme_option+=[5]
    if lock_theme_girly>0:
        chaine_theme_option+=[6]
    if lock_theme_dark_girly>0:
        chaine_theme_option+=[7]
    if lock_theme_zeldo>0:
        chaine_theme_option+=[8]

        
    
def new_pomme():
    global position_pomme,position_pomme_gold,validation_creation
    pick_x_y()
    l=randint(chance1_pomme_gen,chance2_pomme_gen)
    validation_creation=True
    if l>ligne_gold_not_gold:
        verification_validation_pomme_gold()
        if validation_creation==True:
            position_pomme_gold+=[[x_objet,y_objet]]
    if validation_creation==False or l<=ligne_gold_not_gold :
        position_pomme+=[[x_objet,y_objet]]

def new_bonus_vie():
    global position_bonus_vie,time_bonus_vie
    pick_x_y()
    position_bonus_vie+=[[x_objet,y_objet]]
    time_bonus_vie=randint(chance1_bonus_vie,chance2_bonus_vie)
    
def new_piece():
    global position_piece,time_spawn_piece
    pick_x_y()
    position_piece+=[[x_objet,y_objet]]
    time_spawn_piece=randint(chance1_piece,chance2_piece)

def new_coffre():
    global position_coffre,time_spawn_coffre
    pick_x_y()
    position_coffre+=[[x_objet,y_objet]]
    time_spawn_coffre=randint(chance1_coffre,chance2_coffre)

def new_malus_invers_touche():
    global position_invers_touche,time_spawn_invers_touche
    pick_x_y()
    position_invers_touche+=[[x_objet,y_objet]]
    time_spawn_invers_touche=randint(chance1_malus_invers_touche,chance2_malus_invers_touche)

def new_boost_piece():
    global position_boost_piece
    pick_x_y()
    position_boost_piece+=[[x_objet,y_objet]]

def new_boost_point():
    global position_boost_point
    pick_x_y()
    position_boost_point+=[[x_objet,y_objet]]
    
def new_bonus_plus_pts():
    global position_bonus_plus_pts,time_bonus_plus_pts
    pick_x_y()
    position_bonus_plus_pts+=[[x_objet,y_objet]]
    time_bonus_plus_pts=randint(chance1_bonus_plus_pts,chance2_bonus_plus_pts)

def new_malus_moins_pts():
    global position_malus_moins_pts,time_malus_moins_pts
    pick_x_y()
    position_malus_moins_pts+=[[x_objet,y_objet]]
    time_malus_moins_pts=randint(chance1_malus_moins_pts,chance2_malus_moins_pts)

def new_malus_div_pts():
    global position_malus_div_pts,time_malus_div_pts
    pick_x_y()
    position_malus_div_pts+=[[x_objet,y_objet]]
    time_malus_div_pts=randint(chance1_malus_div_pts,chance2_malus_div_pts)

def new_bonus_bouclier():
    global position_bonus_bouclier,time_bonus_bouclier,nbr_bouclier_partie
    pick_x_y()
    position_bonus_bouclier+=[[x_objet,y_objet]]
    time_bonus_bouclier=randint(chance1_bouclier,chance2_bouclier)
    nbr_bouclier_partie+=1

def draw_bonus_plus_pts():
    if bonus_plus_pts==True:
        load_img(img_plus_pts)
        place_on_terrain(position_bonus_plus_pts)

def draw_malus_moins_pts():
    if malus_moins_pts==True:
        load_img(img_moins_pts)
        place_on_terrain(position_malus_moins_pts)

def draw_malus_div_pts():
    if malus_div_pts==True:
        load_img(img_div_pts)
        place_on_terrain(position_malus_div_pts)

def draw_malus_invers_touche():
    if malus_invers_touche==True:
        load_img(img_invers_touche)
        place_on_terrain(position_invers_touche)

def draw_bonus_bouclier():
    if bonus_bouclier==True:
        load_img(img_bouclier)
        place_on_terrain(position_bonus_bouclier)
    

def draw_piece():
    load_img(img_piece)
    place_on_terrain(position_piece)

def draw_coffre():
    load_img(img_coffre)
    place_on_terrain(position_coffre)

def draw_boost_piece():
    load_img(img_boost_piece)
    place_on_terrain(position_boost_piece)

def draw_boost_point():
    if bonus_xpts==True:
        load_img(img_boost_point)
        place_on_terrain(position_boost_point)

def draw_bonus_vie():
    if bonus_vie==True:
        load_img(img_vie)
        place_on_terrain(position_bonus_vie)

def pick_x_y():
    global x_objet,y_objet
    restart=True
    while restart==True :
        restart=False
        x_objet=randint(0,19)
        y_objet=randint(1,19)
        if [x_objet,y_objet] in serpent1:
            restart=True
        if mode_piege==True:
            if [x_objet,y_objet] in position_piege:
                restart=True
        if [x_objet,y_objet] in position_pomme:
            restart=True
        if [x_objet,y_objet] in position_pomme_gold:
            restart=True
        if mode_multijoueur==True:
            if [x_objet,y_objet] in serpent2:
                restart=True
        if [x_objet,y_objet] in position_piece:
            restart=True
        if [x_objet,y_objet] in position_coffre:
            restart=True
        if [x_objet,y_objet] in position_boost_piece:
            restart=True
        if bonus_vie==True:
            if [x_objet,y_objet] in position_bonus_vie:
                restart=True
        if bonus_plus_pts==True:
            if [x_objet,y_objet] in position_bonus_plus_pts:
                restart=True
        if bonus_xpts==True:
            if [x_objet,y_objet] in position_boost_point:
                restart=True
        if bonus_bouclier==True:
            if [x_objet,y_objet] in position_bonus_bouclier:
                restart=True
        if malus_moins_pts==True:
            if [x_objet,y_objet] in position_malus_moins_pts:
                restart=True
        if malus_div_pts==True:
            if [x_objet,y_objet] in position_malus_div_pts:
                restart=True
        if malus_invers_touche==True:
            if [x_objet,y_objet] in position_invers_touche:
                restart=True
                
def load_img(a):
    global img
    img = pygame.image.load(a).convert_alpha()

def draw_pomme():
    load_img(img_pomme)
    place_on_terrain(position_pomme)

def draw_pomme_gold():
    load_img(img_pomme_gold)
    place_on_terrain(position_pomme_gold)
    
def place_on_terrain(a):
    for z in a:
        x=z[0]
        y=z[1]
        terrain_jeu_snake.blit(img, (x*25,y*25))

def place_tete_on_terrain(a):
    x=a[0]
    y=a[1]
    terrain_jeu_snake.blit(img, (x*25,y*25))

def identifier_joueur():
    global serpent
    if numero_joueur==1:
        serpent=serpent1.copy()
    elif numero_joueur==2:
        serpent=serpent2.copy()

def mort_serp2():
    global vie_serpent2
    vie_serpent2-=1
    if vie_serpent1>0:
        play_son_mort()

def maj_level_achat():
    global verif_init_choose,lock_vitesse_lent,lock_vitesse_normal,lock_vitesse_rapide,lock_vitesse_expert,lock_vitesse_acceleration,lock_mode_normal,lock_mode_ouvert,lock_mode_piege,lock_mode_multiproie,lock_mode_multijoueur,lock_mode_special,num_fen_shop,lock_theme_negatif,lock_theme_ninja,lock_theme_doume,lock_theme_ikeo,lock_theme_deadpoule,lock_theme_epm,lock_theme_girly,lock_theme_dark_girly,lock_theme_zeldo
    
    if num_fen_shop_plus==3:

        if cible_achat==1:
            lock_theme_ninja+=1
            if lock_theme_ninja==niveau_theme_ninja_maximum:
                num_fen_shop=2
                verif_init_choose=True
                
        if cible_achat==2:
            lock_theme_negatif+=1
            if lock_theme_negatif==niveau_theme_negatif_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==3:
            lock_theme_ikeo+=1
            if lock_theme_ikeo==niveau_theme_ikeo_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==4:
            lock_theme_doume+=1
            if lock_theme_doume==niveau_theme_doume_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==5:
            lock_theme_deadpoule+=1
            if lock_theme_deadpoule==niveau_theme_deadpoule_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==6:
            lock_theme_epm+=1
            if lock_theme_epm==niveau_theme_epm_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==7:
            lock_theme_girly+=1
            if lock_theme_girly==niveau_theme_girly_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==8:
            lock_theme_dark_girly+=1
            if lock_theme_dark_girly==niveau_theme_dark_girly_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==9:
            lock_theme_zeldo+=1
            if lock_theme_zeldo==niveau_theme_zeldo_maximum:
                num_fen_shop=2
                verif_init_choose=True
                
        sauvegarde_theme_lock()
        initialisation_theme_lock()
        actualise_img_theme_shop()

        
    if num_fen_shop_plus==4:

        if cible_achat==1:
            lock_mode_normal+=1
            if lock_mode_normal==niveau_mode_normal_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==2:
            lock_mode_ouvert+=1
            if lock_mode_ouvert==niveau_mode_ouvert_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==3:
            lock_mode_piege+=1
            if lock_mode_piege==niveau_mode_piege_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==4:
            lock_mode_multiproie+=1
            if lock_mode_multiproie==niveau_mode_multiproie_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==5:
            lock_mode_multijoueur+=1
            if lock_mode_multijoueur==niveau_mode_multijoueur_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==6:
            lock_mode_special+=1
            if lock_mode_special==niveau_mode_special_maximum:
                num_fen_shop=2
                verif_init_choose=True

        sauvegarde_mode_lock()
        initialisation_mode_lock()
        actualise_img_mode_shop()

    if num_fen_shop_plus==5:

        if cible_achat==1:
            lock_vitesse_lent+=1
            if lock_vitesse_lent==niveau_vitesse_lente_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==2:
            lock_vitesse_normal+=1
            if lock_vitesse_normal==niveau_vitesse_normal_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==3:
            lock_vitesse_rapide+=1
            if lock_vitesse_rapide==niveau_vitesse_rapide_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==4:
            lock_vitesse_expert+=1
            if lock_vitesse_expert==niveau_vitesse_expert_maximum:
                num_fen_shop=2
                verif_init_choose=True

        if cible_achat==5:
            lock_vitesse_acceleration+=1
            if lock_vitesse_acceleration==niveau_vitesse_acceleration_maximum:
                num_fen_shop=2
                verif_init_choose=True

        sauvegarde_vitesse_lock()
        initialisation_vitesse_lock()
        actualise_img_vitesse_shop()

                
def colision_pomme():
    global agrandir_serpent,gain_point,pomme_draw
    identifier_joueur()
    x=0
    for z in position_pomme:
        if serpent[0]==z:
            del position_pomme[x]
            play_son_pomme()
            gain_point=bonus_pomme_point
            score_up()
            agrandir_serpent=True
            pomme_draw+=1
        x+=1

def colision_plus_pts():
    global gain_point,position_bonus_plus_pts
    if bonus_plus_pts==True:
        identifier_joueur()
        x=0
        for z in position_bonus_plus_pts:
            if serpent[0] == z:
                del position_bonus_plus_pts[x]
                play_son_plus_pts()
                gain_point=bonus_plus_pts_point
                score_up()
            x+=1

def colision_moins_pts():
    global perte_point,position_malus_moins_pts
    if malus_moins_pts==True:
        identifier_joueur()
        x=0
        for z in position_malus_moins_pts:
            if serpent[0] == z:
                del position_malus_moins_pts[x]
                play_son_moins_pts()
                perte_point=malus_moins_pts_point
                score_down()
            x+=1

def colision_div_pts():
    global diviseur_point,position_malus_div_pts
    if malus_div_pts==True:
        identifier_joueur()
        x=0
        for z in position_malus_div_pts:
            if serpent[0] == z:
                del position_malus_div_pts[x]
                play_son_div_pts()
                diviseur_point=malus_div_point
                score_div()
            x+=1
        
def colision_vie():
    global gain_point,vie_serpent1,vie_serpent2,position_bonus_vie
    if bonus_vie==True:
        identifier_joueur()
        x=0
        for z in position_bonus_vie:
            if serpent[0] == z:
                del position_bonus_vie[x]
                play_son_vie()
                gain_point=bonus_coeur_pts
                score_up()
                if numero_joueur==1:
                    vie_serpent1+=bonus_vie_plus
                elif numero_joueur==2:
                    vie_serpent2+=bonus_vie_plus
            x+=1

def verification_validation_creation(a,b):
    global validation_creation
    validation_creation=True
    if len(a)>=b:
        validation_creation=False

def verification_validation_piece():
    global validation_creation
    if argent+((((len(position_piece))+1)*bonus_piece+(len(position_coffre))*bonus_coffre+(len(position_pomme_gold))*bonus_gold_pomme_piece)*multiplicateur_piece)>=limite_argent:
        validation_creation=False

def verification_validation_coffre():
    global validation_creation
    if argent+((((len(position_coffre))+1)*bonus_coffre+(len(position_piece))*bonus_piece+(len(position_pomme_gold))*bonus_gold_pomme_piece)*multiplicateur_piece)>=limite_argent:
        validation_creation=False

def verification_validation_bouclier():
    global validation_creation
    if nbr_bouclier_partie==max_bouclier_partie:
        validation_creation=False
    if bouclier_actif1==True:
        validation_creation=False
    if mode_multijoueur==True:
        if bouclier_actif2==True:
            validation_creation=False

def verification_validation_pomme_gold():
    global validation_creation
    if argent+(((len(position_piece))*bonus_piece+(len(position_coffre))*bonus_coffre+((len(position_pomme_gold))+1)*bonus_gold_pomme_piece)*multiplicateur_piece)>=limite_argent:
        validation_creation=False

def verification_validation_boost_argent(a,b):
    global validation_creation
    if argent+((len(position_piece))*bonus_piece+(len(position_coffre))*bonus_coffre+(len(position_pomme_gold))*bonus_gold_pomme_piece)*multiplicateur_piece*bonus_multiplicateur_piece>=limite_argent:
        validation_creation=False
    if a>=b:
        validation_creation=False

def verification_validation_boost_point(a,b):
    global validation_creation
    if a>=b:
        validation_creation=False
        
def colision_pomme_gold():
    global agrandir_serpent,gain_point,gain_piece,position_pomme_gold,pomme_draw
    identifier_joueur()
    x=0
    for z in position_pomme_gold:
        if serpent[0]==z:
            del position_pomme_gold[x]
            play_son_pomme_gold()
            gain_point=bonus_gold_pomme_point
            score_up()
            gain_piece=bonus_gold_pomme_piece
            argent_up()
            agrandir_serpent=True
            pomme_draw+=1
        x+=1
        
def colision_piece():
    global gain_piece,position_piece
    identifier_joueur()
    x=0
    for z in position_piece:
        if serpent[0]==z:
            del position_piece[x]
            play_son_piece()
            gain_piece=bonus_piece
            argent_up()
        x+=1

def colision_coffre():
    global gain_piece,position_coffre
    identifier_joueur()
    x=0
    for z in position_coffre:
        if serpent[0]==z:
            del position_coffre[x]
            play_son_coffre()
            gain_piece=bonus_coffre
            argent_up()
        x+=1

def colision_invers_touche():
    global position_invers_touche,invers_touche_j2,invers_touche_j1,compteur_time_invers_j1,compteur_time_invers_j2,time_invers_touche_actif_j2,time_invers_touche_actif_j1
    identifier_joueur()
    x=0
    for z in position_invers_touche:
        if serpent[0]==z:
            del position_invers_touche[x]
            play_son_invers_touche()
            if numero_joueur==1:
                invers_touche_j1=True
                compteur_time_invers_j1=0
                time_invers_touche_actif_j1=randint(time1_invers_touche_actif,time2_invers_touche_actif)
            elif numero_joueur==2:
                invers_touche_j2=True
                compteur_time_invers_j2=0
                time_invers_touche_actif_j2=randint(time1_invers_touche_actif,time2_invers_touche_actif)
        x+=1

def colision_boost_piece():
    global position_boost_piece,multiplicateur_piece,boost_piece,time_boost_piece_actif,compteur_time_boost_piece_actif
    identifier_joueur()
    x=0
    for z in position_boost_piece:
        if serpent[0]==z:
            del position_boost_piece[x]
            play_son_boost_piece()
            multiplicateur_piece+=bonus_multiplicateur_piece
            boost_piece=True
            compteur_time_boost_piece_actif=0
            time_boost_piece_actif=randint(time1_boost_piece_actif,time2_boost_piece_actif)
        x+=1

def impres_shop_img(s):
    q=0
    for h in range(1,nbr_shop_ligne+1):
        if len(s)==q:
            break
        for f in range(1,nbr_shop_colone+1):
            b=s[q]
            load_img(b)
            fill(img, pygame.Color (r_col,g_col,b_col))
            fond_shop.blit(img, ((espace_shop_x*f+taille_case_shop*(f-1)),(espace_shop_y*h+taille_case_shop*(h-1))))
            q+=1
            if len(s)==q:
                break
                
def colision_boost_point():
    global position_boost_point,multiplicateur_point1,multiplicateur_point2,boost_point1,boost_point2,time_boost_point_actif1,time_boost_point_actif2,compteur_time_boost_point_actif1,compteur_time_boost_point_actif2
    if bonus_xpts==True:
        identifier_joueur()
        x=0
        for z in position_boost_point:
            if serpent[0]==z:
                del position_boost_point[x]
                play_son_boost_point()
                if numero_joueur==1:
                    multiplicateur_point1+=bonus_multiplicateur_point
                    boost_point1=True
                    compteur_time_boost_point_actif1=0
                    time_boost_point_actif1=randint(time1_boost_point_actif,time2_boost_point_actif)
                elif numero_joueur==2:
                    multiplicateur_point2+=bonus_multiplicateur_point
                    boost_point2=True
                    compteur_time_boost_point_actif2=0
                    time_boost_point_actif2=randint(time1_boost_point_actif,time2_boost_point_actif)
            x+=1

def colision_bouciler():
    global position_bonus_bouclier,bouclier_actif1,bouclier_actif2
    if bonus_bouclier==True:
        identifier_joueur()
        x=0
        for z in position_bonus_bouclier:
            if serpent[0]==z:
                del position_bonus_bouclier[x]
                play_son_bouclier()
                if numero_joueur==1:
                    bouclier_actif1=True
                elif numero_joueur==2:
                    bouclier_actif2=True
            x+=1

def verification_serpent1_mort():
    global vie_serpent1,vie_perdu
    vie_serpent1-=1
    if mode_multijoueur==False:
        vie_perdu=True
        if vie_serpent1>=1:
            play_son_mort()
    else:
        if vie_serpent2>0:
            play_son_mort()
            
def avance_serpent1():
    if mode_ouvert==False:
        serpent1.insert(0,([(serpent1[0])[0]+direction[0],(serpent1[0])[1]+direction[1]]))
    else:
        serpent1.insert(0,([((serpent1[0])[0]+direction[0])%20,((serpent1[0])[1]+direction[1])%20]))

def avance_serpent2():
    if mode_ouvert==False:
        serpent2.insert(0,([(serpent2[0])[0]+direction2[0],(serpent2[0])[1]+direction2[1]]))
    else:
        serpent2.insert(0,([((serpent2[0])[0]+direction2[0])%20,((serpent2[0])[1]+direction2[1])%20]))

def fill(f, j):
    w, h = f.get_size()
    r, g, b, _ = j
    for x in range(w):
        for y in range(h):
            a = f.get_at((x, y))[3]
            f.set_at((x, y), pygame.Color(r, g, b, a))
            
def score_up():
    global txt2_1_titre,txt2_2_titre
    if numero_joueur==1:
        txt2_1_titre=str(gain_point*multiplicateur_point1+eval(txt2_1_titre))
    if numero_joueur==2:
        txt2_2_titre=str(gain_point*multiplicateur_point2+eval(txt2_2_titre))

def score_down():
    global txt2_1_titre,txt2_2_titre
    if numero_joueur==1:
        txt2_1_titre=str(eval(txt2_1_titre)-(perte_point*multiplicateur_point1))
        if eval(txt2_1_titre)<0:
            txt2_1_titre="0"
    if numero_joueur==2:
        txt2_2_titre=str(eval(txt2_2_titre)-(perte_point*multiplicateur_point2))
        if eval(txt2_2_titre)<0:
            txt2_2_titre="0"

def score_div():
    global txt2_1_titre,txt2_2_titre
    if numero_joueur==1:
        txt2_1_titre=str(int(round((eval(txt2_1_titre)/(diviseur_point*multiplicateur_point1)),0)))
    if numero_joueur==2:
        txt2_2_titre=str(int(round((eval(txt2_2_titre)/(diviseur_point*multiplicateur_point2)),0)))
            
def argent_up():
    global argent
    p=gain_piece*multiplicateur_piece
    argent=p+argent

#### son ############
def play_son(son):
    a=pygame.mixer.Sound(son)
    a.play()
    
def play_son_pomme():
    if num_case1==True:
        d=randint(0,2)
        if d==0:
            son_pomme=son_pomme1
        elif d==1:
            son_pomme=son_pomme2
        elif d==2:
            son_pomme=son_pomme3
        play_son(son_pomme)
        
def play_son_pomme_gold():
    if num_case1==True:
        d=randint(0,7)
        if d==0:
            son_pomme_or=son_pomme_or1
        elif d==1:
            son_pomme_or=son_pomme_or2
        elif d==2:
            son_pomme_or=son_pomme_or3
        elif d==3:
            son_pomme_or=son_pomme_or4
        elif d==4:
            son_pomme_or=son_pomme_or5
        elif d==5:
            son_pomme_or=son_pomme_or6
        elif d==6:
            son_pomme_or=son_pomme_or7
        elif d==7:
            son_pomme_or=son_pomme_or8
        play_son(son_pomme_or)

def play_son_mort():
    if num_case1==True:
        d=randint(0,14)
        if d==0:
            son_mort=son_mort1
        elif d==1:
            son_mort=son_mort2
        elif d==2:
            son_mort=son_mort3
        elif d==3:
            son_mort=son_mort4
        elif d==4:
            son_mort=son_mort5
        elif d==5:
            son_mort=son_mort6
        elif d==6:
            son_mort=son_mort7
        elif d==7:
            son_mort=son_mort8
        elif d==8:
            son_mort=son_mort9
        elif d==9:
            son_mort=son_mort10
        elif d==10:
            son_mort=son_mort11
        elif d==11:
            son_mort=son_mort12
        elif d==12:
            son_mort=son_mort13
        elif d==13:
            son_mort=son_mort14
        elif d==14:
            son_mort=son_mort15
        play_son(son_mort)

def play_son_perdu():
    if num_case1==True:
        d=randint(0,10)
        if d==0:
            son_perdu=son_perdu1
        if d==1:
            son_perdu=son_perdu2
        if d==2:
            son_perdu=son_perdu3
        if d==3:
            son_perdu=son_perdu4
        if d==4:
            son_perdu=son_perdu5
        if d==5:
            son_perdu=son_perdu6
        if d==6:
            son_perdu=son_perdu7
        if d==7:
            son_perdu=son_perdu8
        if d==8:
            son_perdu=son_perdu9
        if d==9:
            son_perdu=son_perdu10
        if d==10:
            son_perdu=son_perdu11
        play_son(son_perdu)

def play_son_vie():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_vie=son_vie1
        play_son(son_vie)

def play_son_invers_touche():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_invers_touche=son_invers_touche1
        play_son(son_invers_touche)
        
def play_son_bouclier():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_bouclier=son_bouclier1
        play_son(son_bouclier)

def play_son_bouclier_perdu():
    if num_case1==True:
        d=randint(0,3)
        if d==0:
            son_bouclier_perdu=son_bouclier_perdu1
        elif d==1:
            son_bouclier_perdu=son_bouclier_perdu2
        elif d==2:
            son_bouclier_perdu=son_bouclier_perdu3
        elif d==3:
            son_bouclier_perdu=son_bouclier_perdu4
        play_son(son_bouclier_perdu)
        
def play_son_plus_pts():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_plus_pts=son_plus_pts1
        play_son(son_plus_pts)

def play_son_moins_pts():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_moins_pts=son_moins_pts1
        play_son(son_moins_pts)

def play_son_div_pts():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_div_pts=son_div_pts1
        play_son(son_div_pts)

def play_son_piece():
    if num_case1==True:
        d=randint(0,8)
        if d==0:
            son_piece=son_piece1
        elif d==1:
            son_piece=son_piece2
        elif d==2:
            son_piece=son_piece3
        elif d==3:
            son_piece=son_piece4
        elif d==4:
            son_piece=son_piece5
        elif d==5:
            son_piece=son_piece6
        elif d==6:
            son_piece=son_piece7
        elif d==7:
            son_piece=son_piece8
        elif d==8:
            son_piece=son_piece9
        play_son(son_piece)

def play_son_coffre():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_coffre=son_coffre1
        play_son(son_coffre)
            
def play_son_boost_piece():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_boost_piece=son_boost_piece1
        play_son(son_boost_piece)

def play_son_boost_point():
    if num_case1==True:
        d=randint(0,0)
        if d==0:
            son_boost_point=son_boost_point1
        play_son(son_boost_point)

def play_son_start():
    if num_case1==True:
        d=randint(0,3)
        if d==0:
            son_start=son_start1
        elif d==1:
            son_start=son_start2
        elif d==2:
            son_start=son_start3
        elif d==3:
            son_start=son_start4
        play_son(son_start)

def declenche_choose_zone():
    global compteur_img_shop_menu,compteur_colonne_zone,compteur_ligne_zone
    compteur_img_shop_menu=0
    compteur_colonne_zone=1
    compteur_ligne_zone=1                    
    if len(image_load_shop_menu)-compteur_img_shop_menu>0:
        calcul_zone_shop_menu()
        choose_zone_shop_menu(image_load_shop_menu[compteur_img_shop_menu])
    if len(image_load_shop_menu)-compteur_img_shop_menu>0:
        calcul_zone_shop_menu()
        choose_zone_shop_menu(image_load_shop_menu[compteur_img_shop_menu])
    if len(image_load_shop_menu)-compteur_img_shop_menu>0:
        calcul_zone_shop_menu()
        choose_zone_shop_menu(image_load_shop_menu[compteur_img_shop_menu])
    if len(image_load_shop_menu)-compteur_img_shop_menu>0:
        calcul_zone_shop_menu()
        choose_zone_shop_menu(image_load_shop_menu[compteur_img_shop_menu])
    if len(image_load_shop_menu)-compteur_img_shop_menu>0:
        calcul_zone_shop_menu()
        choose_zone_shop_menu(image_load_shop_menu[compteur_img_shop_menu])
    if len(image_load_shop_menu)-compteur_img_shop_menu>0:
        calcul_zone_shop_menu()
        choose_zone_shop_menu(image_load_shop_menu[compteur_img_shop_menu])
                            
def initialiser_mode():
    global txt5_bouton,mode_multijoueur,mode_multiproie,mode_ouvert,mode_piege
    if num_txt5_bouton==0:
        txt5_bouton=txt5_0_bouton
        mode_ouvert=False
        mode_piege=False
        mode_multiproie=False
        mode_multijoueur=False
    elif num_txt5_bouton==1:
        txt5_bouton=txt5_1_bouton
        mode_ouvert=True
        mode_piege=False
        mode_multiproie=False
        mode_multijoueur=False
    elif num_txt5_bouton==2:
        txt5_bouton=txt5_2_bouton
        mode_piege=True
        mode_ouvert=False
        mode_multiproie=False
        mode_multijoueur=False
    elif num_txt5_bouton==3:
        txt5_bouton=txt5_3_bouton
        mode_multiproie=True
        mode_ouvert=False
        mode_piege=False
        mode_multijoueur=False
    elif num_txt5_bouton==4:
        txt5_bouton=txt5_4_bouton
        mode_multijoueur=True
        mode_multiproie=False
        mode_ouvert=False
        mode_piege=False
    elif num_txt5_bouton==5:
        txt5_bouton=txt5_5_bouton
        if num_case3==True:
            mode_ouvert=False
        else:
            mode_ouvert=True
        if num_case4==True:
            mode_piege=True
        else:
            mode_piege=False
        if num_case5==True:
            mode_multiproie=True
        else:
            mode_multiproie=False
        if num_case6==True:
            mode_multijoueur=True
        else:
            mode_multijoueur=False
    initialiser_bonus()
    initialiser_malus()

def initialiser_bonus():
    global bonus_vie,bonus_xpts,bonus_plus_pts,bonus_bouclier
    if num_case7==True:
        if num_txt5_bouton==5:
            if num_case9==True:
                bonus_xpts=True
            else:
                bonus_xpts=False
            if num_case10==True:
                bonus_plus_pts=True
            else:
                bonus_plus_pts=True
            if mode_multijoueur==False:
                if num_case11==True:
                    bonus_vie=True
                else:
                    bonus_vie=True
            else:
                bonus_vie=False
            if mode_piege==True:
                if num_case12==True:
                    bonus_bouclier=True
                else:
                    bonus_bouclier=False
            else:
                bonus_bouclier=False
            
            
        else:
        
            bonus_xpts=True
            bonus_plus_pts=True
            if mode_multijoueur==False:
                bonus_vie=True
            else:
                bonus_vie=False
            if mode_piege==True:
                bonus_bouclier=True
            else:
                bonus_bouclier=False
    else:
        bonus_xpts=False
        bonus_plus_pts=False
        bonus_vie=False
        bonus_bouclier=False

def initialiser_malus():
    global malus_div_pts,malus_moins_pts,malus_invers_touche
    if num_case8==True:
        if num_txt5_bouton==5:
            if num_case13==True:
                malus_div_pts=True
            else:
                malus_div_pts=False
            if num_case14==True:
                malus_moins_pts=True
            else:
                malus_moins_pts=False
            if num_case15==True:
                malus_invers_touche=True
            else:
                malus_invers_touche=False
        else:
            malus_div_pts=True
            malus_moins_pts=True
            malus_invers_touche=True
    else:
        malus_div_pts=False
        malus_moins_pts=False
        malus_invers_touche=False

def initialiser_mode_score():
    global score_txt_mode
    if num_score_txt_mode==0:
        score_txt_mode=txt5_0_bouton
    elif num_score_txt_mode==1:
        score_txt_mode=txt5_1_bouton
    elif num_score_txt_mode==2:
        score_txt_mode=txt5_2_bouton
    elif num_score_txt_mode==3:
        score_txt_mode=txt5_3_bouton
    elif num_score_txt_mode==4:
        score_txt_mode=txt5_4_bouton
    elif num_score_txt_mode==5:
        score_txt_mode=txt5_5_bouton

def initialiser_vitesse():
    global txt4_bouton
    if num_txt4_bouton==0:
        txt4_bouton=txt4_0_bouton
    elif num_txt4_bouton==1:
        txt4_bouton=txt4_1_bouton
    elif num_txt4_bouton==2:
        txt4_bouton=txt4_2_bouton
    elif num_txt4_bouton==3:
        txt4_bouton=txt4_3_bouton
    elif num_txt4_bouton==4:
        txt4_bouton=txt4_4_bouton

def init_vitesse():
    global fps,compt_fps
    if num_txt4_bouton==1:
        fps=fps3
    elif num_txt4_bouton==2:
        fps=fps2
    elif num_txt4_bouton==3:
        fps=fps5
    elif num_txt4_bouton==0:
        fps=fps4
    elif num_txt4_bouton==4:
        fps=fps4
        compt_fps=3
                            
def draw_serpent():
    global img
    for z in serpent1:
        x=z[0]
        y=z[1]
        pygame.draw.rect(terrain_jeu_snake,(color1),(x*25,y*25,25,25))
    load_img(tete)
    angle1=True
    if malus_invers_touche==True:
        if invers_touche_j1==True:
            angle1=True
        else:
            angle1=False
    if angle1==True:
        if direction==direction_d:
            angle_tete=-90
        elif direction==direction_g:
            angle_tete=90
        elif direction==direction_h:
            angle_tete=180
        elif direction==direction_b:
            angle_tete=0
    else:
        if direction==direction_d:
            angle_tete=90
        elif direction==direction_g:
            angle_tete=-90
        elif direction==direction_h:
            angle_tete=0
        elif direction==direction_b:
            angle_tete=180
    img=pygame.transform.rotate(img, angle_tete)
    m,p,o=color2
    fill(img, pygame.Color (m,p,o))
    place_tete_on_terrain(serpent1[0])
    
    


def draw_serpent2():
    global img
    for z in serpent2:
        x=z[0]
        y=z[1]
        pygame.draw.rect(terrain_jeu_snake,(color1),(x*25,y*25,25,25))
    load_img(tete)
    angle1=True
    if malus_invers_touche==True:
        if invers_touche_j2==True:
            angle2=True
        else:
            angle2=False
    if angle2==True:
        if direction2==direction_d:
            angle_tete=-90
        elif direction2==direction_g:
            angle_tete=90
        elif direction2==direction_h:
            angle_tete=0
        elif direction2==direction_b:
            angle_tete=180
    else:
        if direction2==direction_d:
            angle_tete=90
        elif direction2==direction_g:
            angle_tete=-90
        elif direction2==direction_h:
            angle_tete=180
        elif direction2==direction_b:
            angle_tete=0   
    img=pygame.transform.rotate(img, angle_tete)
    m,p,o=color2
    fill(img, pygame.Color (m,p,o))
    place_tete_on_terrain(serpent2[0])
        
def draw_piege():
    if mode_piege==True: 
        for z in position_piege:
            x=z[0]
            y=z[1]
            pygame.draw.rect(terrain_jeu_snake,(color1),(x*25,y*25,25,25))
    
def draw_vie():
    vie = pygame.image.load(img_vie).convert_alpha()
    fond.blit(vie, ((espace_vie+nbr_vie_draw*30),y_position_coeur))

def restart_position_serpent():
    global serpent1,direction,direction_p
    ancien_serpent=serpent.copy()
    serpent1=[]
    direction=direction_admin
    for nombre_case_corp in range(0,len(ancien_serpent)):
        serpent1+=[((-1-nombre_case_corp),0)]
    direction_p=direction
    init_vitesse()
    if malus_invers_touche==True:
        invers_touche_j1=False
    if bonus_vie==True:
        compt_bonus_vie=0

def init_record():
    global txt_record1, txt_record2, txt_record3, txt_record4, txt_record5
    if score_txt_mode==txt5_0_bouton:
        txt_record1=record_normale_1
        txt_record2=record_normale_2
        txt_record3=record_normale_3
        txt_record4=record_normale_4
        txt_record5=record_normale_5
    elif score_txt_mode==txt5_1_bouton:
        txt_record1=record_ouvert_1
        txt_record2=record_ouvert_2
        txt_record3=record_ouvert_3
        txt_record4=record_ouvert_4
        txt_record5=record_ouvert_5
    elif score_txt_mode==txt5_2_bouton:
        txt_record1=record_piege_1
        txt_record2=record_piege_2
        txt_record3=record_piege_3
        txt_record4=record_piege_4
        txt_record5=record_piege_5
    elif score_txt_mode==txt5_3_bouton:
        txt_record1=record_multiproie_1
        txt_record2=record_multiproie_2
        txt_record3=record_multiproie_3
        txt_record4=record_multiproie_4
        txt_record5=record_multiproie_5
    elif score_txt_mode==txt5_4_bouton:
        txt_record1=record_multijoueur_1
        txt_record2=record_multijoueur_2
        txt_record3=record_multijoueur_3
        txt_record4=record_multijoueur_4
        txt_record5=record_multijoueur_5
    elif score_txt_mode==txt5_5_bouton:
        txt_record1=record_special_1
        txt_record2=record_special_2
        txt_record3=record_special_3
        txt_record4=record_special_4
        txt_record5=record_special_5

def def_theme():
    global num_txt9_bouton ,color1,color2,color3,play_musique,musique
    if len(chaine_theme_option)>1:
        pygame.mixer.music.fadeout(fondu)
        play_musique=False
    if num_txt9_bouton==0:
        color1=col1
        color2=col2
        musique=musique1
    elif num_txt9_bouton==1:
        color1=col2
        color2=col1
        musique=musique2
    elif num_txt9_bouton==2:
        color1=col3
        color2=col4
        musique=musique3
    elif num_txt9_bouton==3:
        color1=col5
        color2=col2
        musique=musique4
    elif num_txt9_bouton==4:
        color1=col5
        color2=col1
        musique=musique5
    elif num_txt9_bouton==5:
        color1=col1
        color2=col4
        musique=musique6
    elif num_txt9_bouton==6:
        color1=col6
        color2=col1
        musique=musique7
    elif num_txt9_bouton==7:
        color1=col1
        color2=col6
        musique=musique8
    elif num_txt9_bouton==8:
        color1=col4
        color2=col7
        musique=musique9

def init_all_lock():
    initialisation_mode_lock()
    initialisation_vitesse_lock()
    initialisation_theme_lock()
    
def page_option1():
    global num_fen_option
    init_all_lock()
    num_fen_option=0
    
def sauvegarde_partie():
    if num_case1==True:
        if action_quitt==False:
            play_son_perdu()

    #choix de la liste des records
    list_new_record=[]
    score_parti=txt2_1_titre
    if num_txt5_bouton==0:
        list_ancien_record=[record_normale_1]+[record_normale_2]+[record_normale_3]+[record_normale_4]+[record_normale_5]
        src_score=src_record_normal
    elif num_txt5_bouton==1:
        list_ancien_record=[record_ouvert_1]+[record_ouvert_2]+[record_ouvert_3]+[record_ouvert_4]+[record_ouvert_5]
        src_score=src_record_ouvert
    elif num_txt5_bouton==2:
        list_ancien_record=[record_piege_1]+[record_piege_2]+[record_piege_3]+[record_piege_4]+[record_piege_5]
        src_score=src_record_piege
    elif num_txt5_bouton==3:
        list_ancien_record=[record_multiproie_1]+[record_multiproie_2]+[record_multiproie_3]+[record_multiproie_4]+[record_multiproie_5]
        src_score=src_record_multiproie
    elif num_txt5_bouton==4:
        list_ancien_record=[record_multijoueur_1]+[record_multijoueur_2]+[record_multijoueur_3]+[record_multijoueur_4]+[record_multijoueur_5]
        src_score=src_record_multijoueur
    elif num_txt5_bouton==5:
        list_ancien_record=[record_special_1]+[record_special_2]+[record_special_3]+[record_special_4]+[record_special_5]
        src_score=src_record_special
    #reorganisation du score (si le joueur 1 a battue un record)
    for ancien_record in list_ancien_record:
        if int(ancien_record)< int(score_parti) and not score_parti in list_new_record:
            list_new_record+=[score_parti]
            score_parti=ancien_record
        else:
            list_new_record+=[ancien_record]

    #reorganisation du score (si le joueur 2 a battue un record)
    if mode_multijoueur==True:
        list_ancien_record=list_new_record.copy()
        list_new_record=[]
        score_parti=txt2_2_titre
        for ancien_record in list_ancien_record:
            if int(ancien_record)< int(score_parti) and not score_parti in list_new_record:
                list_new_record+=[score_parti]
                score_parti=ancien_record
            else:
                list_new_record+=[ancien_record]
                
    #enregistrement de la nouvelle liste des records
    score_fichier = open(src_score, "w")
    score_record=str(list_new_record[0])+"\n"+str(list_new_record[1])+"\n"+str(list_new_record[2])+"\n"+str(list_new_record[3])+"\n"+str(list_new_record[4])+"\n"
    score_fichier.write(score_record)
    score_fichier.close()

def fenetre_pres_achat(g,t,c,w):
    global description_achat,prix_achat,niveau_achat_actuel,niveau_achat_maximum,num_fen_shop
    description_achat=g
    prix_achat=t
    niveau_achat_actuel=c
    niveau_achat_maximum=w
    num_fen_shop=3
    
def actualise_img_vitesse_shop():
    global r_col,g_col,b_col,verif_init_choose,num_page_shop_bis,reinit_page
    if reinit_page==True:
        num_page_shop_bis=0
    r_col,g_col,b_col=color1
    det_chaine_img_vitesse_option_bis ()
    verif_init_choose=True
    reinit_page=True
    
def actualise_img_mode_shop():
    global r_col,g_col,b_col,verif_init_choose,num_page_shop_bis,reinit_page
    if reinit_page==True:
        num_page_shop_bis=0
    r_col,g_col,b_col=color1
    det_chaine_img_mode_option_bis ()
    verif_init_choose=True
    reinit_page=True

def actualise_img_theme_shop():
    global r_col,g_col,b_col,verif_init_choose,num_page_shop_bis,reinit_page
    if reinit_page==True:
        num_page_shop_bis=0
    r_col,g_col,b_col=color1
    det_chaine_img_theme_option_bis ()
    verif_init_choose=True
    reinit_page=True

def actualise_img_objet_shop():
    global r_col,g_col,b_col,image_load_shop_menu,verif_init_choose,num_page_shop_bis
    num_page_shop_bis=0
    image_load1_shop_menu=[]
    image_load_shop_menu_bis=[image_load1_shop_menu]
    r_col,g_col,b_col=color1
    verif_init_choose=True

def actualise_img_skin_shop():
    global r_col,g_col,b_col,image_load_shop_menu,verif_init_choose
    num_page_shop_bis=0
    image_load1_shop_menu=[]
    image_load_shop_menu_bis=[image_load1_shop_menu]
    r_col,g_col,b_col=color1
    verif_init_choose=True

def actualise_img_menu_shop():
    global r_col,g_col,b_col,image_load_shop_menu,image_load1_shop_menu,verif_init_choose,image_load_shop_menu_bis,num_page_shop_bis
    num_page_shop_bis=0
    image_load1_shop_menu=img_objet_shop,img_shop_skin,img_theme_shop,img_mode_shop,img_vitesse_shop
    image_load_shop_menu=image_load1_shop_menu
    image_load_shop_menu_bis=[image_load1_shop_menu]
    r_col,g_col,b_col=color1
    verif_init_choose=True
    
def init_score_record():
    global record_normale_1,record_normale_2,record_normale_3,record_normale_4,record_normale_5,record_ouvert_1,record_ouvert_2,record_ouvert_3,record_ouvert_4,record_ouvert_5,record_piege_1,record_piege_2,record_piege_3,record_piege_4,record_piege_5,record_multiproie_1,record_multiproie_2,record_multiproie_3,record_multiproie_4,record_multiproie_5,record_multijoueur_1,record_multijoueur_2,record_multijoueur_3,record_multijoueur_4,record_multijoueur_5,record_special_1,record_special_2,record_special_3,record_special_4,record_special_5
    #initialisation score
    #normal
    record_fichier = open(src_record_normal, "r")        
    contenu =record_fichier.readlines()
    record_normale_1=(contenu[0])[:-1]
    record_normale_2=(contenu[1])[:-1]
    record_normale_3=(contenu[2])[:-1]
    record_normale_4=(contenu[3])[:-1]
    record_normale_5=(contenu[4])[:-1]
    record_fichier.close()

    #ouvert
    record_fichier = open(src_record_ouvert, "r")        
    contenu =record_fichier.readlines()
    record_ouvert_1=(contenu[0])[:-1]
    record_ouvert_2=(contenu[1])[:-1]
    record_ouvert_3=(contenu[2])[:-1]
    record_ouvert_4=(contenu[3])[:-1]
    record_ouvert_5=(contenu[4])[:-1]
    record_fichier.close()

    #piege
    record_fichier = open(src_record_piege, "r")        
    contenu =record_fichier.readlines()
    record_piege_1=(contenu[0])[:-1]
    record_piege_2=(contenu[1])[:-1]
    record_piege_3=(contenu[2])[:-1]
    record_piege_4=(contenu[3])[:-1]
    record_piege_5=(contenu[4])[:-1]
    record_fichier.close()

    #multiproie
    record_fichier = open(src_record_multiproie, "r")        
    contenu =record_fichier.readlines()
    record_multiproie_1=(contenu[0])[:-1]
    record_multiproie_2=(contenu[1])[:-1]
    record_multiproie_3=(contenu[2])[:-1]
    record_multiproie_4=(contenu[3])[:-1]
    record_multiproie_5=(contenu[4])[:-1]
    record_fichier.close()

    #multijoueur
    record_fichier = open(src_record_multijoueur, "r")        
    contenu =record_fichier.readlines()
    record_multijoueur_1=(contenu[0])[:-1]
    record_multijoueur_2=(contenu[1])[:-1]
    record_multijoueur_3=(contenu[2])[:-1]
    record_multijoueur_4=(contenu[3])[:-1]
    record_multijoueur_5=(contenu[4])[:-1]
    record_fichier.close()

    #special
    record_fichier = open(src_record_special, "r")        
    contenu =record_fichier.readlines()
    record_special_1=(contenu[0])[:-1]
    record_special_2=(contenu[1])[:-1]
    record_special_3=(contenu[2])[:-1]
    record_special_4=(contenu[3])[:-1]
    record_special_5=(contenu[4])[:-1]
    record_fichier.close()

def initialisation_mode_lock():
    global lock_mode_normal,lock_mode_ouvert,lock_mode_piege,lock_mode_multiproie,lock_mode_multijoueur,lock_mode_special
    init_fichier = open(src_lock_mode, "r")        
    contenu =init_fichier.readlines()


    lock_mode_normal=int((contenu[0])[:-1])
    lock_mode_ouvert=int((contenu[1])[:-1])
    lock_mode_piege=int((contenu[2])[:-1])
    lock_mode_multiproie=int((contenu[3])[:-1])
    lock_mode_multijoueur=int((contenu[4])[:-1])
    lock_mode_special=int((contenu[5])[:-1])

    init_fichier.close()
    
    det_chaine_mode_option()

def sauvegarde_mode_lock():
    init_fichier = open(src_lock_mode, "w")
    sauvegarde_txt=str(lock_mode_normal)+"\n"+str(lock_mode_ouvert)+"\n"+str(lock_mode_piege)+"\n"+str(lock_mode_multiproie)+"\n"+str(lock_mode_multijoueur)+"\n"+str(lock_mode_special)+"\n"
    init_fichier.write(sauvegarde_txt)
    init_fichier.close()

def initialisation_vitesse_lock():
    global lock_vitesse_lent,lock_vitesse_normal,lock_vitesse_rapide,lock_vitesse_expert,lock_vitesse_acceleration
    init_fichier = open(src_lock_vitesse, "r")        
    contenu =init_fichier.readlines()


    lock_vitesse_lent=int((contenu[0])[:-1])
    lock_vitesse_normal=int((contenu[1])[:-1])
    lock_vitesse_rapide=int((contenu[2])[:-1])
    lock_vitesse_expert=int((contenu[3])[:-1])
    lock_vitesse_acceleration=int((contenu[4])[:-1])

    init_fichier.close()

    det_chaine_vitesse_option()

def sauvegarde_vitesse_lock():
    init_fichier = open(src_lock_vitesse, "w")
    sauvegarde_txt=str(lock_vitesse_lent)+"\n"+str(lock_vitesse_normal)+"\n"+str(lock_vitesse_rapide)+"\n"+str(lock_vitesse_expert)+"\n"+str(lock_vitesse_acceleration)+"\n"
    init_fichier.write(sauvegarde_txt)
    init_fichier.close()

def initialisation_theme_lock():
    global lock_theme_ninja,lock_theme_negatif,lock_theme_ikeo,lock_theme_doume,lock_theme_deadpoule,lock_theme_epm,lock_theme_girly,lock_theme_dark_girly,lock_theme_zeldo
    init_fichier = open(src_lock_theme, "r")        
    contenu =init_fichier.readlines()


    lock_theme_ninja=int((contenu[0])[:-1])
    lock_theme_negatif=int((contenu[1])[:-1])
    lock_theme_ikeo=int((contenu[2])[:-1])
    lock_theme_doume=int((contenu[3])[:-1])
    lock_theme_deadpoule=int((contenu[4])[:-1])
    lock_theme_epm=int((contenu[5])[:-1])
    lock_theme_girly=int((contenu[6])[:-1])
    lock_theme_dark_girly=int((contenu[7])[:-1])
    lock_theme_zeldo=int((contenu[8])[:-1])

    init_fichier.close()

    det_chaine_theme_option()

def sauvegarde_theme_lock():
    init_fichier = open(src_lock_theme, "w")
    sauvegarde_txt=str(lock_theme_ninja)+"\n"+str(lock_theme_negatif)+"\n"+str(lock_theme_ikeo)+"\n"+str(lock_theme_doume)+"\n"+str(lock_theme_deadpoule)+"\n"+str(lock_theme_epm)+"\n"+str(lock_theme_girly)+"\n"+str(lock_theme_dark_girly)+"\n"+str(lock_theme_zeldo)+"\n"
    init_fichier.write(sauvegarde_txt)
    init_fichier.close()

def calcul_zone_shop_menu():
    global compteur_ligne_zone,compteur_colonne_zone,zone_shop_menu_x,zone_shop_menu_y
    p=True
    while p==True:
        if compteur_colonne_zone<=nbr_shop_colone:
            zone_shop_menu_x=(espace_shop_x*compteur_colonne_zone+taille_case_shop*(compteur_colonne_zone-1))
            zone_shop_menu_y=(espace_shop_y*compteur_ligne_zone+taille_case_shop*(compteur_ligne_zone-1))+position_fond_shop[1]
            p=False
            compteur_colonne_zone+=1
        else:
            compteur_colonne_zone=1
            compteur_ligne_zone+=1
    
    

    

    
def choose_zone_shop_menu(a):
    global zone_theme_zeldo_x,zone_theme_zeldo_y,zone_theme_dark_girly_x,zone_theme_dark_girly_y,zone_theme_girly_x,zone_theme_girly_y,zone_theme_epm_x,zone_theme_epm_y,zone_theme_deadpoule_x,zone_theme_deadpoule_y,zone_theme_doume_x,zone_theme_doume_y,zone_theme_ikeo_x,zone_theme_ikeo_y,zone_theme_negatif_x,zone_theme_negatif_y,zone_theme_ninja_x,zone_theme_ninja_y,zone_mode_special_x,zone_mode_special_y,zone_mode_multijoueur_x,zone_mode_multijoueur_y,zone_mode_multiproie_x,zone_mode_multiproie_y,zone_mode_piege_x,zone_mode_piege_y,zone_mode_ouvert_x,zone_mode_ouvert_y,compteur_img_shop_menu,zone_mode_normal_x,zone_mode_normal_y,zone_fleche_droite_x,zone_fleche_droite_y,zone_fleche_gauche_x,zone_fleche_gauche_y,zone_vitesse_acceleration_x,zone_vitesse_acceleration_y,zone_vitesse_expert_x,zone_vitesse_expert_y,zone_vitesse_normal_x,zone_vitesse_normal_y,zone_vitesse_lent_x,zone_vitesse_rapide_x,zone_vitesse_rapide_y,zone_vitesse_lent_y,zone_vitesse_menu_x,zone_vitesse_menu_y,zone_skin_menu_x,zone_skin_menu_y,zone_mode_menu_x,zone_mode_menu_y,zone_objet_menu_x,zone_objet_menu_y,zone_theme_menu_x,zone_theme_menu_y
    if num_fen_shop==1:
        if a==img_shop_skin:
            zone_skin_menu_x=zone_shop_menu_x
            zone_skin_menu_y=zone_shop_menu_y
        elif a==img_mode_shop:
            zone_mode_menu_x=zone_shop_menu_x
            zone_mode_menu_y=zone_shop_menu_y
        elif a==img_objet_shop:
            zone_objet_menu_x=zone_shop_menu_x
            zone_objet_menu_y=zone_shop_menu_y
        elif a==img_theme_shop:
            zone_theme_menu_x=zone_shop_menu_x
            zone_theme_menu_y=zone_shop_menu_y
        elif a==img_vitesse_shop:
            zone_vitesse_menu_x=zone_shop_menu_x
            zone_vitesse_menu_y=zone_shop_menu_y
    elif num_fen_shop==2:

        if num_fen_shop_plus==3:
            if a==img_theme_ninja_shop:
                zone_theme_ninja_x=zone_shop_menu_x
                zone_theme_ninja_y=zone_shop_menu_y
            if a==img_theme_negatif_shop:
                zone_theme_negatif_x=zone_shop_menu_x
                zone_theme_negatif_y=zone_shop_menu_y
            if a==img_theme_ikeo_shop:
                zone_theme_ikeo_x=zone_shop_menu_x
                zone_theme_ikeo_y=zone_shop_menu_y
            if a==img_theme_doume_shop:
                zone_theme_doume_x=zone_shop_menu_x
                zone_theme_doume_y=zone_shop_menu_y
            if a==img_theme_deadpoule_shop:
                zone_theme_deadpoule_x=zone_shop_menu_x
                zone_theme_deadpoule_y=zone_shop_menu_y
            if a==img_theme_epm_shop:
                zone_theme_epm_x=zone_shop_menu_x
                zone_theme_epm_y=zone_shop_menu_y
            if a==img_theme_girly_shop:
                zone_theme_girly_x=zone_shop_menu_x
                zone_theme_girly_y=zone_shop_menu_y
            if a==img_theme_dark_girly_shop:
                zone_theme_dark_girly_x=zone_shop_menu_x
                zone_theme_dark_girly_y=zone_shop_menu_y
            if a==img_theme_zeldo_shop:
                zone_theme_zeldo_x=zone_shop_menu_x
                zone_theme_zeldo_y=zone_shop_menu_y
        
        if num_fen_shop_plus==4:
            if a==img_mode_normal_shop:
                zone_mode_normal_x=zone_shop_menu_x
                zone_mode_normal_y=zone_shop_menu_y
            if a==img_mode_ouvert_shop:
                zone_mode_ouvert_x=zone_shop_menu_x
                zone_mode_ouvert_y=zone_shop_menu_y
            if a==img_mode_piege_shop:
                zone_mode_piege_x=zone_shop_menu_x
                zone_mode_piege_y=zone_shop_menu_y
            if a==img_mode_multiproie_shop:
                zone_mode_multiproie_x=zone_shop_menu_x
                zone_mode_multiproie_y=zone_shop_menu_y
            if a==img_mode_multijoueur_shop:
                zone_mode_multijoueur_x=zone_shop_menu_x
                zone_mode_multijoueur_y=zone_shop_menu_y
            if a==img_mode_special_shop:
                zone_mode_special_x=zone_shop_menu_x
                zone_mode_special_y=zone_shop_menu_y

                
        if num_fen_shop_plus==5:
            if a==img_vitesse_lent_shop:
                zone_vitesse_lent_x=zone_shop_menu_x
                zone_vitesse_lent_y=zone_shop_menu_y
            elif a==img_vitesse_normal_shop:
                zone_vitesse_normal_x=zone_shop_menu_x
                zone_vitesse_normal_y=zone_shop_menu_y
            elif a==img_vitesse_rapide_shop:
                zone_vitesse_rapide_x=zone_shop_menu_x
                zone_vitesse_rapide_y=zone_shop_menu_y
            elif a==img_vitesse_expert_shop:
                zone_vitesse_expert_x=zone_shop_menu_x
                zone_vitesse_expert_y=zone_shop_menu_y
            elif a==img_vitesse_acceleration_shop:
                zone_vitesse_acceleration_x=zone_shop_menu_x
                zone_vitesse_acceleration_y=zone_shop_menu_y
    if a==img_fleche_gauche_shop:
        zone_fleche_gauche_x=zone_shop_menu_x
        zone_fleche_gauche_y=zone_shop_menu_y
    if a==img_fleche_droite_shop:
        zone_fleche_droite_x=zone_shop_menu_x
        zone_fleche_droite_y=zone_shop_menu_y
        
    compteur_img_shop_menu+=1
    
#creation boucle infini
continuer = True
init_score_record()
initialiser_vitesse()
initialiser_mode()
play_musique=False
initialisation_theme_lock()
def_theme()

while continuer==True:
    pygame.time.Clock().tick(fps)
    if continuer==True:

        #fondu intro##############################
        if intro_fondu==True:
            if moment_fondu==True:
                logo_imp=pygame.image.load(logo).convert_alpha()
                fond=pygame.Surface(taille_fond)
                fond.fill((color1))
                if num_case1==True:
                    son_p_intro=pygame.mixer.Sound(son_intro)
                    son_p_intro.play()
                #apparition
                for i in range(255,0,-4):
                    fond.blit(logo_imp,position_logo)
                    fond.fill((i,i,i),special_flags=BLEND_RGB_SUB)
                    pygame.time.wait(temps_pause_image_fondu)
                    pygame.display.flip()
                    fenetre.blit(fond,position_fond)
                pygame.time.wait(temps_pause_fondu)
                
                #disparition
                for i in range(0,255,4):
                    fond.fill(0x040404,special_flags=BLEND_RGB_SUB)
                    pygame.time.wait(temps_pause_image_fondu)
                    pygame.display.flip()
                    fenetre.blit(fond,position_fond)
                pygame.time.wait(temps_pause_fondu)
                intro_fondu=False

                logo_imp_simon=pygame.image.load(logo_simon).convert_alpha()
                if num_case1==True:
                    son_p_intro_simon=pygame.mixer.Sound(son_intro_simon)
                    son_p_intro_simon.play()
                #apparition
                for i in range(255,0,-4):
                    fond.blit(logo_imp_simon,position_logo)
                    fond.fill((i,i,i),special_flags=BLEND_RGB_SUB)
                    pygame.time.wait(temps_pause_image_fondu)
                    pygame.display.flip()
                    fenetre.blit(fond,position_fond)
                pygame.time.wait(temps_pause_fondu)
                
                #disparition
                for i in range(0,255,4):
                    fond.fill(0x040404,special_flags=BLEND_RGB_SUB)
                    pygame.time.wait(temps_pause_image_fondu)
                    pygame.display.flip()
                    fenetre.blit(fond,position_fond)
                pygame.time.wait(temps_pause_fondu)
                intro_fondu=False
                
                moment_fondu=False
        else:
            moment_fondu=False

        if moment_fondu==False:
            #musique#############################
            if num_case2==True:
                if play_musique==False:
                    pygame.mixer.music.load(musique)
                    pygame.mixer.music.set_volume(volume)
                    pygame.mixer.music.play(loops=-1)
                    play_musique=True
            else:
                pygame.mixer.music.fadeout(fondu)
                play_musique=False



        #si evenement
        for event in pygame.event.get():

            #evenement quitter
            if event.type == QUIT:
                if num_case2==True:
                    action_quitt=True
                    pygame.mixer.music.fadeout(fondu)
                    pygame.time.wait(fondu)
                if number_create_fen==5:
                    sauvegarde_partie()
                pygame.quit()
                init_fichier = open(src_sauvegarde, "w")
                sauvegarde_txt=str(num_txt4_bouton)+"\n"+str(num_txt5_bouton)+"\n"+str(num_txt9_bouton)+"\n"+str(int(num_case1))+"\n"+str(int(num_case2))+"\n"+str(num_score_txt_mode)+"\n"+str(int(num_case3))+"\n"+str(int(num_case4))+"\n"+str(int(num_case5))+"\n"+str(int(num_case6))+"\n"+str(int(num_case7))+"\n"+str(int(num_case8))+"\n"+str(int(num_case9))+"\n"+str(int(num_case10))+"\n"+str(int(num_case11))+"\n"+str(int(num_case12))+"\n"+str(argent)+"\n"+str(int(num_case13))+"\n"+str(int(num_case14))+"\n"+str(int(num_case15))+"\n"
                init_fichier.write(sauvegarde_txt)
                init_fichier.close()
                continuer = False

            #autre evenement
            if moment_fondu==False:

                #son##################################
                if num_case1==True:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        son_p_clic=pygame.mixer.Sound(son_clic)
                        son_p_clic.play()
                    if number_create_fen==5:
                        if event.type == MOUSEBUTTONDOWN and event.button == 3:
                            son_p_clic=pygame.mixer.Sound(son_clic)
                            son_p_clic.play()


                #page 2#############################
                if number_create_fen==2:
                    #bouton jouer clic
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone1_x1 and event.pos[0] < zone1_x2 and event.pos[1] > zone1_y1 and event.pos[1] < zone1_y2:
                        number_create_fen=5
                        stop_game_over=False
                        pause=False

                        if mode_piege==True:
                            position_piege=[]
                            for z in range(0,nbr_piege):
                                xmmm=randint(0,19)
                                ymmm=randint(1,19)
                                position_piege+=[[xmmm,ymmm]]
                            position_bonus_bouclier=[]
                            compt_spawn_bouclier=0
                            time_bonus_bouclier=randint(chance1_bouclier,chance2_bouclier)
                            nbr_bouclier_partie=0
                            bouclier_actif1=False
                            
                        if bonus_xpts==True:
                            position_boost_point=[]
                            compt_spawn_boost_point=0
                            boost_point1=False
                            
                        if mode_multiproie==True:
                            pomme_draw_time=True
                            comp_app_pomme_multi=0
                            time_spawn_pomme=randint(chance1_pomme_plus,chance2_pomme_plus)
                            
                        if bonus_plus_pts==True:
                            position_bonus_plus_pts=[]
                            compt_spawn_plus_pts=0
                            time_bonus_plus_pts=randint(chance1_bonus_plus_pts,chance2_bonus_plus_pts)

                        if malus_moins_pts==True:
                            position_malus_moins_pts=[]
                            compt_spawn_moins_pts=0
                            time_malus_moins_pts=randint(chance1_malus_moins_pts,chance2_malus_moins_pts)

                        if malus_div_pts==True:
                            position_malus_div_pts=[]
                            compt_spawn_div_pts=0
                            time_malus_div_pts=randint(chance1_malus_div_pts,chance2_malus_div_pts)

                        if malus_invers_touche==True:
                            position_invers_touche=[]
                            compt_spawn_invers_touche=0
                            time_spawn_invers_touche=randint(chance1_malus_invers_touche,chance2_malus_invers_touche)
                            invers_touche_j1=False
                            
                        multiplicateur_point1=multiplicateur_point_admin
                        multiplicateur_piece=multiplicateur_piece_admin
                        
                        position_pomme=[]
                        position_pomme_gold=[]
                        position_piece=[]
                        compt_spawn_piece=0
                        time_spawn_piece=randint(chance1_piece,chance2_piece)
                        position_coffre=[]
                        compt_spawn_coffre=0
                        time_spawn_coffre=randint(chance1_coffre,chance2_coffre)
                        position_boost_piece=[]
                        compt_spawn_boost_piece=0
                        boost_piece=False
                        
                        serpent1=serpent_admin.copy()
                        direction_p=direction_admin
                        direction=direction_admin
                        vie_serpent1=vie_serpent1_admin
                        txt2_1_titre=txt2_1_titre_base
                        pommej1=0
                        
                        
                        
                        
                        if mode_multijoueur==True:
                            init_clean1=True
                            init_clean2=True
                            pomme_draw=2
                            multiplicateur_point2=multiplicateur_point_admin

                            if bonus_xpts==True:
                                boost_point2=False

                            if bonus_bouclier==True:
                                bouclier_actif2=False

                            if malus_invers_touche==True:
                                invers_touche_j2=False
                                
                            serpent2=serpent2_admin.copy()
                            direction_p2=direction_admin2
                            direction2=direction_admin2
                            vie_serpent2=vie_serpent2_admin
                            txt2_2_titre=txt2_2_titre_base
                            pommej2=0
                            
                        else:
                            pomme_draw=1
                            vie_perdu=False
                            
                            if bonus_vie==True:
                                position_bonus_vie=[]
                                compt_bonus_vie=0
                                time_bonus_vie=randint(chance1_bonus_vie,chance2_bonus_vie)

                        play_son_start()
                        
                        init_vitesse()
                    #bouton score clic
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone2_x1 and event.pos[0] < zone2_x2 and event.pos[1] > zone2_y1 and event.pos[1] < zone2_y2:
                        number_create_fen=4
                    #bouton option clic
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone3_x1 and event.pos[0] < zone3_x2 and event.pos[1] > zone3_y1 and event.pos[1] < zone3_y2:
                        number_create_fen=3
                        page_option1()
                        

                    #bouton shop clic
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone27_x1 and event.pos[0] < zone27_x2 and event.pos[1] > zone27_y1 and event.pos[1] < zone27_y2:
                        number_create_fen=7
                        num_fen_shop=1
                        reinit_page=True
                        actualise_img_menu_shop()







                #page 3###########################
                elif number_create_fen==3:
                    #bouton menu clic
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone8_x1 and event.pos[0] < zone8_x2 and event.pos[1] > zone8_y1 and event.pos[1] < zone8_y2:
                        number_create_fen=2
                    if num_fen_option==0:
                        #bouton vitesse clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone4_x1 and event.pos[0] < zone4_x2 and event.pos[1] > zone4_y1 and event.pos[1] < zone4_y2:
                            monb=0
                            for lpl in chaine_vitesse_option:
                                monb+=1
                                if lpl==num_txt4_bouton:
                                    if monb<len(chaine_vitesse_option):
                                        num_txt4_bouton=chaine_vitesse_option[monb]
                                        break
                                    else :
                                        num_txt4_bouton=chaine_vitesse_option[0]
                                        break
    
                            initialiser_vitesse()
                        #bouton mode clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone5_x1 and event.pos[0] < zone5_x2 and event.pos[1] > zone5_y1 and event.pos[1] < zone5_y2:
                            monb=0
                            for lpl in chaine_mode_option:
                                monb+=1
                                if lpl==num_txt5_bouton:
                                    if monb<len(chaine_mode_option):
                                        num_txt5_bouton=chaine_mode_option[monb]
                                        break
                                    else :
                                        num_txt5_bouton=chaine_mode_option[0]
                                        break
                                        
                            initialiser_mode()
                        #bouton theme clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone9_x1 and event.pos[0] < zone9_x2 and event.pos[1] > zone9_y1 and event.pos[1] < zone9_y2:
                            monb=0
                            for lpl in chaine_theme_option:
                                monb+=1
                                if lpl==num_txt9_bouton:
                                    if monb<len(chaine_theme_option):
                                        num_txt9_bouton=chaine_theme_option[monb]
                                        break
                                    else :
                                        num_txt9_bouton=chaine_theme_option[0]
                                        break
                                    
                            def_theme()
                            
                        #bouton son clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone6_x1 and event.pos[0] < zone6_x2 and event.pos[1] > zone6_y1 and event.pos[1] < zone6_y2:
                            if num_case1==True:
                                num_case1=False
                            else :
                                num_case1=True
                        #bouton musique clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone7_x1 and event.pos[0] < zone7_x2 and event.pos[1] > zone7_y1 and event.pos[1] < zone7_y2:
                            if num_case2==True:
                                num_case2=False
                            else :
                                num_case2=True
                        #bouton bonus clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone16_x1 and event.pos[0] < zone16_x2 and event.pos[1] > zone16_y1 and event.pos[1] < zone16_y2:
                            if num_case7==True:
                                num_case7=False
                            else :
                                num_case7=True
                            initialiser_bonus()
                        #bouton malus clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone17_x1 and event.pos[0] < zone17_x2 and event.pos[1] > zone17_y1 and event.pos[1] < zone17_y2:
                            if num_case8==True:
                                num_case8=False
                            else :
                                num_case8=True
                            initialiser_malus()
                            
                    elif num_fen_option==1:
                        #bouton bordure clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone12_x1 and event.pos[0] < zone12_x2 and event.pos[1] > zone12_y1 and event.pos[1] < zone12_y2:
                            if num_case3==True:
                                num_case3=False
                            else :
                                num_case3=True
                            initialiser_mode()
                        #bouton piege clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone13_x1 and event.pos[0] < zone13_x2 and event.pos[1] > zone13_y1 and event.pos[1] < zone13_y2:
                            if num_case4==True:
                                num_case4=False
                            else :
                                num_case4=True
                            initialiser_mode()
                        #bouton multiproie clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone14_x1 and event.pos[0] < zone14_x2 and event.pos[1] > zone14_y1 and event.pos[1] < zone14_y2:
                            if num_case5==True:
                                num_case5=False
                            else :
                                num_case5=True
                            initialiser_mode()
                        #bouton multijoueur clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone15_x1 and event.pos[0] < zone15_x2 and event.pos[1] > zone15_y1 and event.pos[1] < zone15_y2:
                            if num_case6==True:
                                num_case6=False
                            else :
                                num_case6=True
                            initialiser_mode()

                    elif num_fen_option==2:
                        #bouton x2 points clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone18_x1 and event.pos[0] < zone18_x2 and event.pos[1] > zone18_y1 and event.pos[1] < zone18_y2:
                            if num_case9==True:
                                num_case9=False
                            else :
                                num_case9=True
                            initialiser_bonus()
                        #bouton +10pts clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone19_x1 and event.pos[0] < zone19_x2 and event.pos[1] > zone19_y1 and event.pos[1] < zone19_y2:
                            if num_case10==True:
                                num_case10=False
                            else :
                                num_case10=True
                            initialiser_bonus()
                        #bouton vie clic
                        if mode_multijoueur==False:
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone20_x1 and event.pos[0] < zone20_x2 and event.pos[1] > zone20_y1 and event.pos[1] < zone20_y2:
                                if num_case11==True:
                                    num_case11=False
                                else :
                                    num_case11=True
                                initialiser_bonus()
                        #bouton bouclier clic
                        if mode_piege==True:
                            if mode_multijoueur==False:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone21_x1 and event.pos[0] < zone21_x2 and event.pos[1] > zone21_y1 and event.pos[1] < zone21_y2:
                                    if num_case12==True:
                                        num_case12=False
                                    else :
                                        num_case12=True
                                    initialiser_bonus()
                            else:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone21_x1 and event.pos[0] < zone21_x2 and event.pos[1] > zone21_y1_bis and event.pos[1] < zone21_y2_bis:
                                    if num_case12==True:
                                        num_case12=False
                                    else :
                                        num_case12=True
                                    initialiser_bonus()
                    elif num_fen_option==3:
                        #bouton div points clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone24_x1 and event.pos[0] < zone24_x2 and event.pos[1] > zone24_y1 and event.pos[1] < zone24_y2:
                            if num_case13==True:
                                num_case13=False
                            else :
                                num_case13=True
                            initialiser_malus()
                        #bouton -pts clic
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone25_x1 and event.pos[0] < zone25_x2 and event.pos[1] > zone25_y1 and event.pos[1] < zone25_y2:
                            if num_case14==True:
                                num_case14=False
                            else :
                                num_case14=True
                            initialiser_malus()
                        #bouton invers
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone26_x1 and event.pos[0] < zone26_x2 and event.pos[1] > zone26_y1 and event.pos[1] < zone26_y2:
                            if num_case15==True:
                                num_case15=False
                            else :
                                num_case15=True
                            initialiser_malus()
                        

                    #>
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone11_1_x1 and event.pos[0] < zone11_1_x2 and event.pos[1] > zone11_1_y1 and event.pos[1] < zone11_1_y2:
                        if num_txt5_bouton==5:
                            if num_fen_option==0:
                                num_fen_option=1
                            elif num_fen_option==1:
                                if num_case7==True: 
                                    num_fen_option=2
                                elif num_case8==True:
                                    num_fen_option=3
                                else:
                                    page_option1()
                            elif num_fen_option==2:
                                if num_case8==True:
                                    num_fen_option=3
                                else:
                                    page_option1()
                            elif num_fen_option==3:
                                page_option1()








                #page 4#############################
                elif number_create_fen==4:
                    #menu
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone8_x1 and event.pos[0] < zone8_x2 and event.pos[1] > zone8_y1 and event.pos[1] < zone8_y2:
                        number_create_fen=2
                    #<
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone10_x1 and event.pos[0] < zone10_x2 and event.pos[1] > zone10_y1 and event.pos[1] < zone10_y2:
                        if num_score_txt_mode==0:
                            num_score_txt_mode=5
                        elif num_score_txt_mode==1:
                            num_score_txt_mode=0
                        elif num_score_txt_mode==2:
                            num_score_txt_mode=1
                        elif num_score_txt_mode==3:
                            num_score_txt_mode=2
                        elif num_score_txt_mode==4:
                            num_score_txt_mode=3
                        elif num_score_txt_mode==5:
                            num_score_txt_mode=4
                    #>
                    elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone11_x1 and event.pos[0] < zone11_x2 and event.pos[1] > zone11_y1 and event.pos[1] < zone11_y2:
                        if num_score_txt_mode==0:
                            num_score_txt_mode=1
                        elif num_score_txt_mode==1:
                            num_score_txt_mode=2
                        elif num_score_txt_mode==2:
                            num_score_txt_mode=3
                        elif num_score_txt_mode==3:
                            num_score_txt_mode=4
                        elif num_score_txt_mode==4:
                            num_score_txt_mode=5
                        elif num_score_txt_mode==5:
                            num_score_txt_mode=0





                #page 5#############################
                elif number_create_fen==5:
                    if event.type == KEYDOWN :
                        if event.key == K_p or event.key == K_ESCAPE:
                            if pause==True:
                                fps=ancien_fps
                                pause=False
                            elif pause==False:
                                ancien_fps=fps
                                fps=fps1
                                pause=True

                    if pause==True:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone22_x1 and event.pos[0] < zone22_x2 and event.pos[1] > zone22_y1 and event.pos[1] < zone22_y2:
                            fps=ancien_fps
                            pause=False
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone23_x1 and event.pos[0] < zone23_x2 and event.pos[1] > zone23_y1 and event.pos[1] < zone23_y2:
                            fps=ancien_fps
                            pause=False
                            stop_game_over=True

                    else:
                        if  mode_multijoueur==False:
                            pos_touche_j1=False
                            if malus_invers_touche==True:
                                if invers_touche_j1==True:
                                    pos_touche_j1=True
                                    
                            if pos_touche_j1==False:
                                if event.type == KEYDOWN:
                                    if event.key == K_LEFT:
                                        if not direction==direction_d:
                                            direction_p=direction_g
                                    if event.key == K_UP:
                                        if not direction==direction_b:
                                            direction_p=direction_h
                                    if event.key == K_RIGHT:
                                        if not direction==direction_g:
                                            direction_p=direction_d
                                    if event.key == K_DOWN:
                                        if not direction==direction_h:
                                            direction_p=direction_b
                                            
                                    if event.key == K_a:
                                        if not direction==direction_d:
                                            direction_p=direction_g
                                    if event.key == K_w:
                                        if not direction==direction_b:
                                            direction_p=direction_h
                                    if event.key == K_d:
                                        if not direction==direction_g:
                                            direction_p=direction_d
                                    if event.key == K_s:
                                        if not direction==direction_h:
                                            direction_p=direction_b
                                            
                                if event.type == MOUSEBUTTONDOWN:
                                    if event.button == 1:
                                        if direction==direction_d:
                                            direction_p=direction_h
                                        if direction==direction_b:
                                            direction_p=direction_d
                                        if direction==direction_g:
                                            direction_p=direction_b
                                        if direction==direction_h:
                                            direction_p=direction_g
                                            
                                    if event.button == 3:
                                        if direction==direction_d:
                                            direction_p=direction_b
                                        if direction==direction_b:
                                            direction_p=direction_g
                                        if direction==direction_g:
                                            direction_p=direction_h
                                        if direction==direction_h:
                                            direction_p=direction_d
                            else:
                                if event.type == KEYDOWN:
                                    if event.key == K_UP:
                                        if not direction==direction_d:
                                            direction_p=direction_g
                                    if event.key == K_RIGHT:
                                        if not direction==direction_b:
                                            direction_p=direction_h
                                    if event.key == K_DOWN:
                                        if not direction==direction_g:
                                            direction_p=direction_d
                                    if event.key == K_LEFT:
                                        if not direction==direction_h:
                                            direction_p=direction_b
                                            
                                    if event.key == K_s:
                                        if not direction==direction_d:
                                            direction_p=direction_g
                                    if event.key == K_d:
                                        if not direction==direction_b:
                                            direction_p=direction_h
                                    if event.key == K_w:
                                        if not direction==direction_g:
                                            direction_p=direction_d
                                    if event.key == K_a:
                                        if not direction==direction_h:
                                            direction_p=direction_b
                                            
                                if event.type == MOUSEBUTTONDOWN:
                                    if event.button == 3:
                                        if direction==direction_d:
                                            direction_p=direction_h
                                        if direction==direction_b:
                                            direction_p=direction_d
                                        if direction==direction_g:
                                            direction_p=direction_b
                                        if direction==direction_h:
                                            direction_p=direction_g
                                            
                                    if event.button == 1:
                                        if direction==direction_d:
                                            direction_p=direction_b
                                        if direction==direction_b:
                                            direction_p=direction_g
                                        if direction==direction_g:
                                            direction_p=direction_h
                                        if direction==direction_h:
                                            direction_p=direction_d
                                        
                        else:
                            pos_touche_j1=False
                            pos_touche_j2=False
                            if malus_invers_touche==True:
                                if invers_touche_j1==True:
                                    pos_touche_j1=True
                                if invers_touche_j2==True:
                                    pos_touche_j2=True

                            if pos_touche_j1==False:
                                if event.type == KEYDOWN:
                                    if event.key == K_a:
                                        if not direction==direction_d:
                                            direction_p=direction_g
                                    if event.key == K_w:
                                        if not direction==direction_b:
                                            direction_p=direction_h
                                    if event.key == K_d:
                                        if not direction==direction_g:
                                            direction_p=direction_d
                                    if event.key == K_s:
                                        if not direction==direction_h:
                                            direction_p=direction_b
                            else:
                                if event.type == KEYDOWN:
                                    if event.key == K_w:
                                        if not direction==direction_d:
                                            direction_p=direction_g
                                    if event.key == K_d:
                                        if not direction==direction_b:
                                            direction_p=direction_h
                                    if event.key == K_s:
                                        if not direction==direction_g:
                                            direction_p=direction_d
                                    if event.key == K_a:
                                        if not direction==direction_h:
                                            direction_p=direction_b
                                            
                            if pos_touche_j2==False:
                                if event.type == KEYDOWN:
                                    if event.key == K_LEFT:
                                        if not direction2==direction_d:
                                            direction_p2=direction_g
                                    if event.key == K_UP:
                                        if not direction2==direction_b:
                                            direction_p2=direction_h
                                    if event.key == K_RIGHT:
                                        if not direction2==direction_g:
                                            direction_p2=direction_d
                                    if event.key == K_DOWN:
                                        if not direction2==direction_h:
                                            direction_p2=direction_b
                            else:
                                if event.type == KEYDOWN:
                                    if event.key == K_DOWN:
                                        if not direction2==direction_d:
                                            direction_p2=direction_g
                                    if event.key == K_LEFT:
                                        if not direction2==direction_b:
                                            direction_p2=direction_h
                                    if event.key == K_UP:
                                        if not direction2==direction_g:
                                            direction_p2=direction_d
                                    if event.key == K_RIGHT:
                                        if not direction2==direction_h:
                                            direction_p2=direction_b

                        

                #page 6##############################
                elif number_create_fen==6:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone8_x1 and event.pos[0] < zone8_x2 and event.pos[1] > zone8_y1 and event.pos[1] < zone8_y2:
                        number_create_fen=2
                        
                #page 7##############################
                elif number_create_fen==7:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone8_x1 and event.pos[0] < zone8_x2 and event.pos[1] > zone8_y1 and event.pos[1] < zone8_y2:
                        number_create_fen=2

                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone28_x1 and event.pos[0] < zone28_x2 and event.pos[1] > zone28_y1 and event.pos[1] < zone28_y2:
                        if num_fen_shop==1:
                            number_create_fen=2
                        elif num_fen_shop==2:
                            num_fen_shop=1
                            num_page_shop_bis=0
                            actualise_img_menu_shop()
                        elif num_fen_shop==3:
                            num_fen_shop=2
                            reinit_page=False
                            if num_fen_shop_plus==1:
                                actualise_img_skin_shop()
                            elif num_fen_shop_plus==2:
                                actualise_img_objet_shop()
                            elif num_fen_shop_plus==3:
                                actualise_img_theme_shop()
                            elif num_fen_shop_plus==4:
                                actualise_img_mode_shop()
                            elif num_fen_shop_plus==5:
                                actualise_img_vitesse_shop()
                            
                    if num_fen_shop==1:
                        if img_shop_skin in image_load_shop_menu:
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_skin_menu_x and event.pos[0] < zone_skin_menu_x+taille_case_shop and event.pos[1] > zone_skin_menu_y and event.pos[1] < zone_skin_menu_y+taille_case_shop:
                                num_fen_shop_plus=1
                                num_fen_shop=2
                                actualise_img_skin_shop()
                                
                        if img_objet_shop in image_load_shop_menu:
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_objet_menu_x and event.pos[0] < zone_objet_menu_x+taille_case_shop and event.pos[1] > zone_objet_menu_y and event.pos[1] < zone_objet_menu_y+taille_case_shop:
                                num_fen_shop_plus=2
                                num_fen_shop=2
                                actualise_img_objet_shop()
                                
                        if img_theme_shop in image_load_shop_menu:
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_menu_x and event.pos[0] < zone_theme_menu_x+taille_case_shop and event.pos[1] > zone_theme_menu_y and event.pos[1] < zone_theme_menu_y+taille_case_shop:
                                num_fen_shop_plus=3
                                num_fen_shop=2
                                actualise_img_theme_shop()
                                
                        if img_mode_shop in image_load_shop_menu:
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_mode_menu_x and event.pos[0] < zone_mode_menu_x+taille_case_shop and event.pos[1] > zone_mode_menu_y and event.pos[1] < zone_mode_menu_y+taille_case_shop:
                                num_fen_shop_plus=4
                                num_fen_shop=2
                                actualise_img_mode_shop()
                                
                        if img_vitesse_shop in image_load_shop_menu:
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_vitesse_menu_x and event.pos[0] < zone_vitesse_menu_x+taille_case_shop and event.pos[1] > zone_vitesse_menu_y and event.pos[1] < zone_vitesse_menu_y+taille_case_shop:
                                num_fen_shop_plus=5
                                num_fen_shop=2
                                actualise_img_vitesse_shop()

                    elif num_fen_shop==2:

                        if num_fen_shop_plus==3:
                            if img_theme_ninja_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_ninja_x and event.pos[0] < zone_theme_ninja_x+taille_case_shop and event.pos[1] > zone_theme_ninja_y and event.pos[1] < zone_theme_ninja_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme1,
                                                       prix_theme_ninja,
                                                       lock_theme_ninja,
                                                       niveau_theme_ninja_maximum)
                                    cible_achat=1
                                    
                            if img_theme_negatif_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_negatif_x and event.pos[0] < zone_theme_negatif_x+taille_case_shop and event.pos[1] > zone_theme_negatif_y and event.pos[1] < zone_theme_negatif_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme2,
                                                       prix_theme_negatif,
                                                       lock_theme_negatif,
                                                       niveau_theme_negatif_maximum)
                                    cible_achat=2
                                    
                            if img_theme_ikeo_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_ikeo_x and event.pos[0] < zone_theme_ikeo_x+taille_case_shop and event.pos[1] > zone_theme_ikeo_y and event.pos[1] < zone_theme_ikeo_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme3,
                                                       prix_theme_ikeo,
                                                       lock_theme_ikeo,
                                                       niveau_theme_ikeo_maximum)
                                    cible_achat=3
                                                                
                            if img_theme_doume_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_doume_x and event.pos[0] < zone_theme_doume_x+taille_case_shop and event.pos[1] > zone_theme_doume_y and event.pos[1] < zone_theme_doume_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme4,
                                                       prix_theme_doume,
                                                       lock_theme_doume,
                                                       niveau_theme_doume_maximum)
                                    cible_achat=4
                                                                
                            if img_theme_deadpoule_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_deadpoule_x and event.pos[0] < zone_theme_deadpoule_x+taille_case_shop and event.pos[1] > zone_theme_deadpoule_y and event.pos[1] < zone_theme_deadpoule_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme5,
                                                       prix_theme_deadpoule,
                                                       lock_theme_deadpoule,
                                                       niveau_theme_deadpoule_maximum)
                                    cible_achat=5
                                                                
                            if img_theme_epm_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_epm_x and event.pos[0] < zone_theme_epm_x+taille_case_shop and event.pos[1] > zone_theme_epm_y and event.pos[1] < zone_theme_epm_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme6,
                                                       prix_theme_epm,
                                                       lock_theme_epm,
                                                       niveau_theme_epm_maximum)
                                    cible_achat=6
                                                                
                            if img_theme_girly_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_girly_x and event.pos[0] < zone_theme_girly_x+taille_case_shop and event.pos[1] > zone_theme_girly_y and event.pos[1] < zone_theme_girly_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme7,
                                                       prix_theme_girly,
                                                       lock_theme_girly,
                                                       niveau_theme_girly_maximum)
                                    cible_achat=7
                                                                
                            if img_theme_dark_girly_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_dark_girly_x and event.pos[0] < zone_theme_dark_girly_x+taille_case_shop and event.pos[1] > zone_theme_dark_girly_y and event.pos[1] < zone_theme_dark_girly_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme8,
                                                       prix_theme_dark_girly,
                                                       lock_theme_dark_girly,
                                                       niveau_theme_dark_girly_maximum)
                                    cible_achat=8
                                                                
                            if img_theme_zeldo_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_theme_zeldo_x and event.pos[0] < zone_theme_zeldo_x+taille_case_shop and event.pos[1] > zone_theme_zeldo_y and event.pos[1] < zone_theme_zeldo_y+taille_case_shop:
                                    fenetre_pres_achat(description_theme9,
                                                       prix_theme_zeldo,
                                                       lock_theme_zeldo,
                                                       niveau_theme_zeldo_maximum)
                                    cible_achat=9

                            

                        if num_fen_shop_plus==4:
                            if img_mode_normal_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_mode_normal_x and event.pos[0] < zone_mode_normal_x+taille_case_shop and event.pos[1] > zone_mode_normal_y and event.pos[1] < zone_mode_normal_y+taille_case_shop:
                                    fenetre_pres_achat(description_mode1,
                                                       prix_mode_normal,
                                                       lock_mode_normal,
                                                       niveau_mode_normal_maximum)
                                    cible_achat=1
                                    
                            if img_mode_ouvert_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_mode_ouvert_x and event.pos[0] < zone_mode_ouvert_x+taille_case_shop and event.pos[1] > zone_mode_ouvert_y and event.pos[1] < zone_mode_ouvert_y+taille_case_shop:
                                    fenetre_pres_achat(description_mode2,
                                                       prix_mode_ouvert,
                                                       lock_mode_ouvert,
                                                       niveau_mode_ouvert_maximum)
                                    cible_achat=2
                                    
                            if img_mode_piege_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_mode_piege_x and event.pos[0] < zone_mode_piege_x+taille_case_shop and event.pos[1] > zone_mode_piege_y and event.pos[1] < zone_mode_piege_y+taille_case_shop:
                                    fenetre_pres_achat(description1_mode3+str(nbr_piege)+description2_mode3,
                                                       prix_mode_piege,
                                                       lock_mode_piege,
                                                       niveau_mode_piege_maximum)
                                    cible_achat=3

                            if img_mode_multiproie_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_mode_multiproie_x and event.pos[0] < zone_mode_multiproie_x+taille_case_shop and event.pos[1] > zone_mode_multiproie_y and event.pos[1] < zone_mode_multiproie_y+taille_case_shop:
                                    fenetre_pres_achat(description1_mode4+str(limite_pomme)+description2_mode4,
                                                       prix_mode_multiproie,
                                                       lock_mode_multiproie,
                                                       niveau_mode_multiproie_maximum)
                                    cible_achat=4

                            if img_mode_multijoueur_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_mode_multijoueur_x and event.pos[0] < zone_mode_multijoueur_x+taille_case_shop and event.pos[1] > zone_mode_multijoueur_y and event.pos[1] < zone_mode_multijoueur_y+taille_case_shop:
                                    fenetre_pres_achat(description_mode5,
                                                       prix_mode_multijoueur,
                                                       lock_mode_multijoueur,
                                                       niveau_mode_multijoueur_maximum)
                                    cible_achat=5

                            if img_mode_special_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_mode_special_x and event.pos[0] < zone_mode_special_x+taille_case_shop and event.pos[1] > zone_mode_special_y and event.pos[1] < zone_mode_special_y+taille_case_shop:
                                    fenetre_pres_achat(description_mode6,
                                                       prix_mode_special,
                                                       lock_mode_special,
                                                       niveau_mode_special_maximum)
                                    cible_achat=6

                            


                                    
                                    
                        if num_fen_shop_plus==5:
                            if img_vitesse_lent_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_vitesse_lent_x and event.pos[0] < zone_vitesse_lent_x+taille_case_shop and event.pos[1] > zone_vitesse_lent_y and event.pos[1] < zone_vitesse_lent_y+taille_case_shop:
                                    fenetre_pres_achat(description_vitesse1+txt1_vitesse_description+description_vitesse2+str(fps4)+description_vitesse3,
                                                       prix_vitesse_lente,
                                                       lock_vitesse_lent,
                                                       niveau_vitesse_lente_maximum)
                                    cible_achat=1
    
                            if img_vitesse_normal_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_vitesse_normal_x and event.pos[0] < zone_vitesse_normal_x+taille_case_shop and event.pos[1] > zone_vitesse_normal_y and event.pos[1] < zone_vitesse_normal_y+taille_case_shop:
                                    fenetre_pres_achat(description_vitesse1+txt2_vitesse_description+description_vitesse2+str(fps3)+description_vitesse3,
                                                       prix_vitesse_normal,
                                                       lock_vitesse_normal,
                                                       niveau_vitesse_normal_maximum)
                                    cible_achat=2
    
                            if img_vitesse_rapide_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_vitesse_rapide_x and event.pos[0] < zone_vitesse_rapide_x+taille_case_shop and event.pos[1] > zone_vitesse_rapide_y and event.pos[1] < zone_vitesse_rapide_y+taille_case_shop:
                                    fenetre_pres_achat(description_vitesse1+txt3_vitesse_description+description_vitesse2+str(fps2)+description_vitesse3,
                                                       prix_vitesse_rapide,
                                                       lock_vitesse_rapide,
                                                       niveau_vitesse_rapide_maximum)
                                    cible_achat=3

                            if img_vitesse_expert_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_vitesse_expert_x and event.pos[0] < zone_vitesse_expert_x+taille_case_shop and event.pos[1] > zone_vitesse_expert_y and event.pos[1] < zone_vitesse_expert_y+taille_case_shop:
                                    fenetre_pres_achat(description_vitesse1+txt4_vitesse_description+description_vitesse2+str(fps5)+description_vitesse3,
                                                       prix_vitesse_expert,
                                                       lock_vitesse_expert,
                                                       niveau_vitesse_expert_maximum)
                                    cible_achat=4
                                    
                            if img_vitesse_acceleration_shop in image_load_shop_menu:
                                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_vitesse_acceleration_x and event.pos[0] < zone_vitesse_acceleration_x+taille_case_shop and event.pos[1] > zone_vitesse_acceleration_y and event.pos[1] < zone_vitesse_acceleration_y+taille_case_shop:
                                    fenetre_pres_achat(description_vitesse1+txt5_vitesse_description+description_vitesse2+description_vitesse4,
                                                       prix_vitesse_acceleration,
                                                       lock_vitesse_acceleration,
                                                       niveau_vitesse_acceleration_maximum)
                                    cible_achat=5
                                    
                    elif num_fen_shop==3:
                        if prix_achat<=argent:
                            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone29_x1 and event.pos[0] < zone29_x2 and event.pos[1] > zone29_y1 and event.pos[1] < zone29_y2:
                                argent-=prix_achat
                                maj_level_achat()

                                

                    if img_fleche_gauche_shop in image_load_shop_menu:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_fleche_gauche_x and event.pos[0] < zone_fleche_gauche_x+taille_case_shop and event.pos[1] > zone_fleche_gauche_y and event.pos[1] < zone_fleche_gauche_y+taille_case_shop:
                            num_page_shop_bis-=1
                            verif_init_choose=True
                            
                    if img_fleche_droite_shop in image_load_shop_menu:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > zone_fleche_droite_x and event.pos[0] < zone_fleche_droite_x+taille_case_shop and event.pos[1] > zone_fleche_droite_y and event.pos[1] < zone_fleche_droite_y+taille_case_shop:
                            num_page_shop_bis+=1
                            verif_init_choose=True
                            
                    image_load_shop_menu=image_load_shop_menu_bis[num_page_shop_bis]
                    if verif_init_choose==True:
                        verif_init_choose=False
                        declenche_choose_zone()
                    
        if continuer==True:
            if  number_create_fen==5 :
                if not vie_serpent1==0:   
                    direction=direction_p   #serpent 1
                
                if mode_multijoueur==True and not vie_serpent2==0:      #serpent 2
                    direction2=direction_p2
                    
                if num_txt4_bouton==4 and pause==False:
                    fps=round((log(compt_fps)),4)
                    compt_fps=compt_fps*1.05
                

            draw_fenetre()






            #actualisation
            fenetre.blit(fond,position_fond)
            pygame.display.update()


"""
rebliter
fenetre.fill()

recuperer longueur
print(texte.get_width())

recuperer hauteur
print(texte.get_height())


print(texte.get_width())
print(texte.get_height())
"""

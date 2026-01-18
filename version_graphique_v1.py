"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

from time import*
from turtle import*
from Code.game.fonction_game import*
from Code.Affichage.fonction_affichage import *

def dessine_resultat(resultat, t):
    if "Joueur" in resultat:
        dessiner_bouton((0,0),50,resultat, "green", t)
    else:
        dessiner_bouton((0,0),50,resultat, "red", t)


# Initialistion des règles, joueur, A et B, ainsi que la variable last_player qui représentera le dernier joueur a avoir joué

regle = [2,3,5]
min_regle = min(regle)          # on utilise min_regle car comme ça on evite d'avoir à appeler la fonction min() à chaque fois

nb_human = 1 #int(input("Entrez le nombre de joueur (humain) : "))
nb_bot = 1 #int(input("Entrez le nombre de joueur (bot) : "))
joueur = []
for i in range(1,nb_human+1):
    joueur.append("Joueur n°"+str(i))                              # On defini le nombre d'humain et de bot qui joue 
for i in range(1,nb_bot+1):
    joueur.append("Bot n°"+str(i))
nb_joueur_total = nb_bot + nb_human                         

last_player = 0 # 0=p1 et 1=p2 ,ect                         on defini une variable last joueur pour savoir facilement qui est le dernier joueur a avoir jouer
                                                            # qui est une information très utile car on ne fais pas Nécessairement du 1 joueur vs 1 ordi
                                                            # de plus je trouve que ça simplifie la compréhension du code, on comprend facilement qu'on incremente le joueur qui joue,
                                                            # je sais que plusieurs de mes camarades avaient parfois un problème avec votre protocole, car on test pour rentrer dans 
                                                            # la boucle si le joueur peut jouer et après on test si il ne peut pas jouer alors il perd, il n'est pas préciser que c'est en fonction des éléments choisi

screen = Screen()                               #initialise l'instance screen qui est la fenetre de Turtle
screen.setup(width=1.0, height=1.0)             # met la fenètre de turtle en pleine écran

t_background = Turtle()                         #initialisation de la turtle qui dessine le decor/background
t_background.hideturtle()

t_coup_temporaire = Turtle()                    #initialisation de la turtle qui écrit les informations en direct le nombre de fruit mangé par l'utilisatuer
t_coup_temporaire.hideturtle()

t_ecriture = Turtle()
t_ecriture.hideturtle()                         #initialisation de la turtle qui écrit les informations globale de la partie

screen.tracer(0)                                # active le tracer(0) qui permet de afficher le resultat sans toute les animations, ect



last_play = "Début de la partie"                                            # initialise la variable qui affichera le dernier coup à "Début de la partie" tant qu'il n'y a pas encore de coup joué
liste_objet = initialisation(t_background, t_ecriture,  screen, last_play)  # initialise la liste liste_objet, qui contient 4 sous-lists :
                                                                            # la première est une autre sous-liste qui contient toute les position/turtue/etat/taille
                                                                            # la deuxième contient le nombre de fruit restant pour chaque fruit
                                                                            # la troisieme contient les fruits choisis en chaine de caractère, utile de nombreuse fois pour l'affichage
                                                                            # la dernière contient les fonction de dessin associé au fruit


while peutjouer(liste_objet[1], min_regle):         #demarre la boucle jeux, peutjouer() est une fonction qui renvoit True si au moins un coup est disponible
    if last_player < nb_human:                      #test si c'est aux joueur ou aux bots de joueur
        liste_objet, last_play = tour_humain(t_coup_temporaire, liste_objet, screen, regle)         # Fais jouer un humain et met à jour les variables dernier coup et la liste des objet
    else:
        sleep(3.5)                                                                                  # attend un petit peu avant que le bot joue
        liste_objet, last_play = tour_ordi(regle, liste_objet, screen)                              # Fais jouer un bot et met à jour les variables dernier coup et la liste des objet
    
    
    affichage_information_game(t_ecriture, liste_objet, joueur[last_player], last_play)     # affiche les information global du jeu : nom du jeu + nombre de chaque fruit + dernier coup
    screen.update()                                                                         # met à jour la fenetre screen

    if last_play == "le joueur n'a pas\nrespécté les règles":                               # test si un joueur n'as pas respécté les regle
        break                                                                               # si oui on sort de la boucle

    last_player = (last_player + 1) % nb_joueur_total                                       # incremente de 1 le compteur de joueur



dessine_resultat(joueur[last_player-1] + " a gagné !!!", t_background)          # affiche le resultat en gros
screen.update()                                                                 # met à jour la fenetre screen
sleep(4)                                                                        # attend 4 sec

# ferme la fenètre car il y a plus rien


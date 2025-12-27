from random import*
from turtle import*
from Code.game.fonction_game import*
from Code.Affichage.affichage_fruit import *


# Initialistion des règles, joueur, A et B, ainsi que la variable last_player qui représentera le dernier joueur a avoir joué

regle = [2,3,5]
min_regle = min(regle)          # on utilise min_regle car comme ça on evite d'avoir à appeler la fonction min() à chaque fois

nb_human = int(input("Entrez le nombre de joueur (humain) : "))
nb_bot = int(input("Entrez le nombre de joueur (bot) : "))
joueur = []
for i in range(1,nb_human+1):
    joueur.append("joueur"+str(i))                              # On defini le nombre d'humain et de bot qui joue 
for i in range(1,nb_bot+1):
    joueur.append("bot"+str(i))
nb_joueur_total = nb_bot + nb_human                         

last_player = 0 # 0=p1 et 1=p2 ,ect                         on defini une variable last joueur pour savoir facilement qui est le dernier joueur a avoir jouer
                                                            # qui est une information très utile car on ne fais pas Nécessairement du 1 joueur vs 1 ordi
                                                            # de plus je trouve que ça simplifie la compréhension du code, on comprend facilement qu'on incremente le joueur qui joue,
                                                            # je sais que plusieurs de mes camarades avaient parfois un problème avec votre protocole, car on test pour rentrer dans 
                                                            # la boucle si le joueur peut jouer et après on test si il ne peut pas jouer alors il perd, il n'est pas préciser que c'est en fonction des éléments choisi
nb_A_initial = nb_A = randint(15,25)
nb_B_initial = nb_B = randint(15,25)
                                     # initialisation des variables de quantité d'élément initaile et en fonction de la partie

liste_a = liste_b = []

for i in range(nb_A):
    liste_a.append([(i,0), "tortue", "entière"])
for i in range(nb_B):
    liste_b.append([(0,i), "tortue", "entière"])



    # debut de la boucle while tant que la partie a un mouvement possible

while peutjouer(nb_A, nb_B, min_regle):
    print("\nIl reste", nb_A, "A et", nb_B, "B")
    print("C'est au tour de", joueur[last_player])      # affichage du nombre d'élément ainsi que la personne qui doit jouer

    if last_player < nb_human:
        cA, cB, liste_a, liste_b = tour_humain(regle, nb_A, nb_B, liste_a, liste_b)         # Fais jouer un humain si c'est le tour d'un humai et d'un bot si c'est un bot
    else:
        cA, cB, liste_a, liste_b = tour_ordi(regle, nb_A, nb_B, liste_a, liste_b)

    nb_A -= cA                                          # on retire les éléments pris par la personne qui a joué
    nb_B -= cB                                          
    
    last_player = (last_player + 1) % nb_joueur_total   # incremente de 1 le compteur de joueur pour faire jouer tout le monde








print("Il reste", nb_A, "A et", nb_B, "B")              # affiche le resultat des éléments restant, ainsi que le gagant !!!
print("Le gagnant est le joueur", joueur[last_player-1])
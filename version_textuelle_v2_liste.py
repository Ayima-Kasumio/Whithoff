"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

from random import*

def choix_legit(nb_A, nb_B, choix, nb_element_voulu):          # fonction qui verifie qu'un choix peut être jouer ou non et il renvoie cA, cB, et action correctement assigné
    cA = 0
    cB = 0                                          # on initialise les variables
    action = False
    
    if choix == 1:
        if nb_A >= nb_element_voulu:
            cA = nb_element_voulu                       # et en fonction du choix on assigne correctement cA, cB, et action
            cB = 0
            action = True
    elif choix == 2:
        if nb_B >= nb_element_voulu:
            cA = 0
            cB = nb_element_voulu
            action = True
    elif choix == 3:
        if (nb_A >= nb_element_voulu) and (nb_B >= nb_element_voulu):
            cA = cB = nb_element_voulu
            action = True
    
    return cA, cB, action                       # Et on les renvoie


def tour_ordi(regle, nb_A, nb_B, liste_a, liste_b):                           # Un tour pour un joueur bot
    action = False                      # definition d'une variable action pour la boucle while
    while not action:                       # action permet de verifier si le joueur a joué ou pas encore
        choix = randint(1,3)                            # choisi aléatoirement un choix possible
        nb_element_voulu = regle[randint(0,2)]          # choisi aléatoirement un nb d'élément à enlever
        cA, cB, action = choix_legit(nb_A, nb_B, choix, nb_element_voulu)       # choix_legit() il verifie que cette combinaison est possible où si il mannque des éléments de A ou de B, et il assigne les bonnes valeurs de cA et cB en fonction du choix; il modifie action à True
        
    
    print("L'ordinateur a choisi de prendre", nb_element_voulu,"du choix", choix)

    for i in range(cA):
        mange = False
        while not mange:
            index = randint(0, len(liste_a)-1)
            if liste_a[index][2] == "Pas mangé":
                liste_a[index][2] = "mangé"
                mange = True
    
    for i in range(cB):
        mange = False
        while not mange:
            index = randint(0, len(liste_b)-1)
            if liste_b[index][2] == "Pas mangé":
                liste_b[index][2] = "mangé"
                mange = True

    return cA, cB, liste_a, liste_b

def tour_humain(regle, nb_A, nb_B, liste_a, liste_b):                         # Un tour pour un joueur humain
    action = False                      # definition d'une variable action pour la boucle while
    while not action:                       # action permet de verifier si le joueur a joué ou pas encore
        choix = int(input("Que voulez vous prendre ? 1: A, 2: B , 3 : B et A "))
        while (choix < 1) or (choix > 3):                   # Tant que le joueur ne joue pas un coup valide il dois rejouer
            choix = int(input("Choix invalide. Que voulez vous prendre ? 1: A, 2: B , 3 : B et A "))

        nb_element_voulu = int(input(f"Combien en voulez vous prendre {regle[0]}, {regle[1]} ou {regle[2]}? "))
        if (nb_element_voulu not in regle):                         # tant que le nombre d'élément à prendre n'est pas autorisé par les regles il dois rejouer
            nb_element_voulu = int(input(f"Choix invalide. Combien en voulez vous prendre {regle[0]}, {regle[1]} ou {regle[2]}? "))

        cA, cB, action = choix_legit(nb_A, nb_B, choix, nb_element_voulu)  # choix_legit() il verifie que cette combinaison est possible où si il mannque des éléments de A ou de B, et il assigne les bonnes valeurs de cA et cB en fonction du choix; il modifie action à True
        
        if not action :                         # Tant que le choix n'est pas valide il doix rejouer
            print("Choix Invalide")


    return cA, cB, liste_a, liste_b

def affiche(nb_A, nb_B, nb_A_initial, nb_B_initial, liste_a, liste_b):        # Une fonction qui affiche les éléments restants et ceux qui on été pris
    for i in range(nb_A):
        print("A", end=" ")
    for i in range(nb_A_initial-nb_A):
        print(" - ", end="")

    print(liste_a)
    print("\n")

    for i in range(nb_B):
        print("B", end=" ")
    for i in range(nb_B_initial-nb_B):
        print(" - ", end="")

    print(liste_b)

    print("\n")

def peutjouer(nb_A, nb_B, min_regle):                       # Une fonction qui verifie si il existe encore Au Moins un coup possible
    return (nb_A >= min_regle) or (nb_B >= min_regle)


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
    liste_a.append([(i,0), "tortue", "Pas mangé"])
for i in range(nb_B):
    liste_b.append([(0,i), "tortue", "Pas mangé"])



    # debut de la boucle while tant que la partie a un mouvement possible

while peutjouer(nb_A, nb_B, min_regle):
    print("\nIl reste", nb_A, "A et", nb_B, "B")
    affiche(nb_A, nb_B, nb_A_initial, nb_B_initial, liste_a, liste_b)
    print("C'est au tour de", joueur[last_player])      # affichage du nombre d'élément ainsi que la personne qui doit jouer

    if last_player < nb_human:
        cA, cB, liste_a, liste_b = tour_humain(regle, nb_A, nb_B, liste_a, liste_b)         # Fais jouer un humain si c'est le tour d'un humai et d'un bot si c'est un bot
    else:
        cA, cB, liste_a, liste_b = tour_ordi(regle, nb_A, nb_B, liste_a, liste_b)

    nb_A -= cA                                          # on retire les éléments pris par la personne qui a joué
    nb_B -= cB                                          
    
    last_player = (last_player + 1) % nb_joueur_total   # incremente de 1 le compteur de joueur pour faire jouer tout le monde








print("Il reste", nb_A, "A et", nb_B, "B")              # affiche le resultat des éléments restant, ainsi que le gagant !!!
affiche(nb_A, nb_B, nb_A_initial, nb_B_initial, liste_a, liste_b)
print("Le gagnant est le joueur", joueur[last_player-1])
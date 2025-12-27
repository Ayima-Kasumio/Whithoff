####################################
# jeu de Whythof avec règle
####################################

'''
Au départ, un nombre nbAInit d'objets de type A et
un nombre nbBInit d'objets de type B sont tirés au hasard.
Une liste regle contient la "règle du jeu" c'est à dire le nombre d'objets
qu'il est possible de retirer (e.g. regle=[2,3,5] signifie que l'on peut
retirer 2, 3 ou 5 objets). 
A chaque tour on doit retirer n objets où n est dans regle de la façon suivante:
    retirer n objets dans A 
    ou bien
    retirer n objets dans B
    ou bien
    retirer n objets à la fois dans A et B
'''

'''La structure proposée ci-dessous est le minimum pour décomposer le code.
N'hésitez pas à ajouter des fonctions/procédures qui vous paraissent utiles
pour améliorer la décomposition et le lisibilité du code.
'''

# pour pouvoir faire joueur l'ordinateur
import random


# affiche les objets "A" ou "B", - si l'objet a été enlevé
# nbA est le nombre de A actuel, nbAInit est le nombre de A initial
# nbB est le nombre de B actuel, nbBInit est le nombre de B initial
def afficheObjets(nbA,nbAInit,nbB,nbBInit):
    print("Il reste",nbA,"A et",nbB,"B")
    for i in range(nbA):
        print("A", end=" ")
    for i in range(nbAInit-nbA):
        print("-", end=" ")
    print("\n")
    for i in range(nbB):
        print("B", end=" ")
    for i in range(nbBInit-nbB):
        print("-", end=" ")
    print("\n")


# renvoie vrai si on peut jouer dans A ou dans B
def peutJouer(nbA,nbB,regle):
    min_regle = min(regle)
    if (nbA >= min_regle or nbB >= min_regle):
        return True
    else:
        return False

# fait jouer le joueur
# renvoie un couple (cA,cB) où cA est le nombre choisi pour retirer dans A
# et cB est le nombre choisi pour retirer dans B
def joueurJoue(nbA,nbB,regle):
    cA = int(input("  ---> Combien de A ? "))
    cB = int(input("  ---> Combien de B ? "))
    return (cA, cB)

# fait jouer l'ordinateur
# renvoie un couple (cA,cB) où cA est le nombre choisi pour retirer dans A
# et cB est le nombre choisi pour retirer dans B
def ordiJoue(nbA,nbB,regle):
    print("L'ordi réfléchit",end="")
    for _ in range(100):
        print(".",end="")
    print("\n")
    loi = random.randint(1,3) # 1= que des A ; 2= que des B ; 3= des A et des B
    nb_pris = random.choice(regle)
    if loi == 1 :
        return (0,nb_pris)
    elif loi == 2 :
        return (nb_pris, 0)
    elif loi == 3 :
        return (nb_pris, nb_pris)
    


    # A COMPLETER
    # utilise random.choice(regle) pour choisir que retirer
    # Par exemple, random.choice([1,2,3,12]) renvoie un nombre parmi 1,2,3 et 12
    # utilise random.randint(0,1) pour décider si l'ordi prend dans A ou dans B ou dans les deux

    
################################################
''' Boucle de jeu
Tirer un nombre aléatoire d'objets A et B
Tant que l'on peut jouer :
   Afficher les objets
   Faire jouer le joueur
   Si le joueur ne peut pas jouer : le joueur a perdu
   Sinon
      Afficher les objets
      Faire jouer l'ordinateur
      Si l'ordinateur ne peut pas jouer, l'ordinateur a perdu
'''
nbAInit = nbA = random.randint(10,35)
nbBInit = nbB = random.randint(10,35)
regle = [2, 3, 5]
print("Bienvenue dans le jeu de Whythof\nRègle:", regle)

while peutJouer(nbA, nbB, regle):
    afficheObjets(nbA,nbAInit,nbB,nbBInit)
    (cA, cB) = joueurJoue(nbA,nbB,regle)
    if ((nbA-cA)<0 or (nbB-cB)<0 ) :
        gagnant = "Ordi"
    else:
        nbA -= cA
        nbB -= cB

        afficheObjets(nbA,nbAInit,nbB,nbBInit)
        (cA, cB) = ordiJoue(nbA,nbB,regle)
        print("L'ordi a pris", cA, "A et", cB, "B\n")

        if ((nbA-cA)<0 or (nbB-cB)<0 ) :
            gagnant = "Joueur"
            
        nbA -= cA
        nbB -= cB





print("C'est fini\n",gagnant," a gagné !", sep="")

""" C'est une version très primitive, il y a des erreurs à gérer mais en suivant le protocole que vous nous avez donné nous avons obtenu ce code

Il y a des modifications que je trouve intéressante à faire, par exemple:
    - on pourrait faire une liste de joueur (dans le cas actuel c'est 1 joueur vs un ordi mais si on fait un mode comme 1joueur vs 1 joueur, vs 1 ordi on a juste à modifier une liste)
    - pour l'instant, il mannque des gestion d'erreur, genre actuellement le joueur pourrait prendre 19 A des le debut de la partie
    - de même pour l'ordi il peut prendre n'importe lequel des choix, il serait intéressant de rajouter des test pour verifier si il reste assez de A et de B pour qu'il soit moins bête

c'est que mon avis perso mais ça pourrait être interressant c'est pour ça qu'après avoir fait votre version j'ai fait une version personnelle qui contient toute ces modifs














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


def tour_ordi(regle, nb_A, nb_B):                           # Un tour pour un joueur bot
    action = False                      # definition d'une variable action pour la boucle while
    while not action:                       # action permet de verifier si le joueur a joué ou pas encore
        choix = randint(1,3)                            # choisi aléatoirement un choix possible
        nb_element_voulu = regle[randint(0,2)]          # choisi aléatoirement un nb d'élément à enlever
        cA, cB, action = choix_legit(nb_A, nb_B, choix, nb_element_voulu)       # choix_legit() il verifie que cette combinaison est possible où si il mannque des éléments de A ou de B, et il assigne les bonnes valeurs de cA et cB en fonction du choix; il modifie action à True
        
    
    print("L'ordinateur a choisi de prendre", nb_element_voulu,"du choix", choix) 
    return cA, cB

def tour_humain(regle, nb_A, nb_B):                         # Un tour pour un joueur humain
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


    return cA, cB

def affiche(nb_A, nb_B, nb_A_initial, nb_B_initial):        # Une fonction qui affiche les éléments restants et ceux qui on été pris
    for i in range(nb_A):
        print("A", end=" ")
    for i in range(nb_A_initial-nb_A):
        print(" - ", end="")

    print("\n")

    for i in range(nb_B):
        print("B", end=" ")
    for i in range(nb_B_initial-nb_B):
        print(" - ", end="")

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
nb_A = randint(15,30)
nb_B = randint(15,30)
nb_A_initial = nb_A                                     # initialisation des variables de quantité d'élément initaile et en fonction de la partie
nb_B_initial = nb_B



    # debut de la boucle while tant que la partie a un mouvement possible

while peutjouer(nb_A, nb_B, min_regle):
    print("\nIl reste", nb_A, "A et", nb_B, "B")
    affiche(nb_A, nb_B, nb_A_initial, nb_B_initial)
    print("C'est au tour de", joueur[last_player])      # affichage du nombre d'élément ainsi que la personne qui doit jouer

    if last_player < nb_human:
        cA, cB = tour_humain(regle, nb_A, nb_B)         # Fais jouer un humain si c'est le tour d'un humai et d'un bot si c'est un bot
    else:
        cA, cB = tour_ordi(regle, nb_A, nb_B)

    nb_A -= cA                                          # on retire les éléments pris par la personne qui a joué
    nb_B -= cB                                          
    
    last_player = (last_player + 1) % nb_joueur_total   # incremente de 1 le compteur de joueur pour faire jouer tout le monde


print("Il reste", nb_A, "A et", nb_B, "B")              # affiche le resultat des éléments restant, ainsi que le gagant !!!
affiche(nb_A, nb_B, nb_A_initial, nb_B_initial)
print("Le gagnant est le joueur", joueur[last_player-1])

"""
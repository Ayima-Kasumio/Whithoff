from random import*

from Code.game.choix_legit import*


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
            if liste_a[index][2] == "entière":
                liste_a[index][2] = "mangé"
                mange = True
    
    for i in range(cB):
        mange = False
        while not mange:
            index = randint(0, len(liste_b)-1)
            if liste_b[index][2] == "entière":
                liste_b[index][2] = "mangé"
                mange = True

    return cA, cB, liste_a, liste_b
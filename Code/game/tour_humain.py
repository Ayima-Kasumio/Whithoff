from Code.game.choix_legit import*

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
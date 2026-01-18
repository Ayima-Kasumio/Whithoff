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

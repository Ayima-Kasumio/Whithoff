def coup_valide(liste_objet, coup, regle):
    if coup[2] == coup[3] == 0 :
        cA = coup[0]
        cB = coup[1]
        return ((cA == cB and cA <= liste_objet[1][0] and cB <= liste_objet[1][1] and cA in regle) or (cA ==0 and cB in regle and cB <= liste_objet[1][1]) or (cA in regle and cB ==0 and cA <= liste_objet[1][0]))
    elif coup[0] == coup[1] == 0:
        cA = coup[2]
        cB = coup[3]
        return ((cA == cB and cA <= liste_objet[1][2] and cB <= liste_objet[1][3] and cA in regle) or (cA ==0 and cB in regle and cB <= liste_objet[1][3]) or (cA in regle and cB ==0 and cA <= liste_objet[1][2]))
    else:
        return False
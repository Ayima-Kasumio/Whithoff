from Code.Affichage.procedure_raisin.dessiner_raisin_mangee import*
from Code.Affichage.procedure_pasteque.dessiner_pasteque_mangee import*

def fxn(x, y):
    global liste_tortue_raisin
    global liste_tortue_pasteque
    global taille_raisin
    global taille_pasteque
    global screen

    for i in liste_tortue_raisin:
        if ((x-i[0][0])**2 + (y-i[0][1])**2)**0.5 < taille_raisin:
            if (i[2] == "Pas mangé"):
                dessiner_raisin_mangee((i[0][0], i[0][1]-taille_raisin), taille_raisin, i[1])
                i[2] = "Mangé"
                break

    for i in liste_tortue_pasteque:
        if ( ((x-i[0][0])**2 + (y-i[0][1])**2)**0.5 < 2*taille_pasteque and y-i[0][1]<taille_pasteque):
            if (i[2] == "Pas mangé"):
                dessiner_pasteque_mangee((i[0][0], i[0][1]-taille_pasteque), taille_pasteque, i[1])
                i[2] = "Mangé"
                break

    screen.update()
from Code.Affichage.dessiner_bouton import *

def affichage_fruit_mange_tour(t, liste_fruit, coup_temporaire):
    t.clear()
    t.up()
    for i in range(len(coup_temporaire)):
        t.goto(-860, 0-30*i)
        t.write(liste_fruit[2][i]+" Mangé : " + str(coup_temporaire[i]),False,"center", ("Arial", 12, "normal"))

    dessiner_bouton((-860,-200),12, "Tour fini", "red", t)
from Code.Affichage.dessiner_rectangle import *

def dessiner_bouton(position,taille_police, texte, color, t):
    dessiner_rectangle((position[0]-taille_police*(len(texte)//2+1), position[1]+2*taille_police), taille_police*(len(texte)+2), 4*taille_police , color, t )

    t.up()
    t.goto(position[0],position[1]-taille_police)
    t.write(texte,False,"center", ("Arial", taille_police, "normal"))
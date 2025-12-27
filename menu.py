from turtle import*
from Code.Affichage.fonction_affichage import *

def dessiner_bouton(position, largeur, hauteur, couleur, texte, t):
    t.up()
    t.goto(position[0] - largeur/2, position[1] + hauteur/2)
    t.down()
    t.color("black", couleur)
    t.begin_fill()
    for _ in range(2):
        t.forward(largeur)
        t.right(90)
        t.forward(hauteur)
        t.right(90)
    t.end_fill()

    t.up()
    t.goto(position[0], position[1]-hauteur/(6))
    t.down()
    t.color("black")
    t.write(texte, align="center", font=("Arial", 13, "bold"))

def fxn(x, y):
    global liste_boutons
    for i in liste_boutons:
        if (abs(i[0][0] - x) < i[1]/2) and (abs(i[0][1] - y) < i[2]/2):
            if i[4] == "Start game":
                tc.up()
                tc.goto(0,0)
                tc.down()
                tc.clear()
                tc.write("Game Started")
                
            elif i[4] == "X":
                bye()
        


screen = Screen()

t_background = Turtle()
t_background.speed()
t_background.hideturtle()
tc = Turtle()
tc.speed()
tc.hideturtle()

liste_boutons = [[(0, 0), 150, 50, "blue", "Start game"], [(910, 460), 50, 50, "red", "X"]]
dessiner_fond(t_background, screen, 3, 0, 72, 250)

for i in liste_boutons:
    dessiner_bouton(i[0], i[1], i[2], i[3], i[4], tc)

screen.onclick(fxn)

done()
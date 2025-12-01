# Illustration de comment utiliser 2 tortues et comment temporiser

# ce code n'est pas très bien écrit, il faudra bien sûr structurer mieux que ça

from turtle import *
import time

# dessine une croix dans le carré de largeur l dont le point en bas
# à gauche est (x,y), avec la tortue t
def dessineCroix(x,y,l,c,t):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.width(5)
    t.goto(x+l,y+l)
    t.up()
    t.goto(x+l,y)
    t.down()
    t.goto(x,y+l)
    t.width(1)

# le décor dessiné avec la tortue t
def decor(t):
    dessineCroix(-200,-100,100,"green",t)
    dessineCroix(-200,100,50,"yellow",t)

# dessine un objet de type A avec la tortue t
def dessineObjetA(x,y,l,c,t):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(c)
    t.circle(l)

# dessin rapide
speed(0)

# tortue du décor
# on créé un premier objet de la classe Turtle
td = Turtle()

# tortue des Objets
# on créé un deuxième objet de la classe Turtle
tc = Turtle()

# on dessine le décor
decor(td)

# dessin de 2 objets
dessineObjetA(0,100,20,"blue",tc)
dessineObjetA(0,0,20,"blue",tc)

# on attend 1 seconde
time.sleep(2)

# on efface ce qui a été dessiné par la tortue des Objets
# le décor ne bouge pas
tc.clear()

# on attend 2 secondes avant de redessiner d'autres Objets
time.sleep(2)
dessineObjetA(0,0,20,"purple",tc)





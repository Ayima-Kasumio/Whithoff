from turtle import *
import random

def arbre_classique(t, x, y, scale):
    t.penup()
    t.goto(x, y)
    t.color("#8B5A2B")
    t.pendown()

    t.begin_fill()
    for _ in range(2):
        t.forward(30*scale)
        t.left(90)
        t.forward(120*scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(x+15*scale, y+120*scale)
    t.color("#2E8B57")
    t.pendown()

    t.begin_fill()
    t.circle(70*scale)
    t.end_fill()

def arbre_large(t, x, y, scale):
    t.penup()
    t.goto(x, y)
    t.color("#7A4A1E")
    t.pendown()

    t.begin_fill()
    for _ in range(2):
        t.forward(35*scale)
        t.left(90)
        t.forward(110*scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(x+17*scale, y+110*scale)
    t.color("#228B22")
    t.pendown()

    t.begin_fill()
    t.circle(90*scale)
    t.end_fill()



def arbre_fruitier(t, x, y, scale):
    t.penup()
    t.goto(x, y)
    t.color("#6B4226")
    t.pendown()

    t.begin_fill()
    for _ in range(2):
        t.forward(28*scale)
        t.left(90)
        t.forward(115*scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(x+14*scale, y+115*scale)
    t.color("#3CB371")
    t.pendown()

    t.begin_fill()
    t.circle(65*scale)
    t.end_fill()

    # Fruits
    for _ in range(6):
        fx = x + random.randint(-40, 40)*scale
        fy = y + 140*scale + random.randint(-20, 40)*scale
        t.penup()
        t.goto(fx, fy)
        t.color("purple")
        t.pendown()
        t.begin_fill()
        t.circle(4*scale)
        t.end_fill()


def fleur(position, taille, t):
    x, y = position

    couleurs_petales = [
        "#FF69B4",  # rose
        "#FFD700",  # jaune
        "#FF6347",  # rouge
        "#9370DB",  # violet
        "#FFA500",  # orange
        "#00CED1"   # turquoise
    ]

    couleur_petale = random.choice(couleurs_petales)

    # Tige
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.color("darkgreen")
    t.pendown()
    t.width(max(1, int(taille / 4)))
    t.forward(20 * taille)

    

    # Pétales
    t.color(couleur_petale)
    for angle in range(0, 360, 60):
        t.penup()
        t.goto(x, y + 20 * taille)
        t.setheading(angle)
        t.forward(5 * taille)
        t.pendown()
        t.begin_fill()
        t.circle(4 * taille)
        t.end_fill()

    t.width(1)

    # Centre de la fleur
    t.penup()
    t.goto(x, y + 20 * taille)
    t.color("#FFD700")
    t.pendown()
    t.begin_fill()
    t.circle(3 * taille)
    t.end_fill()


t = Turtle()
t.hideturtle()
screen = Screen()
screen.tracer(0)


arbre_classique(t, -300, -50, 1)
arbre_large(t, -100, -50, 1)
arbre_fruitier(t, 100, -50, 1)
arbre_classique(t, 300, -50, 1)

for _ in range(5):
    fx = random.randint(-400, 400)
    fy = random.randint(-300, -150)
    fleur((fx, fy), 2*random.uniform(0.5, 1.2), t)

screen.update()

done()
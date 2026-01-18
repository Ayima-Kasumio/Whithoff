import turtle
import math

# --- Helpers ---
def _goto(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()

def _filled_circle(t, x, y, r, color):
    t.up()
    t.goto(x, y - r)
    t.setheading(0)
    t.down()
    t.color("black", color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.up()

def _filled_polygon(t, points, color):
    if not points:
        return
    t.up()
    t.goto(points[0])
    t.down()
    t.color("black", color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()
    t.up()

def _line(t, p1, p2, width=1, color="black"):
    t.color(color)
    t.width(width)
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.up()
    t.width(1)

# --- Lapin ---
def dessiner_lapin(position, scale, t, *,
                   couleur="lightgray", yeux_color="black", orientation=1):
    """
    Dessine un lapin simple et mignon.
    position: (x,y) base du corps
    scale: facteur de taille
    t: turtle.Turtle
    orientation: 1 pour regarder vers la droite, -1 pour gauche
    """
    x, y = position
    s = scale

    # Corps
    body_r = 22 * s
    _filled_circle(t, x, y + body_r*0.2, body_r, couleur)

    # Queue (petite boule derrière)
    tail_r = 8 * s
    tail_x = x - orientation * (body_r * 0.9)
    _filled_circle(t, tail_x, y + body_r*0.3, tail_r, "white")

    # Tête
    head_r = 14 * s
    head_x = x + orientation * (body_r * 0.5)
    head_y = y + body_r * 0.9
    _filled_circle(t, head_x, head_y, head_r, couleur)

    # Oreilles (deux polygones allongés)
    ear_w = 8 * s
    ear_h = 32 * s
    # oreille gauche (vue du lapin)
    ear1 = [
        (head_x - orientation * 6*s, head_y + head_r*0.6),
        (head_x - orientation * 6*s - orientation * ear_w, head_y + head_r*0.6 + ear_h*0.15),
        (head_x - orientation * 2*s - orientation * ear_w/2, head_y + head_r*0.6 + ear_h),
        (head_x - orientation * 2*s, head_y + head_r*0.6 + ear_h*0.5),
    ]
    # oreille droite
    ear2 = [
        (head_x + orientation * 6*s, head_y + head_r*0.6),
        (head_x + orientation * 6*s + orientation * ear_w, head_y + head_r*0.6 + ear_h*0.15),
        (head_x + orientation * 2*s + orientation * ear_w/2, head_y + head_r*0.6 + ear_h),
        (head_x + orientation * 2*s, head_y + head_r*0.6 + ear_h*0.5),
    ]
    _filled_polygon(t, ear1, couleur)
    _filled_polygon(t, ear2, couleur)
    # intérieurs d'oreille
    inner_ear_color = "pink"
    inner_scale = 0.65
    ear1_inner = [(head_x - orientation * 6*s + (p[0]- (head_x - orientation * 6*s))*inner_scale,
                   head_y + head_r*0.6 + (p[1] - (head_y + head_r*0.6))*inner_scale) for p in ear1]
    ear2_inner = [(head_x + orientation * 6*s + (p[0]- (head_x + orientation * 6*s))*inner_scale,
                   head_y + head_r*0.6 + (p[1] - (head_y + head_r*0.6))*inner_scale) for p in ear2]
    _filled_polygon(t, ear1_inner, inner_ear_color)
    _filled_polygon(t, ear2_inner, inner_ear_color)

    # Yeux
    eye_r = 2.6 * s
    eye_x = head_x + orientation * (head_r * 0.35)
    eye_y = head_y + head_r*0.22
    _filled_circle(t, eye_x, eye_y, eye_r, yeux_color)
    # Petit éclat
    _filled_circle(t, eye_x + (-orientation)*eye_r*0.4, eye_y + eye_r*0.4, eye_r*0.45, "white")

    # Nez
    nose_r = 2.6 * s
    nose_x = head_x + orientation * (head_r*0.6)
    nose_y = head_y - head_r*0.05
    _filled_circle(t, nose_x, nose_y, nose_r, "pink")

    # Moustaches
    whisk_len = 18 * s
    for sign in (-1, 1):
        start = (nose_x - orientation*1.5*s, nose_y + 0.5*sign*s)
        end = (start[0] + orientation * whisk_len, start[1] + sign * 3*s)
        _line(t, start, end, width=1, color="black")

    # Pattes avant (deux petits arcs ou ellipses)
    paw_w = 8 * s
    paw_h = 6 * s
    paw1_center = (x + orientation * 6*s, y + paw_h)
    paw2_center = (x + orientation * 0*s, y + paw_h)
    _filled_circle(t, paw1_center[0], paw1_center[1], paw_w/2, couleur)
    _filled_circle(t, paw2_center[0], paw2_center[1], paw_w/2, couleur)

# --- Oiseau ---
def dessiner_oiseau(position, scale, t, *,
                    couleur="orange", aile_color=None, yeux_color="black",
                    orientation=1):
    """
    Dessine un oiseau simple.
    position: (x,y) centre du corps
    scale: facteur de taille
    t: turtle.Turtle
    orientation: 1 pour regarder vers la droite, -1 pour gauche
    """
    x, y = position
    s = scale
    if aile_color is None:
        aile_color = couleur

    # Corps (ovale approximé par deux cercles superposés)
    body_r = 14 * s
    _filled_circle(t, x, y, body_r, couleur)
    # petit "poitrine" pour l'ovale
    _filled_circle(t, x - orientation * (body_r*0.35), y - body_r*0.15, body_r*0.85, couleur)

    # Aile (forme en goutte)
    wing = [
        (x - orientation * 2*s, y + 2*s),
        (x - orientation * (body_r*0.2), y + body_r*0.9),
        (x + orientation * (body_r*0.9), y + body_r*0.2),
        (x - orientation * (body_r*0.2), y - body_r*0.4),
    ]
    _filled_polygon(t, wing, aile_color)

    # Bec (triangle)
    beak_len = 10 * s
    beak = [
        (x + orientation * (body_r + 2*s), y + 3*s),
        (x + orientation * (body_r + beak_len), y + 1.5*s),
        (x + orientation * (body_r + 2*s), y - 0.5*s),
    ]
    _filled_polygon(t, beak, "yellow")

    # Oeil
    eye_r = 2.2 * s
    eye_x = x + orientation * (body_r*0.6)
    eye_y = y + body_r*0.35
    _filled_circle(t, eye_x, eye_y, eye_r, yeux_color)
    _filled_circle(t, eye_x + (-orientation)*eye_r*0.4, eye_y + eye_r*0.4, eye_r*0.5, "white")

    # Queue (petits traits ou triangles)
    tail_len = 12 * s
    tail_pts = [
        (x - orientation*(body_r + 2*s), y - 1*s),
        (x - orientation*(body_r + tail_len*0.6), y - 4*s),
        (x - orientation*(body_r + tail_len), y + 3*s),
    ]
    _filled_polygon(t, tail_pts, couleur)

    # Pattes (deux traits simples)
    leg_y = y - body_r - 3*s
    left_leg_x = x - orientation * 4*s
    right_leg_x = x + orientation * 0*s
    _line(t, (left_leg_x, leg_y), (left_leg_x, leg_y - 10*s), width=2, color="sienna")
    _line(t, (right_leg_x, leg_y), (right_leg_x, leg_y - 10*s), width=2, color="sienna")

# --- Exemple d'utilisation ---
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(900, 600)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Dessiner quelques lapins et oiseaux
    dessiner_lapin((-200, -100), 1.2, t, couleur="lightgray", yeux_color="darkblue", orientation=1)
    dessiner_lapin((-120, -120), 0.9, t, couleur="white", yeux_color="black", orientation=-1)
    dessiner_oiseau((80, -20), 1.1, t, couleur="deepskyblue", aile_color="dodger blue", orientation=1)
    dessiner_oiseau((160, 20), 0.8, t, couleur="coral", aile_color="lightcoral", orientation=-1)

    # Laisser la fenêtre ouverte
    screen.mainloop()
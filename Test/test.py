"""
Dessins "réalistes" (simplifiés) pour Turtle :
- dessiner_lapin_realiste(position, scale, t, ...)
- dessiner_oiseau_realiste(position, scale, t, ...)

Ces fonctions utilisent des ellipses remplies (approximées par polygones)
pour obtenir des formes douces et naturelles. Options pour orientation,
couleurs et petites ombres pour donner du volume.
"""
import turtle
import math

# ---------- Helpers ----------
def _poly_from_ellipse(cx, cy, rx, ry, rotation_deg=0, steps=60):
    rot = math.radians(rotation_deg)
    pts = []
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        x = rx * math.cos(theta)
        y = ry * math.sin(theta)
        # rotate
        xr = x * math.cos(rot) - y * math.sin(rot)
        yr = x * math.sin(rot) + y * math.cos(rot)
        pts.append((cx + xr, cy + yr))
    return pts

def _filled_polygon_from_points(t, points, fillcolor, outline="black"):
    if not points:
        return
    t.up()
    t.goto(points[0])
    t.down()
    t.color(outline, fillcolor)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()
    t.up()

def _filled_ellipse(t, cx, cy, rx, ry, rotation_deg=0, fillcolor="black", outline="black", steps=60):
    pts = _poly_from_ellipse(cx, cy, rx, ry, rotation_deg, steps)
    _filled_polygon_from_points(t, pts, fillcolor, outline)

def _line(t, p1, p2, width=1, color="black"):
    t.color(color)
    t.width(width)
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.up()
    t.width(1)

# ---------- Oiseau réaliste ----------
def dessiner_oiseau_realiste(position, scale, t,
                             couleur="#f4a261", ventre_color="#fff2e6",
                             aile_color=None, yeux_color="black",
                             orientation=1, ombre_color="#cfa77a"):
    """
    Dessine un oiseau plus lisse et "réaliste" (formes elliptiques pour corps & aile).
    position: (x,y) centre du corps
    scale: facteur de taille
    orientation: 1 = regard à droite, -1 = gauche
    """
    x, y = position
    s = scale
    if aile_color is None:
        aile_color = couleur

    # Corps (ellipse légèrement verticale)
    body_rx = 28 * s
    body_ry = 20 * s
    body_cx = x
    body_cy = y
    _filled_ellipse(t, body_cx + 4*s*orientation, body_cy - 4*s, body_rx*0.98, body_ry*0.9, rotation_deg=0,
                    fillcolor=ombre_color, outline=ombre_color, steps=80)
    _filled_ellipse(t, body_cx, body_cy, body_rx, body_ry, rotation_deg=12*orientation, fillcolor=couleur, outline="black", steps=100)

    # Ventre plus clair (ellipse chevauchante)
    _filled_ellipse(t, body_cx - 4*s*orientation, body_cy - 6*s, body_rx*0.64, body_ry*0.6, rotation_deg=12*orientation,
                    fillcolor=ventre_color, outline=ventre_color, steps=80)

    # Aile (ellipse plus large et inclinée)
    wing_cx = body_cx - orientation * (6 * s)
    wing_cy = body_cy + 4 * s
    wing_rx = 20 * s
    wing_ry = 12 * s
    _filled_ellipse(t, wing_cx, wing_cy, wing_rx, wing_ry, rotation_deg=32*orientation, fillcolor=aile_color, outline="black", steps=90)
    # Petite ombre sur l'aile
    _filled_ellipse(t, wing_cx + 6*s*orientation, wing_cy - 2*s, wing_rx*0.6, wing_ry*0.5, rotation_deg=32*orientation,
                    fillcolor=ombre_color, outline=ombre_color, steps=60)

    # Tête (petite ellipse)
    head_rx = 12 * s
    head_ry = 11 * s
    head_cx = body_cx + orientation * (body_rx * 0.7)
    head_cy = body_cy + 6 * s
    _filled_ellipse(t, head_cx, head_cy, head_rx, head_ry, rotation_deg=0, fillcolor=couleur, outline="black", steps=80)

    # Bec (légèrement courbé : deux petits triangles / polygones pour douceur)
    beak_len = 14 * s
    beak_w = 7 * s
    beak_tip = (head_cx + orientation * (head_rx + beak_len), head_cy)
    beak_base_top = (head_cx + orientation * (head_rx * 0.6), head_cy + 3*s)
    beak_base_bot = (head_cx + orientation * (head_rx * 0.6), head_cy - 3*s)
    _filled_polygon_from_points(t, [beak_base_top, beak_tip, beak_base_bot], "yellow", outline="black")

    # Oeil (iris et reflet)
    eye_rx = 3.6 * s
    eye_ry = 3.6 * s
    eye_cx = head_cx + orientation * (head_rx * 0.25)
    eye_cy = head_cy + 2 * s
    _filled_ellipse(t, eye_cx, eye_cy, eye_rx, eye_ry, 0, fillcolor=yeux_color, outline=yeux_color, steps=36)
    _filled_ellipse(t, eye_cx - orientation*1.1*s, eye_cy + 1.0*s, eye_rx*0.45, eye_ry*0.45, 0, fillcolor="white", outline="white", steps=18)

    # Queue : plusieurs petites ellipses inclinées
    tail_base_x = body_cx - orientation * (body_rx + 6*s)
    tail_base_y = body_cy - 2 * s
    for i in range(3):
        trx = 8 * s * (1 - i*0.12)
        tryy = 4.5 * s * (1 + i*0.05)
        angle = -20 + i * 20
        _filled_ellipse(t, tail_base_x - i*4*s*orientation, tail_base_y + i*2*s, trx, tryy, rotation_deg=angle*orientation,
                        fillcolor=couleur, outline="black", steps=40)

    # Pattes (lignes fines)
    leg_y = body_cy - body_ry - 6 * s
    left_leg_x = body_cx - 6*s
    right_leg_x = body_cx + 2*s
    _line(t, (left_leg_x, leg_y), (left_leg_x, leg_y - 14*s), width=2, color="#8b5a2b")
    _line(t, (right_leg_x, leg_y), (right_leg_x, leg_y - 14*s), width=2, color="#8b5a2b")

# ---------- Exemple d'utilisation ----------
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(1000, 700)
    screen.title("Lapin et Oiseau réalistes (Turtle)")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Fond clair
    screen.bgcolor("#eaf6ff")

    # Exemple : plusieurs instances
    dessiner_oiseau_realiste((140, -40), 1.1, t, couleur="#ff8a65", ventre_color="#fff4ea", orientation=1)
    dessiner_oiseau_realiste((240, 20), 2, t, couleur="#6fb3d2", aile_color="#4aa1c7", orientation=-1)

    screen.mainloop()
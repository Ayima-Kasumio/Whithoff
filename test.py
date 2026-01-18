"""
Megemont Aymeric
Sarfati Enzo
"""

import random
import math
import turtle

# Fonction existante (conservée)
def dessiner_triangle_isocele(position, longeur, hauteur, color, t):
    t.up()
    t.goto(position[0]-longeur//2, position[1])
    t.down()
    t.color("black", color)
    t.begin_fill()
    t.goto(position[0]+longeur//2, position[1])
    t.goto(position[0], position[1]+hauteur)
    t.goto(position[0]-longeur//2, position[1])
    t.end_fill()

# --- NOUVELLES FONCTIONS POUR MONTAGNE PLUS RÉALISTE ---

def _draw_filled_polygon(t, points, fillcolor, outline="black"):
    """Dessine un polygone plein donné par la liste de points [(x,y), ...]."""
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

def _interpolate(p1, p2, y_target):
    """Retourne le point d'intersection sur le segment p1-p2 avec la ligne y = y_target."""
    (x1, y1), (x2, y2) = p1, p2
    if y1 == y2:
        return (x1, y1)
    t = (y_target - y1) / (y2 - y1)
    x = x1 + t * (x2 - x1)
    return (x, y_target)

def _extract_snow_polygon(top_points, base_y, snow_threshold_y):
    """
    Découpe la partie supérieure (crête) où y >= snow_threshold_y
    et renvoie un polygone pour la neige (avec interpolation aux intersections).
    top_points doit être la liste ordonnée de la bordure supérieure gauche->droite.
    """
    poly = []
    n = len(top_points)
    for i in range(n - 1):
        p = top_points[i]
        q = top_points[i+1]
        if p[1] >= snow_threshold_y:
            poly.append(p)
        # si segment traverse la ligne de seuil, ajouter le point d'intersection
        if (p[1] < snow_threshold_y and q[1] > snow_threshold_y) or (p[1] > snow_threshold_y and q[1] < snow_threshold_y):
            inter = _interpolate(p, q, snow_threshold_y)
            poly.append(inter)
    # vérifier le dernier point
    if top_points and top_points[-1][1] >= snow_threshold_y:
        poly.append(top_points[-1])
    # si poly vide, renvoyer None
    if not poly:
        return None
    # ajouter les deux points bas qui ferment la forme (projeter vers base_y)
    left = (poly[0][0], base_y)
    right = (poly[-1][0], base_y)
    full = [left] + poly + [right]
    return full

def dessiner_montagne(position, largeur, hauteur, t, *,
                       n_dents=8, rugosite=0.35, neige=0.18,
                       couleur_base="saddle brown", couleur_ombre="sienna", seed=None):
    """
    Dessine une montagne non-triangle avec une crête irrégulière et un capuchon de neige.
    position: (x,y) base centrale
    largeur, hauteur: taille de la montagne
    t: turtle.Turtle
    n_dents: nombre de points le long de la crête (plus = plus détaillé)
    rugosite: amplitude relative des irrégularités (0..1)
    neige: fraction de la hauteur occupée par la neige au sommet (0..0.5 typiquement)
    couleur_base: couleur principale
    couleur_ombre: couleur plus sombre pour l'ombre/face
    seed: int pour rendre le résultat reproductible (ou None)
    """
    if seed is not None:
        random.seed(seed)

    cx, cy = position
    left_x = cx - largeur / 2
    right_x = cx + largeur / 2
    base_y = cy
    peak_y = cy + hauteur

    # Générer la crête (liste de points du bord supérieur de gauche à droite)
    # On s'assure qu'il y a un sommet principal près du centre.
    # x_positions régulièrement espacées
    xs = [left_x + i * (largeur / (n_dents - 1)) for i in range(n_dents)]
    top_points = []
    for i, x in enumerate(xs):
        # distance relative au centre (0 au centre -> sommet plus haut)
        dx_norm = abs((x - cx) / (largeur / 2))
        # hauteur de base pour ce x : courbe en V inversé (pic au centre)
        base_h = peak_y - (hauteur * (dx_norm))
        # ajouter irrégularité aléatoire (proportionnelle à la hauteur restante)
        rand_amp = rugosite * hauteur * (1 - dx_norm)  # moins d'irrégularité vers la base
        y = base_h - random.uniform(-rand_amp, rand_amp)
        # limiter entre base_y et peak_y
        y = max(base_y, min(peak_y, y))
        top_points.append((x, y))

    # Construire le polygone de la montagne en partant de la base gauche, autour de la crête, jusqu'à la base droite
    poly = []
    poly.append((left_x, base_y))
    poly.extend(top_points)
    poly.append((right_x, base_y))

    # Remplir la montagne principale
    _draw_filled_polygon(t, poly, couleur_base, outline="black")

    # Ombre: dessiner une face (par ex. côté droit) légèrement décalée et plus sombre pour donner du volume
    # On prend la moitié droite de la crête et la ferme vers la base droite.
    mid_index = len(top_points) // 2
    right_face = [(cx, peak_y)]  # commencer au sommet visuel
    # ajouter points de la crête du centre -> droite
    right_face.extend(top_points[mid_index:])
    right_face.append((right_x, base_y))
    right_face.append((cx, base_y))  # rabattre vers le centre-bas
    _draw_filled_polygon(t, right_face, couleur_ombre, outline="black")

    # Capuchon de neige: découper la zone au-dessus d'un seuil
    seuil_y = base_y + hauteur * (1 - neige)  # tout ce qui est au-dessus aura de la neige
    snow_poly = _extract_snow_polygon(top_points, base_y, seuil_y)
    if snow_poly:
        # couleur neige
        _draw_filled_polygon(t, snow_poly, "white", outline="light gray")

    # Optionnel: texture légère (traits horizontaux courts) pour simuler roches/hachures
    t.color("black")
    t.width(1)
    for (x, y) in top_points[1:-1]:
        # dessiner de petits traits verticaux/obliques sous la crête
        length = max(4, hauteur * 0.03)
        angle = random.uniform(-25, 25)
        t.up()
        t.goto(x, y - 3)
        t.setheading(-90 + angle)
        t.down()
        t.forward(length)
        t.up()

# Exemple d'utilisation (commenter/décommenter selon besoin)
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(800, 600)
    t = turtle.Turtle()
    t.speed(0)

    # dessiner plusieurs montagnes superposées pour profondeur
    dessiner_montagne((0, -100), 520, 300, t, n_dents=12, rugosite=0.28, neige=0.16, seed=42)
    dessiner_montagne((-220, -140), 360, 220, t, n_dents=10, rugosite=0.30, neige=0.12, couleur_base="saddlebrown", couleur_ombre="brown", seed=1)
    dessiner_montagne((220, -160), 300, 180, t, n_dents=8, rugosite=0.20, neige=0.10, couleur_base="sienna", couleur_ombre="peru", seed=7)

    t.hideturtle()
    screen.mainloop()
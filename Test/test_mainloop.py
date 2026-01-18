"""
Exemple pour comprendre `turtle.mainloop()` (avec commentaires en français).

Usage:
  - Lancer: `python3 Test/test_mainloop.py`
  - Optionnel: `python3 Test/test_mainloop.py --keep-open` pour empêcher la fermeture automatique.

Explication rapide:
  - `mainloop()` démarre la boucle d'événements de Turtle (boucle principale).
  - Elle bloque l'exécution du script jusqu'à ce que la fenêtre soit fermée (ou jusqu'à appel de `bye()`).
  - On peut attacher des événements (clics, touches, timers) qui seront gérés pendant cette boucle.
"""

import argparse
import turtle


def dessiner_carre(t, taille=100):
    for _ in range(4):
        t.forward(taille)
        t.left(90)


def main(keep_open: bool):
    # Création de l'écran et d'une tortue
    screen = turtle.Screen()
    screen.title("Demo turtle.mainloop()")
    t = turtle.Turtle()

    # Dessine un carré
    dessiner_carre(t, 120)

    # Exemple d'événement: au clic, afficher les coordonnées dans la console
    def on_click(x, y):
        print(f"Clic détecté aux coordonnées: ({x:.1f}, {y:.1f})")

    screen.onclick(on_click)

    # Option: fermer automatiquement après 3 secondes si l'utilisateur ne demande pas de garder ouvert
    if not keep_open:
        screen.ontimer(screen.bye, 6000)  # ferme la fenêtre après 3000 ms

    # Démarre la boucle d'événements
    # Tant que mainloop tourne, les événements (clics, timers...) sont traités.
    screen.mainloop()


main(True)

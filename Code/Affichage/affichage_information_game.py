def affichage_information_game(t, liste_objet_initiale, joueur, last_play):
    t.clear()
    t.up()
    t.goto(-860, 440)
    t.write("Jeu de Whithoff",False,"center", ("Arial", 12, "normal"))

    t.goto(-860, 390)
    t.write("C'est au tour de " + joueur,False,"center", ("Arial", 12, "normal"))

    for i in range(len(liste_objet_initiale[2])):
        t.goto(-860, 340-30*i)
        t.write("Il reste "+ str(liste_objet_initiale[1][i]) +" " +liste_objet_initiale[2][i],False,"center", ("Arial", 12, "normal"))



    t.goto(-860, 100)
    t.write(last_play,False,"center", ("Arial", 12, "normal"))

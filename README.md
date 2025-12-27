A python project where we create a mini game called Whithoff for a school homework at Polytech Nice-Sophia (Peip1 2025-2026)






t_background = Turtle()
t_background.speed()
t_background.hideturtle()
screen = Screen()
t_background.speed(0)

taille = 200

t_background.up()
t_background.goto(0,0)
t_background.down()
t_background.write("0,0")

dessiner_table((0,0), taille, t_background)

done()
import turtle
wn = turtle.Screen()

def fxn(x, y):
    turtle.goto(x, y)
    turtle.write(str(x) + "," + str(y))

wn.onclick(fxn)
wn.mainloop()

turtle.done()
def dessiner_scoreboard(t):
    t.color("black", "#ff8800")
    t.up()
    t.goto(-960,540)
    t.down()
    
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(1080)
        t.right(90)
    t.end_fill()


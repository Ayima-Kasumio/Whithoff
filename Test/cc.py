import turtle

screen = turtle.Screen()
screen.setup(900, 600)

class Page:
    def __init__(self):
        self.turtles = []

    def show(self): pass
    def hide(self):
        for t in self.turtles:
            t.clear()
            t.hideturtle()
        self.turtles = []

    def handle_click(self, x, y): pass
    def on_key(self, key): pass

current = None
def switch_page(new_page):
    global current
    if current:
        current.hide()
    current = new_page
    # rebind global handlers to current page
    screen.onclick(current.handle_click)
    screen.onkey(lambda: current.on_key('space'), 'space')
    current.show()

# Menu page
class MenuPage(Page):
    def __init__(self):
        super().__init__()
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.turtles.append(self.t)

    def show(self):
        self.t.up(); self.t.goto(0, 50)
        self.t.write("My Game", align='center', font=('Arial', 24, 'bold'))
        self.t.goto(0, -10)
        self.t.write("Click to start", align='center', font=('Arial', 16, 'normal'))

    def handle_click(self, x, y):
        # simple area check or just start
        switch_page(GamePage())

# Game page
class GamePage(Page):
    def __init__(self):
        super().__init__()
        self.bg = turtle.Turtle()
        self.bg.hideturtle()
        self.turtles.append(self.bg)
        self.running = False

    def show(self):
        self.bg.up(); self.bg.goto(-200, 100)
        self.bg.write("Game running... press Escape to return", font=('Arial', 12))
        self.running = True
        self._tick()

    def _tick(self):
        if not self.running: 
            return
        # game update work here
        # schedule next frame
        screen.ontimer(self._tick, 100)  # 10 fps

    def handle_click(self, x, y):
        print("Game click at", x, y)

    def on_key(self, key):
        if key == 'escape':
            self.running = False
            switch_page(MenuPage())

# Start app
switch_page(MenuPage())
screen.listen()
screen.mainloop()
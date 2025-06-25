import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red','blue','green','yellow','orange','purple','pink','brown','black','cyan']


def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("Enter number of turtles (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!")           
           
def create_turtles(colors):
    turtles = []
    sapcingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * sapcingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles
      
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance) 
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
    
racers = get_number_of_turtles()    
init_turtle() 
random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)

winner = race(colors)
print("The winner is",winner)
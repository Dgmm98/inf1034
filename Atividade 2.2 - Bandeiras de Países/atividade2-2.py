from turtle import *
from random import randint

t = Turtle()
t.speed(8)
def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()

def poligono_generico(a,b,c,d,e):
    t.teleport(a,b)
    t.begin_fill()
    t.fillcolor(c)
    for i in range(e):
        t.forward(d)
        t.left(360/e)
    t.end_fill()

def japao():
    desenha_retangulo(-100, 50, 200, 100, "white")
    t.teleport(0, -30)
    t.begin_fill()
    t.fillcolor("red")
    t.circle(30)
    t.end_fill()

def alemanha():
    desenha_retangulo(-100, 50, 200, 33.3, "black")
    desenha_retangulo(-100, 16.7, 200, 33.3, "red")
    desenha_retangulo(-100, -16.6, 200, 33.3, "yellow")

def brasil():
    desenha_retangulo(-100, 50, 200, 100, "green")
    t.left(-90)
    poligono_generico(0, 40, "yellow", 70, 3)
    t.left(180)
    poligono_generico(0, -30, "yellow", 70, 3)
    t.left(-90)
    t.begin_fill()
    t.fillcolor("blue")
    t.teleport(0,-15)
    t.circle(20)
    t.end_fill()
    t.teleport(100,100)
    
def turquia():
    t.color("red")
    desenha_retangulo(-100, 50, 200, 100, "red")
    t.left(90)
    t.teleport(-30, 0)
    t.begin_fill()
    t.fillcolor("white")
    t.color("white")
    t.circle(30)
    t.end_fill()
    t.begin_fill()
    t.color("red")
    t.fillcolor("red")
    t.teleport(-28, 0)
    t.circle(22)
    t.end_fill()
    t.teleport(-10, 10)
    t.begin_fill()
    t.fillcolor("white")
    t.color("white")
    for i in range(5):
        t.forward(10)
        t.left(126)
        t.forward(10)
        t.right(50)
    t.end_fill()

def niger():
    desenha_retangulo(-100, 50, 200, 33.3, "orange")
    desenha_retangulo(-100, 16.7, 200, 33.3, "white")
    desenha_retangulo(-100, -16.6, 200, 33.3, "green")
    t.begin_fill()
    t.color("orange")
    t.fillcolor("orange")
    t.teleport(0, -10)
    t.circle(10)
    t.end_fill()

def noruega():
    t.color("dark red")
    desenha_retangulo(-100, 50, 200, 100, "dark red")
    t.color("white")
    desenha_retangulo(-100, 15, 200, 30, "white")
    t.left(-90)
    desenha_retangulo(-30, 50, 100, 30, "white")
    t.color("dark blue")
    desenha_retangulo(-38, 50, 100, 15, "dark blue")
    t.left(90)
    desenha_retangulo(-100, 10, 200, 15, "dark blue")

noruega()

mainloop()
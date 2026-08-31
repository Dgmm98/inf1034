from turtle import *

varcolor1 = textinput("Cor","Qual a cor da primeira forma? ")
# varcolor2 = textinput("Cor","Qual a cor da segunda forma? ")
coordenadas = numinput("Coordenada","Qual o tamanho da coordenada?(em pixel) ")

t = Turtle()
t.shape("turtle")
# posicao_definida = {"primeira":(100,100),"segunda":(-100,100),"terceira":(-100,-100)}

def plano(a):
    t.teleport(0,0)
    t.goto(a,0)
    t.stamp()
    t.left(180)
    t.goto(-a,0)
    t.stamp()
    t.left(90)
    t.teleport(0,0)
    t.goto(0,a)
    t.stamp()
    t.left(180)
    t.goto(0,-a)
    t.stamp()

plano(coordenadas)
t.teleport(200,200)
t.color("Orange")
t.fillcolor(varcolor1)
t.begin_fill()
for cont in range(8):
    t.forward(50)
    t.left(45)
t.end_fill()

t.teleport(-200,200)
t.fillcolor(varcolor1)
t.begin_fill()
for cont in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

t.teleport(-200,-200)
t.fillcolor(varcolor1)
t.begin_fill()
for cont in range(3):
    t.forward(50)
    t.left(120)
t.end_fill()

t.teleport(200,-200)
t.fillcolor(varcolor1)
t.begin_fill()
for cont in range(10):
    t.forward(50)
    t.left(40)
t.end_fill()
t.right(90)
t.teleport(0,0)
for i in range (30):
    t.forward(30+i)
    t.left(30)


mainloop()
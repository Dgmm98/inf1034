from turtle import *
from random import randint

# varcolor1 = textinput("Cor","Qual a cor da primeira forma? ")
#coordenadas = int(numinput("Coordenada","Qual o tamanho da coordenada?(em pixel) "))
coordenada1 = randint(20,400)
coordenada2 = randint(20,400)
#tamanho = numinput("Tamanho","Qual tamanho do poligono?(em pixel) ")
quant_lados = int(numinput("Lados","Quantos lados deve ter esse poligono? "))
t = Turtle()
t.shape("turtle")

def plano(a,b):
    t.teleport(0,0)
    t.goto(a,0)
    t.stamp()
    t.left(180)
    t.goto(-a,0)
    t.stamp()
    t.left(90)
    t.teleport(0,0)
    t.goto(0,b)
    t.stamp()
    t.left(180)
    t.goto(0,-b)
    t.stamp()

def poligono_generico(a,b,c,d,e):
    t.teleport(a,b)
    t.color(c)
    for i in range(e):
        t.forward(d)
        t.left(360/e)

plano(400,400)
poligono_generico(coordenada1,coordenada2,"red",30,quant_lados)
poligono_generico(-coordenada1,-coordenada2,"red",30,quant_lados+1)
poligono_generico(-coordenada1,coordenada2,"red",30,quant_lados+2)
poligono_generico(coordenada1,-coordenada2,"red",30,quant_lados+3)



mainloop()
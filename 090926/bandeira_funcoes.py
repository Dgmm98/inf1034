from turtle import *
from time import sleep

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

def desenha_bandeira_franca():
    desenha_retangulo(-200, 200, 50, 150, "#002153")
    desenha_retangulo(-150, 200, 50, 150, "white")
    desenha_retangulo(-100, 200, 50, 150, "#CF0921")

def desenha_bandeira_japao():
    desenha_retangulo(0,0,100,60,"white")
    t.begin_fill()
    t.fillcolor("Red")
    t.teleport(50,-45)
    t.circle(15)
    t.end_fill()


t = Turtle()

nome_pais = textinput("Escolha um país para desenhar a bandeira","")
paises = {"japao": desenha_bandeira_japao, "frança": desenha_bandeira_franca}
for k in paises:
    if nome_pais.lower() == k:
        desenha = paises[k]
        desenha()

sleep(1)
mainloop()
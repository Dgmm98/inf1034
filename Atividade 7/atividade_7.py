from pygame import *
from random import randint


def desenho_dos_campos(a = str):
    campos = a.split
    caracteres = campos.count()
    # for i in range(caracteres):
    # draw.line(tela,"#ffffff",((800/cacacteres)+caracteres,500),((800/cacacteres)+caracteres,500),15)

init()
tela = display.set_mode((800,600))
running = True
portugues = ["substantivo","artigo","pronome","adjeivo","verbo"]
filme = ["Monstros SA", "King Kong","John Wick","Logan"]
livros = ["Harry Potter","As cronicas de Narnia","A Rainha Vermelha"]
temas = [portugues,filme,livros]
tema_escolhido = temas[randint(0,2)]
palavra_escolhida = tema_escolhido[randint(0,len(tema_escolhido))]

print(palavra_escolhida)



while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    draw.line(tela,"#ffffff",(50,100),(50,400),15)
    draw.line(tela,"#ffffff",(43,100),(170,100),10)
    draw.circle(tela,"white",(170,140),30,5)
    draw.line(tela,"#ffffff",(170,170),(170,300),6)
    draw.line(tela,"#ffffff",(170,190),(230,220),6)
    draw.line(tela,"#ffffff",(170,190),(110,220),6)
    draw.line(tela,"#ffffff",(170,300),(230,360),6)
    draw.line(tela,"#ffffff",(170,300),(110,360),6)

    draw.line(tela,"#ffffff",(250,500),(400,500),15)

    display.update()
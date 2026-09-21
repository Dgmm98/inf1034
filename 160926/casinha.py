from pygame import *

init()
screen = display.set_mode((1280,720))

#recurso
imagem = image.load("dante.png")
imagem = transform.scale(imagem, (120,120))

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    
    screen.fill('#5c0b6e')
    draw.rect(screen,"#034a0f",(0,650,1280,100))
    draw.rect(screen,"#7a4a0a",(300,450,200,200))
    #porta
    draw.rect(screen,"#5e3e06",(430,535,50,115))
    draw.circle(screen,"#000000",(440,580),3)
    #janela
    draw.rect(screen,"#b37abf",(320,535,65,55))
    draw.rect(screen,"#c98206",(320,535,65,6))
    draw.rect(screen,"#c98206",(320,560,65,6))
    draw.rect(screen,"#c98206",(320,590,65,6))
    draw.rect(screen,"#c98206",(320,535,6,55))
    draw.rect(screen,"#c98206",(379,535,6,55))
    
    #sol
    draw.circle(screen,"#bd4d19",(150,150),50)
    draw.line(screen,"#bd4d19",(50,50),(250,250),5)
    draw.line(screen,"#bd4d19",(90,25),(200,275),5)


    screen.blit(imagem,(1100,550))
    display.update()
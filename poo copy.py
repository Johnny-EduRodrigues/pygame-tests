import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura_rect = 40
altura_rect = 50

largura = 640
altura = 480

relogio = pygame.time.Clock()

pontos = 10

x = largura/2
y = altura/2

velocidade = 10

x_verde = randint(40,600)
y_verde = randint(50,430)

fonte = pygame.font.SysFont('Arial', 40, True, False)
fonte_amarelo = pygame.font.SysFont('Arial', 20, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("RogueTrash")

mostrar_opção_amarelo = False
mostrar_opção_azul = False

while True:
    mensagem_pontos = f"Pontos restantes: {pontos}"
    mensagem_amarelo = f"+velocidade"
    mensagem_azul = f"+tamanho"
    tela.fill((0,0,0))
    relogio.tick(60)
    texto = fonte.render(mensagem_pontos, False, (255,255,255))
    texto_amarelo = fonte_amarelo.render(mensagem_amarelo, False, (255,255,255))  
    texto_azul = fonte_amarelo.render(mensagem_azul, False, (255,255,255))  
    if x>= largura:
        x = 0
    if y > altura:
        y = 0
    if x < 0:
        x = largura
    if y < 0:
        y = altura
        
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
    if pontos <= 0 and not mostrar_opção_amarelo:
        mostrar_opção_amarelo = True            

                
    if mostrar_opção_amarelo:
        option_yellow = pygame.draw.rect(tela, (255,255,0), (200,altura/2, 40, 50), 50)
        tela.blit(texto_amarelo, (170, 300))
        option_blue = pygame.draw.rect(tela, (0,0,255), (400,altura/2, 40, 50), 50)
        tela.blit(texto_azul, (370, 300))
        if rect_red.colliderect(option_blue):
            largura_rect += 6
            altura_rect += 6
            pontos = 10
            mostrar_opção_amarelo = False  
        if rect_red.colliderect(option_yellow):
            velocidade += 5
            pontos = 10
            mostrar_opção_amarelo = False

    if pygame.key.get_pressed()[K_a]:
        x -=velocidade
    if pygame.key.get_pressed()[K_d]:
        x +=velocidade
    if pygame.key.get_pressed()[K_w]:
        y -=velocidade
    if pygame.key.get_pressed()[K_s]:
        y +=velocidade
    rect_red = pygame.draw.rect(tela,(255,0,0), (x, y, largura_rect,altura_rect), 30)
    rect_green = pygame.draw.rect(tela, (0,255,0), (x_verde,y_verde,40,50), 50)
    if rect_red.colliderect(rect_green):
        x_verde = randint(40,600)
        y_verde = randint(50,430)
        pontos -= 1
    tela.blit(texto, (230, 40))
    pygame.display.update()
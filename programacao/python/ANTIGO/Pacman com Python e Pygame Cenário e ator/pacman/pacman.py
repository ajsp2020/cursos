import pygame
'''
- Colocando pixels:
Sitaxe: <objeto Surface>.set_at(<posição>,<cor>)

- Cículos: 
Sintaxe: pygame.draw.circle(<surface>,<cor>,<ponto central>,<raio>,<espessura>)

-Retangulos:
Sintaxe: pygame.draw.rect(<surface>,<cor>,(<x e y do ponto sup.esq>, <largura>,<altura>,<espessura>)

- Classe Rect:
r = pygame.rect(<x e y do ponto sup.esq>, <largura>,<altura>)
pygame.draw.rect(<surface>,<cor>,r,<espessura>)

- Polígonos
Sintaxe: pygame.draw.polygon(<surface>,<cor>,<lista de pontos>,<espessura>)
'''
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.1
RAIO = 20
pygame.init()


tela = pygame.display.set_mode((640, 480), 0)  # ((Tamanho da tela),    )
x = 10
y = 10
vel_x = VELOCIDADE
vel_y = VELOCIDADE

while True:

    #Calcula as regras
    x = x + vel_x
    y = y + vel_y
    
    if x + RAIO > 640:
        vel_x = -VELOCIDADE
    if x - RAIO < 0:
        vel_x = VELOCIDADE
    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    if y - RAIO < 0:
        vel_y = VELOCIDADE


    #Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), 20, 0) # (A tela, Cor do desenho, Posição do desenho, raio dp desenho, profundidade)
    pygame.display.update()


    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
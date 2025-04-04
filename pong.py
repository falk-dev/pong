import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong")

# Definir as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Definir os objetos do jogo
raquete_largura = 15
raquete_altura = 100
raquete_velocidade = 10

# Raquete da esquerda
raquete_esquerda = pygame.Rect(30, altura_tela // 2 - raquete_altura // 2, raquete_largura, raquete_altura)

# Raquete da direita
raquete_direita = pygame.Rect(largura_tela - 30 - raquete_largura, altura_tela // 2 - raquete_altura // 2, raquete_largura, raquete_altura)

# Bola
bola = pygame.Rect(largura_tela // 2 - 15, altura_tela // 2 - 15, 30, 30)
bola_velocidade_x = 7
bola_velocidade_y = 7

# Definir o relógio para controlar o FPS
relógio = pygame.time.Clock()

# Função para desenhar os elementos do jogo
def desenhar_tela():
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, raquete_esquerda)
    pygame.draw.rect(tela, BRANCO, raquete_direita)
    pygame.draw.ellipse(tela, BRANCO, bola)
    pygame.display.update()

# Função principal do jogo
def jogo():
    global bola_velocidade_x, bola_velocidade_y

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentação das raquetes
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and raquete_esquerda.top > 0:
            raquete_esquerda.y -= raquete_velocidade
        if teclas[pygame.K_s] and raquete_esquerda.bottom < altura_tela:
            raquete_esquerda.y += raquete_velocidade

        if teclas[pygame.K_UP] and raquete_direita.top > 0:
            raquete_direita.y -= raquete_velocidade
        if teclas[pygame.K_DOWN] and raquete_direita.bottom < altura_tela:
            raquete_direita.y += raquete_velocidade

        # Movimentação da bola
        bola.x += bola_velocidade_x
        bola.y += bola_velocidade_y

        # Verificar colisão com o topo e o fundo
        if bola.top <= 0 or bola.bottom >= altura_tela:
            bola_velocidade_y *= -1

        # Verificar colisão com as raquetes
        if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
            bola_velocidade_x *= -1

        # Verificar se a bola saiu da tela
        if bola.left <= 0 or bola.right >= largura_tela:
            bola.x = largura_tela // 2 - 15
            bola.y = altura_tela // 2 - 15
            bola_velocidade_x *= -1
            bola_velocidade_y *= -1

        # Atualizar a tela
        desenhar_tela()

        # Controlar a taxa de frames por segundo
        relógio.tick(60)

# Iniciar o jogo
jogo()

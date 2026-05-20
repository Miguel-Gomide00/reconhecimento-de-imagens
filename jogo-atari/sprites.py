# sprites.py
import pygame
import random
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, projectiles_group):
        super().__init__()
        self.image = pygame.Surface((TAMANHO_JOGADOR_X, TAMANHO_JOGADOR_Y))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 10
        self.velocidade_x = 0
        
        # Guardar referência aos grupos para poder atirar
        self.all_sprites = all_sprites
        self.projectiles_group = projectiles_group

    def update(self):
        self.velocidade_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocidade_x = -VELOCIDADE_JOGADOR
        if keys[pygame.K_RIGHT]:
            self.velocidade_x = VELOCIDADE_JOGADOR
        
        self.rect.x += self.velocidade_x
        
        # Manter o jogador dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        tiro = Projectile(self.rect.centerx, self.rect.top)
        self.all_sprites.add(tiro)
        self.projectiles_group.add(tiro)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TAMANHO_TIRO_X, TAMANHO_TIRO_Y))
        self.image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidade_y = VELOCIDADE_TIRO

    def update(self):
        self.rect.y += self.velocidade_y
        # Destruir se sair da tela
        if self.rect.bottom < 0:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, multiplicador_velocidade=1.0):
        super().__init__()
        tamanho = random.randint(TAMANHO_ASTEROIDE_MIN, TAMANHO_ASTEROIDE_MAX)
        self.image = pygame.Surface((tamanho, tamanho))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        
        # Posição inicial
        self.rect.x = random.randint(0, LARGURA - tamanho)
        self.rect.y = random.randint(-100, -40)
        
        vel_min = int(VELOCIDADE_ASTEROIDE_MIN * multiplicador_velocidade)
        vel_max = int(VELOCIDADE_ASTEROIDE_MAX * multiplicador_velocidade)
        self.velocidade_y = random.randint(vel_min, max(vel_min + 1, vel_max))

    def update(self):
        self.rect.y += self.velocidade_y

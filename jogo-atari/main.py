# main.py
import pygame
import sys
import random
from settings import *
from sprites import Player, Asteroid

def exibir_texto(tela, texto, tamanho, x, y, cor=BRANCO):
    fonte = pygame.font.SysFont("arial", tamanho, True)
    surface = fonte.render(texto, True, cor)
    rect = surface.get_rect()
    rect.midtop = (x, y)
    tela.blit(surface, rect)

def main():
    # Inicialização do Pygame
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo Atari - Clone")
    relogio = pygame.time.Clock()

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    projectiles_group = pygame.sprite.Group()

    # Criando jogador
    jogador = Player(all_sprites, projectiles_group)
    all_sprites.add(jogador)

    pontuacao = 0
    jogando = True
    game_over = False

    while jogando:
        relogio.tick(FPS)

        # 1. Tratamento de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False
            
            # Controle de tiro
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    jogador.shoot()
                if event.key == pygame.K_r and game_over:
                    # Reiniciar o jogo
                    return main()

        if not game_over:
            # Cálculo da dificuldade baseado na pontuação
            # A velocidade aumenta em 10% a cada 100 pontos
            multiplicador_vel = 1.0 + (pontuacao // 100) * 0.1
            
            # A frequência de spawn aumenta conforme os pontos, limite de 1 em 20 frames
            chance_atual = max(20, int(CHANCE_ASTEROIDE_INICIAL - (pontuacao // 5)))

            # 2. Geração de Asteroides
            if random.randrange(chance_atual) == 0:
                asteroide = Asteroid(multiplicador_vel)
                all_sprites.add(asteroide)
                asteroids_group.add(asteroide)

            # 3. Atualização dos Sprites
            all_sprites.update()

            # 4. Verificação de Colisões
            # Tiros colidindo com Asteroides
            colisoes_tiros_asteroides = pygame.sprite.groupcollide(asteroids_group, projectiles_group, True, True)
            for colisao in colisoes_tiros_asteroides:
                pontuacao += 10 # 10 pontos por asteroide

            # Nave colidindo com Asteroides
            colisao_nave_asteroide = pygame.sprite.spritecollide(jogador, asteroids_group, False)
            if colisao_nave_asteroide:
                game_over = True

            # Asteroides passando do fundo da tela
            for asteroide in asteroids_group:
                if asteroide.rect.top > ALTURA:
                    game_over = True

        # 5. Renderização (Desenho)
        tela.fill(PRETO)
        
        all_sprites.draw(tela)
        
        # Desenhar UI
        exibir_texto(tela, f"Pontos: {pontuacao}", 24, 80, 10)

        if game_over:
            exibir_texto(tela, "GAME OVER", 64, LARGURA // 2, ALTURA // 4, VERMELHO)
            exibir_texto(tela, "Pressione 'R' para reiniciar", 22, LARGURA // 2, ALTURA // 2)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

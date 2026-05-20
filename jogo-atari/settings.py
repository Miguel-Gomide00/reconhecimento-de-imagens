# settings.py
# Configurações do jogo

# Dimensões da tela
LARGURA = 800
ALTURA = 600

# Taxa de atualização (FPS)
FPS = 60

# Cores (R, G, B)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Configurações do Jogador
VELOCIDADE_JOGADOR = 8
TAMANHO_JOGADOR_X = 40
TAMANHO_JOGADOR_Y = 30

# Configurações do Tiro
VELOCIDADE_TIRO = -10 # Move para cima
TAMANHO_TIRO_X = 4
TAMANHO_TIRO_Y = 15

# Configurações do Asteroide
VELOCIDADE_ASTEROIDE_MIN = 2
VELOCIDADE_ASTEROIDE_MAX = 5
TAMANHO_ASTEROIDE_MIN = 20
TAMANHO_ASTEROIDE_MAX = 50
CHANCE_ASTEROIDE_INICIAL = 80 # Chance de spawnar (1 em 80 frames no início)

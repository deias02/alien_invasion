import pygame

class Character:
    """Uma classe para gerenciar o personagem."""
    def __init__(self, screen):
        """Inicializa o personagem e define sua posição inicial."""
        self.screen = screen
        
        # Carrega a imagem do personagem e obtém seu rect
        self.image = pygame.image.load('imagens/character.bmp')
        self.image.set_colorkey((255, 255, 255))  # Define a cor de fundo da imagem para transparente (caso necessário)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Inicia o personagem no centro da tela
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """Desenha o personagem em sua posição atual."""
        self.screen.blit(self.image, self.rect)
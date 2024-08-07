import pygame
from settings import Settings
from game_stats import GameStats
from button import Button 
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group 
from scoreboard import Scoreboard


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Cria o botão Play  
    play_button = Button(ai_settings, screen,"Play") 
    
    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Define a cor de fundo 
    bg_color = (230, 230, 230)
    
    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings, screen)
    bullets = Group() 
    aliens = Group() 
    # Cria a frota de alienígenas 
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active: 
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets) 
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        alien_drop_speedc=50
        
        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        aliens.draw(screen)
        
        # Deixa a tela mais recente visível
        pygame.display.flip()

# Chama a função para iniciar o jogo
run_game()
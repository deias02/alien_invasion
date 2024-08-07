import random

class AlienBullet:
    def __init__(self, screen, alien):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.midtop = alien.rect.midbottom
        self.color = (255, 0, 0)
        self.speed = 6
        
        
        for bullet in alien_bullets.sprites():
            bullet.update()
        if bullet.rect.colliderect(ship.rect):
            # Código para lidar com a colisão (por exemplo, perder uma vida ou terminar o jogo)
            alien_bullets.remove(bullet)

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def alien_shoot(ai_settings, screen, aliens, alien_bullets):
    if len(aliens) > 0:
        shooting_alien = random.choice(aliens.sprites())
        alien_bullet = AlienBullet(screen, shooting_alien)
        alien_bullets.add(alien_bullet)
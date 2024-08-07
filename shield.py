class Shield:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 60, 10)
        self.color = (0, 255, 0)
        self.health = 3

    def update(self):
        if self.health <= 0:
            self.rect = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def check_shield_collisions(bullets, shields):
    for shield in shields:
        for bullet in bullets:
            if bullet.rect.colliderect(shield.rect):
                bullets.remove(bullet)
                shield.health -= 1
                shield.update()
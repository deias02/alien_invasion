pygame.mixer.init()

if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    play_bullet_sound()
    # Código para disparar a bala

if bullet.rect.colliderect(alien.rect):
    play_explosion_sound()
    # Código para lidar com a colisão

bullet_sound = pygame.mixer.Sound('sounds/bullet.wav')
explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')

def play_bullet_sound():
    bullet_sound.play()

def play_explosion_sound():
    explosion_sound.play()
import pygame
from os import listdir 
from os.path import isfile, join

pygame.init()
pygame.display.set_caption("Sociable Agents")

# ----- GLOBAL VARIABLES ----
WIDTH, HEIGHT = 1000, 1000
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def load_sprites(character_sprite, width, height):
    path = join("assets", "Characters", character_sprite)
    sprite_files = [f for f in listdir(path) if isfile(join(path, f))]
    
    sprites = []
    for sprite_file in sprite_files:
        img = pygame.image.load(join(path, sprite_file)).convert_alpha()
        scaled_img = pygame.transform.scale(img, (width, height))
        sprites.append(scaled_img)
    
    return sprites

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, character_sprite):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.sprites = load_sprites(character_sprite, width, height)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.animation_frames = 30  # Number of frames to show each sprite image
        self.current_frame = 0
    
    def animate(self, task="idle"): # Changing the sprite depending on which task the agent is doing.
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            if task == "idle":
                self.image = self.sprites[0]
            
            else:
                self.image = self.sprites[1]
        # if self.current_frame >= self.animation_frames:
        #     self.current_frame = 0
        #     self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
        #     self.image = self.sprites[self.current_sprite]
    
    def draw(self, win):
        win.blit(self.image, self.rect.topleft)

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background: 
        window.blit(bg_image, tile)
    player.draw(window)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Tile3.png")
    num_players = 5
    player = Player(50, 50, 100, 120, "Character1")

    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= PLAYER_VEL
        elif keys[pygame.K_RIGHT]:
            player.rect.x += PLAYER_VEL

        player.animate()
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)

import pygame

class Hp:

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)

    def __init__(self, hp, gameDisplay):
        self.health = hp
        self.gameDisplay = gameDisplay
        self.player_icon = pygame.image.load("Link Sprites/front_sprites/front 1.png")
        self.enemy_icon = pygame.image.load("ganon_icon.png")
        self.enemy_icon = pygame.transform.scale(self.enemy_icon, (64, 43))
        self.player_rect = self.player_icon.get_rect(center=(20, 560))
        self.enemy_rect = self.enemy_icon.get_rect(center=(505, 560))

    def lose_player_health(self, enemy_attack):
        self.health -= enemy_attack

    def lose_enemy_health(self, player_attack):
        self.health -= player_attack

    def message_to_screen(self, msg, color, size):
        font = pygame.font.SysFont(None, size)
        screen_text = font.render(msg, True, color)
        return screen_text

    # health bar for link
    def health_bar_main(self, player_health):

        if player_health > 75:
            player_health_color = self.green
        elif player_health > 50:
            player_health_color = self.yellow
        elif player_health > 25:
            player_health_color = self.orange
        else:
            player_health_color = self.red

        self.gameDisplay.blit(self.player_icon, self.player_rect)
        pygame.draw.rect(self.gameDisplay, self.black, (78, 544, 112, 37))
        pygame.draw.rect(self.gameDisplay, self.white, (82, 548, 104, 29))

        if player_health > 0:
            pygame.draw.rect(self.gameDisplay, player_health_color, (84, 550, player_health, 25))

    # health bar for ganon
    def health_bar_boss(self, enemy_health):

        if enemy_health > 150:
            enemy_health_color = self.green
        elif enemy_health > 100:
            enemy_health_color = self.yellow
        elif enemy_health > 50:
            enemy_health_color = self.orange
        else:
            enemy_health_color = self.red

        self.gameDisplay.blit(self.enemy_icon, self.enemy_rect)
        pygame.draw.rect(self.gameDisplay, self.black, (574, 544, 212, 37))
        pygame.draw.rect(self.gameDisplay, self.white, (578, 548, 204, 29))

        if enemy_health > 0:
            pygame.draw.rect(self.gameDisplay, enemy_health_color, (580, 550, enemy_health, 25))

    # health bars for naruto, sasuke, kakashi, luffy, pikachu, and goku
    def health_bars_side_char(self, enemy_health, length):

        if enemy_health > 150:
            enemy_health_color = self.green
        elif enemy_health > 100:
            enemy_health_color = self.yellow
        elif enemy_health > 50:
            enemy_health_color = self.orange
        else:
            enemy_health_color = self.red

        pygame.draw.rect(self.gameDisplay, self.black, (575, length - 5, 210, 20))
        pygame.draw.rect(self.gameDisplay, self.white, (578, length - 2, 204, 14))

        if enemy_health > 0:
            pygame.draw.rect(self.gameDisplay, enemy_health_color, (580, length, enemy_health, 10))


import pygame
import sys
import time


class Game:
    def __init__(self, speed=12):
        self.check_errors = pygame.init()
        if self.check_errors[1] > 0:
            sys.exit()

        self.width = 320
        self.height = 480

        self.green = pygame.Color(50, 200, 50)
        self.yellow = pygame.Color(255, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.brown = pygame.Color(200, 50, 50)

        self.fps_controller = pygame.time.Clock()
        self.speed = speed

        self.score = 0

        self.s_font = pygame.font.SysFont('arial', 20)
        self.go_font = pygame.font.SysFont('arial', 40)

    def set_surface(self):
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')

    def eventing(self, change_to):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    self.game_over()
        return change_to

    def refresh_screen(self):
        pygame.display.flip()
        self.fps_controller.tick(self.speed)

    def show_score(self):
        s_surf = self.s_font.render(f'Score: {self.score}', True, self.black)
        s_rect = s_surf.get_rect()
        s_rect.midtop = (self.width // 2, 10)
        self.surface.blit(s_surf, s_rect)

    def game_over(self):
        go_surf = self.go_font.render('GAME OVER', True, self.black)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (self.width // 2, self.height // 4)
        self.surface.blit(go_surf, go_rect)

        self.show_score()

        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

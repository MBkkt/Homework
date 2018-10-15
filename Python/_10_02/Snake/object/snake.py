import random
import pygame


class Snake:
    def __init__(self, snake_color):
        self.snake_body = [[100, 160], [90, 160], [80, 160]]
        self.snake_head = self.snake_body[0].copy()
        self.snake_color = snake_color
        self.direction = "RIGHT"
        self.change_to = self.direction

    def change_direction(self):
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head(self):
        if self.direction == "RIGHT":
            self.snake_head[0] += 20
        elif self.direction == "LEFT":
            self.snake_head[0] -= 20
        elif self.direction == "UP":
            self.snake_head[1] -= 20
        elif self.direction == "DOWN":
            self.snake_head[1] += 20

    def body_mechanism(self, score, apple_pos, width, height):
        self.snake_body.insert(0, self.snake_head.copy())
        if self.snake_head[0] == apple_pos[0] and self.snake_head[1] == apple_pos[1]:
            apple_pos = [random.randrange(2, width // 20 - 1) * 20,
                         random.randrange(2, height // 20 - 1) * 20]
            score += 1
        else:
            self.snake_body.pop()
        return score, apple_pos

    def draw_snake(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], 20, 20))

    def check(self, screen_width, screen_height):
        if any((self.snake_head[0] > screen_width - 10 or self.snake_head[0] < 0,
                self.snake_head[1] > screen_height - 10 or self.snake_head[1] < 0)):
            return True
        for block in self.snake_body[1:]:
            if block[0] == self.snake_head[0] and block[1] == self.snake_head[1]:
                return True

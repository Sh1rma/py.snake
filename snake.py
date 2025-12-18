import pygame
from settings import GRID_SIZE

class Snake:
    def __init__(self):
        self.positions = [(100, 100)]
        self.direction = (0, -GRID_SIZE)

    def move(self):
        head_x, head_y = self.positions[0]
        delta_x, delta_y = self.direction
        new_head = (head_x + delta_x, head_y + delta_y)
        self.positions = [new_head] + self.positions[:-1]

    def change_direction(self, new_direction):
        self.direction = new_direction

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, (0, 255, 0), (*pos, GRID_SIZE, GRID_SIZE))
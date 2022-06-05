"""main_menu.py"""
import pygame

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)


class Button():
    """Button class"""

    def __init__(self, image, x_pos, y_pos, text_input) -> None:
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self) -> None:
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position) -> None:
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top)

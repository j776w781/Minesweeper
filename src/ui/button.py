"""
Program name:
Description:
Inputs:
Outputs:
External sources:
Authors:
Creation date: 28 August 2025
"""

import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 30) #get custom font later

    def draw(self, surface):
        # Draw button background
        pygame.draw.rect(surface, (100, 100, 100), self.rect) 
        # Render and draw text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and event.button == 1: #If the mouse position is over the button AND the left mouse button was pressed
                self.action()


def on_button_click():
    print("Button clicked!")

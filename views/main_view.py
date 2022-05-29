"""Main view which serves as container for other views"""

import pygame
from .abstract_view import AbstractView


class MainView(AbstractView):
    """Class implementing main window of the application"""
    SCREEN_COLOR = (0, 0, 0)

    def __init__(self, name, window_width, window_height, model=None):
        """Setup pygame window"""
        super().__init__(name, model)
        pygame.init()
        pygame.display.set_caption("Game of life")
        size = (window_width, window_height)
        self.__screen = pygame.display.set_mode(size)

    def add_component(self, comp):
        """Add new component to MainView"""
        super().add_component(comp)

    def update(self, *args, **kwargs):
        pass

    def show(self, surface=None):
        """Display nested view's children"""
        self.__screen.fill(self.SCREEN_COLOR)
        for child in self.get_children():
            child.show(self.__screen)

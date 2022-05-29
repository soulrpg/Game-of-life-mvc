"""Concrete BoardView"""

from .abstract_view import AbstractView
import pygame

class BoardView(AbstractView):
    """Board view contaning displayed cells"""
    BOARD_COLOR = (230, 230, 255)

    def __init__(self, name, size, model=None):
        super().__init__(name, model)
        self.__size = size

    def add_component(self, comp):
        """Add component"""
        super().add_component(comp)

    def update(self, *args, **kwargs):
        pass

    def show(self, surface=None):
        """Show board and all cells"""
        pygame.draw.rect(surface, self.BOARD_COLOR, (0, 0, self.__size, self.__size))
        for child in self.get_children():
            child.show(surface)

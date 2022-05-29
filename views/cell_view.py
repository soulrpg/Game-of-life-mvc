"""Concrete CellView"""

from .abstract_view import AbstractView
import pygame


class CellView(AbstractView):
    """Single cell view class"""
    CELL_COLOR = (10, 10, 50)

    def __init__(self, name, model=None):
        super().__init__(name, model)
        self.__x_pos = model.x_pos
        self.__y_pos = model.y_pos
        self.__alive = model.alive


    def add_component(self, comp):
        pass


    def update(self, *args, **kwargs):
        self.__alive = args[0].alive


    def show(self, surface=None):
        if self.__alive:
            pygame.draw.rect(surface, self.CELL_COLOR,\
                (20 * self.__x_pos, 20 * self.__y_pos, 20, 20))
        
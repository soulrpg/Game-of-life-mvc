from .abstract_view import AbstractView
import pygame

class BoardView(AbstractView):
    BOARD_COLOR = (230, 230, 255)

    def __init__(self, name, size, model=None):
        super().__init__(name, model)
        self.__size = size


    def add_component(self, comp):
        super().add_component(comp)


    def update(self, *args, **kwargs):
        pass


    def show(self, surface):
        pygame.draw.rect(surface, self.BOARD_COLOR, (0, 0, self.__size, self.__size))
        for child in self.get_children():
            child.show(surface)
        
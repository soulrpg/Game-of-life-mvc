from .abstract_view import AbstractView
import pygame

class MainView(AbstractView):
    """Class implementing main window of the application"""
    SCREEN_COLOR = (0, 0, 0)
    
    
    def __init__(self, name, window_width, window_height, model=None):
        """Setup pygame window"""
        super().__init__(name, model)
        size = (window_width, window_height)
        self.__screen = pygame.display.set_mode(size)
        self.__screen.fill(self.SCREEN_COLOR)
        

    @property
    def screen(self):
        return self.__screen


    def add_component(self, comp):
        super().add_component(comp)

    def update(self, *args, **kwargs):
        pass

    def show(self):
        pass
        
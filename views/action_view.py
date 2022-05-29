from .abstract_view import AbstractView
import pygame

class ActionView(AbstractView):
    def __init__(self, name, model=None):
        super().__init__(name, model)
        self.__simulation_running = False
        self.__start_img = pygame.image.load("img/play.png")
        self.__stop_img = pygame.image.load("img/stop.png")
        
        # Scale images
        self.__start_img = pygame.transform.scale(self.__start_img,\
            (240, 240))
        self.__stop_img = pygame.transform.scale(self.__stop_img,\
            (240, 240))
        

    def add_component(self, comp):
        pass


    def update(self, *args, **kwargs):
        pass


    def show(self, surface):
        if self.__simulation_running:
            surface.blit(self.__stop_img, (720, 120))
        else:
            surface.blit(self.__start_img, (720, 120))
        
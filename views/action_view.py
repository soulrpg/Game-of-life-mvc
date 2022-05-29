from .abstract_view import AbstractView
import pygame

class ActionView(AbstractView):
    TEXT_COLOR = (255, 255, 255)
    TEXT_COLOR_RUNNING = (120, 255, 120)
    TEXT_COLOR_STOPPED = (255, 120, 150)


    def __init__(self, name, model=None):
        super().__init__(name, model)
        self.__simulation_running = False
        self.__font = pygame.font.SysFont(None, 24)
        

    def add_component(self, comp):
        pass


    def update(self, *args, **kwargs):
        self.__simulation_running = args[0].simulation_running


    def show(self, surface):
        status_text = ""
        action_text = ""
        status_color = None
        if self.__simulation_running:
            status_text = "Status: RUNNING"
            action_text = "Press SPACE to PAUSE"
            status_color = self.TEXT_COLOR_RUNNING
        else:
            status_text = "Status: STOPPED"
            action_text = "Press SPACE to RUN"
            status_color = self.TEXT_COLOR_STOPPED
        status_rendered = self.__font.render(status_text, True, status_color)
        surface.blit(status_rendered, (760, 40))
        action_rendered = self.__font.render(action_text, True, self.TEXT_COLOR)
        surface.blit(action_rendered, (760, 80))
        simulation_label = self.__font.render("simulation", True, self.TEXT_COLOR)
        surface.blit(simulation_label, (760, 100))
        
        
from .abstract_controller import AbstractController
import pygame


class GraphicController(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)


    @AbstractController.view.setter
    def view(self, value):
        if value:
            self._view = value


    def get_user_input(self):
        while True:
                pygame.time.Clock().tick(10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pass
                self._view.show()
                #TODO: all cell states have to be updated there, always
                pygame.display.flip()

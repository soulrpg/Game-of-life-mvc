"""Graphic controller which uses pygame library"""

import sys
import pygame
from .abstract_controller import AbstractController


class GraphicController(AbstractController):
    """Graphic controller handing input from keyboard"""

    def __init__(self, model=None, view=None):
        super().__init__(model, view)


    @AbstractController.view.setter
    def view(self, value):
        if value:
            self._view = value


    def get_user_input(self):
        """Check for SPACE button or quit"""
        while True:
            pygame.time.Clock().tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._model.change_simulation_state()
                        self._model.modify()
            if self._model.simulation_running:
                self._model.tick()
            self._view.show()
            pygame.display.flip()

"""app.py"""

from models.cell_model import CellModel
from models.board_model import BoardModel
from views.board_view import BoardView
from views.action_view import ActionView
from views.cell_view import CellView
from views.main_view import MainView

import pygame


class App():
    """App initializer class"""
    BOARD_SIZE = 20
    WINDOW_WIDTH = 960
    WINDOW_HEIGHT = 720


    def __init__(self, controller):
        """Create models, views and controllers"""
        self.__controller = controller
        board = BoardModel()
        board_view = BoardView("BoardView", board)
        action_view = ActionView("ActionView")
        board.add_observer(board_view)

        # Create cells
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                cell = CellModel(i, j)
                cell_view = CellView("CellView", cell)
                cell.add_observer(cell_view)
                board_view.add_component(cell_view)

        self.__view = MainView("MainView", self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.__view.add_component(board_view)
        self.__view.add_component(action_view)

        self.__controller.model = board
        self.__controller.view = action_view
        
        pygame.init()
        pygame.display.set_caption("Game of life")


    def run(self):
        """Main loop of the app"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.flip()

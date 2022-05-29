"""app.py"""

from models.cell_model import CellModel
from models.board_model import BoardModel
from views.board_view import BoardView
from views.action_view import ActionView
from views.cell_view import CellView
from views.main_view import MainView


class App():
    """App initializer class"""
    BOARD_SIZE = 36
    WINDOW_WIDTH = 960
    WINDOW_HEIGHT = 720


    def __init__(self, controller):
        """Create models, views and controllers"""
        self.__controller = controller
        board = BoardModel(self.BOARD_SIZE)
        self.__view = MainView("MainView", self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        board_view = BoardView("BoardView", self.WINDOW_HEIGHT, board)
        action_view = ActionView("ActionView")
        board.add_observer(board_view)
        board.add_observer(action_view)

        # Create cells
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                cell = CellModel(i, j)
                board.add_cell(cell)
                cell_view = CellView(\
                    "CellView[" + str(i) + "][" + str(j) + "]", cell)
                cell.add_observer(cell_view)
                board_view.add_component(cell_view)

        self.__view.add_component(board_view)
        self.__view.add_component(action_view)

        self.__controller.model = board
        self.__controller.view = self.__view


    def run(self):
        """Main loop of the app"""
        self.__controller.get_user_input()

"""Board model"""

from .abstract_model import AbstractModel


class BoardModel(AbstractModel):
    """Class representing board with cells inside"""

    def __init__(self, board_size):
        """Create empty cell board with given size"""
        super().__init__()
        self.__cells = [[None] * board_size for i in range(board_size)]
        self.__simulation_running = False
        self.__board_size = board_size

    def change_simulation_state(self):
        """Change simulation state to the opposite"""
        self.__simulation_running = not self.__simulation_running

    def tick(self):
        """Single iteration of game of life"""
        for i, cell_row in enumerate(self.cells):
            for j, cell in enumerate(cell_row):
                alive_neightbors = 0
                for neightbor in self.get_neightbors(i, j):
                    if neightbor.alive:
                        alive_neightbors += 1
                if cell.alive:
                    cell.alive = (alive_neightbors in [2, 3])
                else:
                    cell.alive = (alive_neightbors == 3)
        self.modify()

    def get_neightbors(self, pos_x, pos_y):
        """Get all neightbors if possible"""
        neightbors = []
        if not pos_x == 0:
            neightbors.append(self.cells[pos_x - 1][pos_y])
        if not pos_x == self.__board_size - 1:
            neightbors.append(self.cells[pos_x + 1][pos_y])
        if not pos_y == 0:
            neightbors.append(self.cells[pos_x][pos_y - 1])
        if not pos_y == self.__board_size - 1:
            neightbors.append(self.cells[pos_x][pos_y + 1])
        if not (pos_x == self.__board_size - 1 or pos_y == self.__board_size - 1):
            neightbors.append(self.cells[pos_x + 1][pos_y + 1])
        if not (pos_x == 0 or pos_y == 0):
            neightbors.append(self.cells[pos_x - 1][pos_y - 1])
        if not (pos_x == 0 or pos_y == self.__board_size - 1):
            neightbors.append(self.cells[pos_x - 1][pos_y + 1])
        if not (pos_x == self.__board_size - 1 or pos_y == 0):
            neightbors.append(self.cells[pos_x + 1][pos_y - 1])
        return neightbors

    def modify(self, *args, **kwargs):
        """Modify board and its cells"""
        for cell_row in self.cells:
            for cell in cell_row:
                cell.modify()
        self.notify()

    def notify(self):
        """Notify all observers"""
        for obs in self._obs_list.values():
            obs.update(self)

    def add_cell(self, cell):
        """Add cell at given position in cell two-dimensional list"""
        self.__cells[cell.x_pos][cell.y_pos] = cell

    @property
    def cells(self):
        """Get cells"""
        return self.__cells

    @property
    def simulation_running(self):
        """Get simulation_running"""
        return self.__simulation_running
        
    def reset(self):
        """Randomize state of the board"""
        for cell_row in self.cells:
            for cell in cell_row:
                cell.reset()
        self.__simulation_running = False
        self.modify()

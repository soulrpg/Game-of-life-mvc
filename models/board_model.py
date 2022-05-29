from .abstract_model import AbstractModel


class BoardModel(AbstractModel):
    def __init__(self, board_size):
        super().__init__()
        self.__cells = [[None] * board_size for i in range(board_size)]
        self.__simulation_running = False
        self.__board_size = board_size
        
    def change_simulation_state(self):
        self.__simulation_running = not self.__simulation_running
        

    def tick(self):
        for i, cell_row in enumerate(self.cells):
            for j, cell in enumerate(cell_row):
                alive_neightbors = 0
                for neightbor in self.get_neightbors(i, j):
                    if neightbor.alive:
                        alive_neightbors += 1
                if cell.alive:
                    cell.alive = (alive_neightbors == 2 or alive_neightbors == 3)
                else:
                    cell.alive = (alive_neightbors == 3)
        self.modify()


    def get_neightbors(self, x, y):
        neightbors = []
        if not x == 0:
            neightbors.append(self.cells[x - 1][y])
        if not x == self.__board_size - 1:
            neightbors.append(self.cells[x + 1][y])
        if not y == 0:
            neightbors.append(self.cells[x][y - 1])
        if not y == self.__board_size - 1:
            neightbors.append(self.cells[x][y + 1])
        if not (x == self.__board_size - 1 or y == self.__board_size - 1):
            neightbors.append(self.cells[x + 1][y + 1])
        if not (x == 0 or y == 0):
            neightbors.append(self.cells[x - 1][y - 1])
        if not (x == 0 or y == self.__board_size - 1):
            neightbors.append(self.cells[x - 1][y + 1])
        if not (x == self.__board_size - 1 or y == 0):
            neightbors.append(self.cells[x + 1][y - 1])
        return neightbors
    

    def modify(self, *args, **kwargs):
        for cell_row in self.cells:
            for cell in cell_row:
                cell.modify()
        self.notify()


    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self)


    def add_cell(self, cell):
        self.__cells[cell.x_pos][cell.y_pos] = cell


    @property
    def cells(self):
        return self.__cells
        
        
    @property
    def simulation_running(self):
        return self.__simulation_running

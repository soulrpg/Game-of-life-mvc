from .abstract_model import AbstractModel


class CellModel(AbstractModel):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.__x_pos = x_pos
        self.__y_pos = y_pos

    def modify(self, *args, **kwargs):
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self)
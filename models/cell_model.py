"""Cell model"""

import random
from .abstract_model import AbstractModel


class CellModel(AbstractModel):
    """Cell model, keeps position and alive state"""
    BORN_ALIVE_CHANCE = 0.15

    def __init__(self, x_pos, y_pos):
        """Create alive or dead cell based on BORN_ALIVE_CHANCE"""
        super().__init__()
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__alive = random.random() < self.BORN_ALIVE_CHANCE

    def modify(self, *args, **kwargs):
        """Modify cell"""
        self.notify()

    def notify(self):
        """Notify cell view"""
        for obs in self._obs_list.values():
            obs.update(self)

    @property
    def x_pos(self):
        """Get x_pos"""
        return self.__x_pos

    @property
    def y_pos(self):
        """Get y_pos"""
        return self.__y_pos

    @property
    def alive(self):
        """Get alive"""
        return self.__alive

    @alive.setter
    def alive(self, value):
        """Set alive"""
        self.__alive = value

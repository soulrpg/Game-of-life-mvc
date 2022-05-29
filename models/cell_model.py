"""Cell model"""
from .abstract_model import AbstractModel
import random


class CellModel(AbstractModel):
    BORN_ALIVE_CHANCE = 0.1

    def __init__(self, x_pos, y_pos):
        """Create alive or dead cell based on BORN_ALIVE_CHANCE"""
        super().__init__()
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__alive = random.random() < self.BORN_ALIVE_CHANCE


    def modify(self, *args, **kwargs):
        self.notify()


    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self)
            
    @property
    def x_pos(self):
        return self.__x_pos
        
    
    @property
    def y_pos(self):
        return self.__y_pos
    
    
    @property
    def alive(self):
        return self.__alive

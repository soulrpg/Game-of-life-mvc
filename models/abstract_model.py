"""Base model"""

from abc import ABC, abstractmethod


class AbstractModel(ABC):
    """Abstract model class"""

    def __init__(self):
        super().__init__()
        self._obs_list = {}

    def add_observer(self, obs):
        """Add observer base method"""
        if obs.name not in self._obs_list:
            self._obs_list[obs.name] = obs

    def remove_observer(self, name):
        """Remove observer base method"""
        if name in self._obs_list:
            del self._obs_list[name]

    @abstractmethod
    def modify(self, *args, **kwargs):
        pass


    @abstractmethod
    def notify(self):
        pass

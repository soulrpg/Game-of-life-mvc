"""Base view"""

from abc import ABC, abstractmethod


class AbstractView(ABC):
    """Abstract view class"""

    def __init__(self, name, model):
        super().__init__()
        self.__name = name
        self.__component_list = {}
        self._model = model

    @property
    def name(self):
        """Get name"""
        return self.__name

    def get_children(self):
        """Get __component_list"""
        return self.__component_list.values()

    def remove_component(self, name):
        """Remove component from __component_list with given name"""
        if name in self.__component_list:
            del self.__component_list[name]

    @abstractmethod
    def add_component(self, comp):
        """Add component (has to have new name)"""
        if comp.name not in self.__component_list:
            self.__component_list[comp.name] = comp

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def show(self, surface=None):
        pass

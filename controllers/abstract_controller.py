"""Base controller"""

from abc import ABC, abstractmethod


class AbstractController(ABC):
    """AbstractController class"""

    def __init__(self, model=None, view=None):
        super().__init__()
        self._model = model
        self._view = view

    @abstractmethod
    def get_user_input(self):
        """Get user input"""
        pass

    @property
    def model(self):
        """Get model"""
        return self._model

    @model.setter
    def model(self, value):
        """Set model"""
        self._model = value


    @property
    def view(self):
        """Get _view"""
        return self._view


    @view.setter
    def view(self, value):
        """Set _view"""
        self._view = value

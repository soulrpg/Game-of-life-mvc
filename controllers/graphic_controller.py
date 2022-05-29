from .abstract_controller import AbstractController


class GraphicController(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)

    @AbstractController.view.setter
    def view(self, value):
        if value:
            self._view = value

    def get_user_input(self):
        pass
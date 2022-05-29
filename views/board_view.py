from .abstract_view import AbstractView

class BoardView(AbstractView):
    def __init__(self, name, model=None):
        super().__init__(name, model)

    def add_component(self, comp):
        super().add_component(comp)

    def update(self, *args, **kwargs):
        pass

    def show(self):
        pass
        
from .abstract_view import AbstractView

class CellView(AbstractView):
    def __init__(self, name, model=None):
        super().__init__(name, model)

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        pass

    def show(self):
        pass
        
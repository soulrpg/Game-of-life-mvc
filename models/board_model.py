from .abstract_model import AbstractModel


class BoardModel(AbstractModel):
    def __init__(self):
        super().__init__()

    def modify(self, *args, **kwargs):
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self)
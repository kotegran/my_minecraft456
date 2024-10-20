from direct.showbase.ShowBase import ShowBase
from Mapmanager import Mapmanager
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        model = self.loader.LoadModel("models/environment")
        model.reparentTo(self.render)
        self.camlens.setFov(50)
        model.setScale(0.1)
        model.setPos(-2, 25, -3)
        self.land = Mapmanager(self.loader, self.render)
        




game= Game()
game.run()
from direct.showbase.Loader import Loader


class Mapmanager():
    def __init__(self, loader: Loader, render):
        self.loader = loader
        self.render = render
        self.model = "block.egg"
        self.texture="block.png"
        self.color= (1, 0, 0, 1)
        self.startNew()
        self.addBlock((0, 10, 0))


    def addBlock(self, pos):
        self.block=self.loader.IpadModel(self.model)
        self.block.setTexture(self.texture)
        self.block.setPos(pos)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

        def startNew(self):
            self.land=self.render.attachNewNode("Land")
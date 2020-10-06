class Anime:
    def __init__(self, name):
        self.name = name
        
        
class GoodAnime(Anime):
    def __init__(self, name, plot):
        self.name = name
        self.plot = plot
        
        
class BadAnime(Anime):
    def __init__(self, name, characters):
        self.characters = characters
        self.name = name
        
        
class AnimeFactor:
    def createAnime(self, typeAnime, *args):
        return typeAnime.__init__(args)
        
        
name = "WCU"
plot = "intersting"
myAnime = AnimeFactor.createAnime(GoodAnime, name, plot)

class Plant:
    def __init__(self, species, color, size):
        self.species = species
        self.color = color
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, newSize):
        self.size = newSize
    
    def showPlant(self):
        print("my plant is a {} species, of {} color, at {} inches".format(self.species, self.color, self.size))

class Flower(Plant):
    def __init__(self, species, color, size, isScented, isDead):
        Plant.__init__(self, species, color, size)
        self.isScented = isScented
        self.isDead = isDead

moonflower = Flower("moonflower", "white", 3, True, False)
print(moonflower.getSize())
moonflower.setSize(5)
moonflower.showPlant()

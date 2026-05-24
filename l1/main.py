class Fruit:
    def __init__(self, color, taste, shape, preference):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference

    def getShape(self):
        return self.shape
        
    def setShape(self, newShape):
        self.shape = newShape
    
    def increasePref(self):
        self.preference = self.preference + 1

    def showFruit(self):
        print("hello, i am a fruit with {} color, {} shape, {}, {}"
              .format(self.color, self.shape, self.taste, self.preference))
        
apple = Fruit("red", "sweet", "round", 1)
apple.showFruit()
print(apple.getShape())
apple.setShape("sphere")
apple.increasePref()
apple.showFruit()

banana = Fruit("yellow", "sweet", "cylinder", 1)
banana.showFruit()
banana.setShape("sliced")
print(banana.getShape())
banana.increasePref()
banana.showFruit()
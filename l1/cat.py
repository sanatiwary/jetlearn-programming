class Cat:
    def __init__(self, breed, color, age, name):
        self.breed = breed
        self.color = color
        self.age = age
        self.name = name
    
    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def increaseAge(self):
        self.age += 1

    def showCat(self):
        print("my cat is a {}, {} color, {} years old, named {}"
              .format(self.breed, self.color, self.age, self.name))
    
cat1 = Cat("tabby", "grey", 2, "storm")
cat1.showCat()
cat1.setName("cloud")
print("cat1's new name is " + cat1.getName())
cat1.increaseAge()
cat1.showCat()

cat2 = Cat("siamese", "white", 3, "jiji")
cat2.showCat()
cat2.setName("violet")
print("cat2's new name is " + cat2.getName())
cat2.increaseAge()
cat2.showCat()
class Profile:
    __age = 14

    def __init__(self, dName, bio):
        self.dName = dName
        self.bio = bio

    def getAge(self):
        return self.__age
    
    def birthday(self):
        self.__age += 1

    def showProfile(self):
        print(self.dName)
        print(self.bio)

p1 = Profile("sana", "highschooler")
print(p1.getAge())
p1.birthday()
print(p1.getAge())
p1.showProfile()
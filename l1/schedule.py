class School:
    def __init__(self, block, subject, teacher, homework):
        self.block = block
        self.subject = subject
        self.teacher = teacher
        self.homework = homework
    
    def assignHW(self, assignment):
        self.homework = assignment
        print("your new homework for " + self.subject + " is to " + self.homework)

    def finishHW(self):
        self.homework = "nothing"
        print("finished my homework for " + self.subject + " class!")

    def showHW(self):
        print("my homework for " + self.subject + " class is " + self.homework)

    def showClass(self):
        print("my block " + self.block + " class is " + self.subject + " with " + self.teacher + " and my homework is to " + "self.homework")

    
class1 = School("1", "spanish", "seno ciuca", "study for spanish test")
class1.showClass()
class1.finishHW()
class1.showHW()
class1.assignHW("cook food for potluck")
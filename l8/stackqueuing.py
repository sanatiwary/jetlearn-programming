class Mix:
    def __init__(self, n):
        self.mix = []
        self.n = n

    def push(self, a):
        if len(self.mix) < self.n:
            self.mix.append(a)
            print("number is pushed")
        else:
            print("tried to push but mix is full")

    def dequeue(self):
        self.mix.pop(0)
        print("number is dequeued")

    def size(self):
        print("size of mix: " + str(len(self.mix)))

    def display(self):
        print("current mix: " + str(self.mix))


m = Mix(3)
m.push(1)
m.push(9)
m.push(6)
m.push(7)
m.size()
m.display()
m.dequeue()
m.size()
m.display()

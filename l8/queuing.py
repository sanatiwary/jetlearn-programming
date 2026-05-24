class Queue:
    def __init__(self):
        self.queue = []

    def queuing(self, a):
        self.queue.append(a)
    
    def dequeuing(self):
        self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)

q = Queue()

q.queuing(1)
q.display()

q.queuing(2)
q.queuing(5)
q.queuing(7)
q.display()

q.dequeuing()
q.display()
print(q.size())
q.display()
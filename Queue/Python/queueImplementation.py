class Queue():

    def __init__(self, size: int = 64):
        self.size = size #Init queue size
        self.Q = [None]*self.size #Init queue space
        self.head = 0 #Init head
        self.tail = 0 #Init tail
        self.nelements = 0 #Size of the queue

    def print(self):
        print("Queue:", self.Q, "head:", self.head, "tail", self.tail)
        print()

    def enqueue(self, x):
        if self.nelements == self.size: #Validate queue overflow
            print("Queue overflow")
            # raise Exception("Queue overflow")
        else:
            self.Q[self.tail] = x #Insert in tail
            self.tail += 1 #Move tail
            if self.tail == self.size: #Tail should reset to 0
                self.tail = 0
            self.nelements += 1 #One new element in the queue

    def dequeue(self):
        if self.nelements == 0: #Validate queue underflow
            print("Queue underflow")
            # raise Exception("Queue underflow")
        else:
            x = self.Q[self.head] #Get head of queue
            self.Q[self.head] = None #Remove from queue
            self.head += 1 #Move head
            if self.head == self.size: #Head should reset to 0
                self.head = 0
            self.nelements -= 1 #One element removed
            return x #Return removed

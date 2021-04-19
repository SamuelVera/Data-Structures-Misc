class Stack:
    """Stack implementation"""
    A = [] #Stack
    top = 0 #Top
    size = 64 #Stack max index

    def __init__(self, size: int=64):
        self.size = size
        self.top = 0
        self.A = [None]*self.size

    def stackPush(self, x):
        if self.size == self.top: #Index overflow
            print("Stack overflow")
            #raise Exception("Stack overflow")
        else:
            self.A[self.top] = x #Occupy top
            self.top += 1 #Increase top

    def stackPop(self):
        if self.top == 0: #Index underflow
            print("Stack undeflow")
            #raise Exception("Stack underflow")
        else:
            self.top -= 1 #Move one down
            x = self.A[self.top] #Get top of stack
            self.A[self.top] = None #Remove
            return x #Return x

    def print(self):
        print("Stack", self.A, "top", self.top)

import math #Math import

class HeapNode:
    """Node of a heap

    Attributes:
    ---------------
    value : T
        Value of the heap
    A : list
        Array of any type for the heap"""
    #Value of the node
    value = None
    #Key of the node
    key = -math.inf

    def __init__(self, value):
        #Node initialization
        self.value = value

class BinaryHeap:
    """Binary heap
    
    Attributes:
    ---------------
    size : int
        Size of the heap
    A : list
        Array of any type for the heap

    Methods:
    ---------------
    make_heap-heap() : void
        Reset heap, or heap initialization. Complexity: O(1)
    insert(x, k) : void
        Insert element 'x' with priority 'k'. Complexity: O(logn)
    increase_key(x, k) : void
        Increase the key of x to k. Complexity: O(logn)
    heapify(i, heapType) : void
        Restore heap's property for the given binary tree i. Complexity: O(logn)
    """
    
    #Heap initialization
    A = []
    size = 0
    isMax = True

    #Initialization of heap
    def __init__(self):
        self.make_heap() #Call initialization method
        self.isMax = isinstance(self, BinaryMaxHeap) #It's a max heap

    def make_heap(self):
        """Initialization of heap"""
        self.A = []
        self.size = 0

    def heapify(self, i: int):
        """Restore heap's property in the given binary tree i. Assumes that the heap property is fullfilled in the sub trees
        
        Parameters:
        ---------------
        i : int
            Index to start Heap's property restoration
        isMaxHeap : bool
            Is heap a max heap or a min heap
        """
        #Calc sub trees roots
        left = 2 * i #Left root
        right = (2*i) + 1 #Right root
        heapParentIndex = i #Parent index (largest or smallest)

        if self.isMax == True: #If its a max heap
            if left < self.size and self.A[left].key > self.A[i].key:
                #If the left root exists and the heap property isn'f fullfilled
                heapParentIndex = left
            if right < self.size and self.A[right].key > self.A[heapParentIndex].key:
                #If right exists and is largest than current largest
                heapParentIndex = right
        else: #If its a min heap
            if left < self.size and self.A[left].key < self.A[i].key:
                #If the left root exists and the min heap property isn'f fullfilled
                heapParentIndex = left
            if right < self.size and self.A[right].key < self.A[heapParentIndex].key:
                #If right exists and is smallest than current smallest
                heapParentIndex = right
        
        if heapParentIndex != i: #Heap's property isn't fullfilled need to do changes
            self.A[heapParentIndex], self.A[i] = self.A[i], self.A[heapParentIndex] #Swap
            self.heapify(heapParentIndex) #Continue with Heap's property checking

    def increase_key(self, i, k):
        """Increase priority of element i to k"""
        iKey = self.A[i].key #Current key

        if iKey < k: #Increase should happen
            self.A[i].key = k #Update key

            if self.isMax: #Is max heap
                while i > 0 and self.A[i // 2].key < self.A[i].key:
                    #While a swap based on the key change needs to be done
                    self.A[i // 2], self.A[i] = self.A[i], self.A[i // 2] #Swap
                    i = i // 2 #Update i with parent (Swap happened)
            else: #Is min heap
                while i > 0 and self.A[i // 2].key > self.A[i].key:
                    #While a swap based on the key change needs to be done
                    self.A[i // 2], self.A[i] = self.A[i], self.A[i // 2] #Swap
                    i = i // 2 #Update i with parent (Swap happened)

    def insert(self, x, k: int):
        """Insert node to heap with priority k
        
        Parameters:
        --------------
        x : HeapNode
            Node to insert
        k : int
            Priority for insertation
        """
        xNode = HeapNode(x) #Generate node with -inf priority
        self.size += 1 #Update size
        self.A.append(xNode) #Append as last
        self.increase_key(self.size - 1, k) #Increase key value

    def change_key(self, i, k):
        """Change priority of element i to k"""
        self.A[i].key = k #Update key

        if self.isMax: #Is max heap
            while i > 0 and self.A[i // 2].key < self.A[i].key:
                #While a swap based on the key change needs to be done
                self.A[i // 2], self.A[i] = self.A[i], self.A[i // 2] #Swap
                i = i // 2 #Update i with parent (Swap happened)
        else: #Is min heap
            while i > 0 and self.A[i // 2].key > self.A[i].key:
                #While a swap based on the key change needs to be done
                self.A[i // 2], self.A[i] = self.A[i], self.A[i // 2] #Swap
                i = i // 2 #Update i with parent (Swap happened)

    def printHeapArrayRepresentation(self):
        print("Heap array: [")
        for node in self.A:
            print(node.value,",")
        print("]")
        print()

class BinaryMaxHeap(BinaryHeap):
    """Binary max heap

    Methods:
    ---------------
    maximum() : (T, key)
        Get maximum node. Complexity: O(1)
    extract_max() : (T, key)
        Extract and return the maximum node. Complexity: O(logn)
    
    """
    def maximum(self):
        """Get value of maximum"""
        if self.size <= 0: #Empty check
            return None

        return self.A[0].value, self.A[0].key #Return node
    
    def extract_max(self):
        """Extract max and get value of it"""
        if self.size <= 0: #Empty check
            return None

        item = self.A[0] #Get max
        self.A[0] = self.A.pop() #Move last to first
        self.size = self.size - 1 #Update size
        self.heapify(0) #Heapify from 0

        return item.value, item.key #Return item

class BinaryMinHeap(BinaryHeap):
    """Binary max heap

    Methods:
    ---------------
    minimum() : (T, key)
        Get minimum node. Complexity: O(1)
    extract_min() : (T, key)
        Extract and return the minimum node. Complexity: O(logn)
    """
    def minimum(self) -> HeapNode:
        """Get value of minimum"""
        if self.size <= 0: #Empty check
            return None

        return self.A[0].value, self.A[0].key #Return node
    
    def extract_min(self) -> HeapNode:
        """Extract min and get value of it"""
        if self.size <= 0: #Empty check
            return None

        item = self.A[0] #Get max
        self.A[0] = self.A.pop() #Move last to first
        self.size = self.size - 1 #Update size
        self.heapify(0) #Heapify from 0

        return item.value, item.key #Return item

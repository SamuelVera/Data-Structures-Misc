import math #Math library

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
    key = -math.inf #Initially -inf

    def __init__(self, value, key):
        #Node initialization
        self.value = value
        self.key = key

class BinomialTree:
    """Binomial Tree class

    Attributes:
    -----------------
    root : HeapNode
        Key of the tree
    order : int
        Order of the tree (n)
    children : list
        Childrens of the tree (other trees)

    Methods:
    -----------------
    add_at_end(x) : void
        Add given node as last of list
    """
    order = 0 #Order of the tree
    children = [] #Childrens of the tree are heap nodes

    def __init__(self, root: HeapNode):
        """Constructor for binomial tree class"""
        self.root = root #Root of the tree
        self.order = 0 #Order 0
        self.children = [] #No childrens
    
    def add_at_end(self, x):
        """Add element x at the end of the tree"""
        self.children.append(x) #Add at the end
        self.order += 1 #Increase order

def print_binomial_tree(t: BinomialTree):
    print('Root Key:', t.root.key, 'root value:', t.root.value) #Print root
    if t.order > 0: #If childs exist
        print("Tree Childs:")
        for i, child in enumerate(t.children): #Print for each child
            print("Child #"+str(i))
            print_binomial_tree(child) #Their substructure

class BinomialHeap:
    """Heap binomial base class

    Attributes:
    -----------------
    trees : list[BinomialTree]
        List of binomial trees of the heap
    
    Methods:
    -----------------
    make_heap : void
        Initializes the heap
    """

    trees = [] #Trees of the heap

    def make_heap(self):
        """Initialize the heap"""
        self.trees = []

    def __init__(self):
        """Binomial heap constructor"""
        self.make_heap() #Initialize the heap

    def print_trees(self):
        """Print the trees of the heap"""
        for i, tree in enumerate(self.trees):
            print("Tree #"+str(i))
            print_binomial_tree(tree) #Print binomial tree

class BinomialMinHeap(BinomialHeap):
    """Min binomial heal class

    Methods:
    -----------------
    minimum : T, int
        Get the minimum node of the heap. Complexity: O(logn)
    extract_min : T, int
        Get the minimum node of the heap and remove it. Complexity: O(logn)
    combine_roots(h) : void
        Combine the current heap binomial trees with the given heap binomial trees (min implementation). Complexity: O(logn)
    merge(h) : void
        Merge the current heap with the given heap while keeping the heap's property (min implementation). Complexity O(logn + logm)
    insert(x, key) : void
        Insert the value x with given key in the heap. Complexity O(logn)
    """

    def minimum(self):
        """Get the minimum value of the heap"""
        if len(self.trees) == 0: #Empty heap
            return None, None #Return none
        
        smallest_root = self.trees[0].root
        for tree in self.trees:
            if tree.root.key < smallest_root.key: #New smallest
                smallest_root.key = tree.root.key
        
        return smallest_root.value, smallest_root.key

    def combine_roots(self, h):
        """Combine the roots of two min heaps"""
        self.trees.extend(h.trees) #Extende current heap and incoming heap
        self.trees.sort(key=lambda tree: tree.order) #Sort by tree order descending

    def merge(self, h):
        """Merge the current heap and the given heap"""
        self.combine_roots(h) #Combine roots
        if self.trees == []: #Combining two empty heaps
            return #Do no ops

        i = 0 #Start at 0
        while i < len(self.trees) - 1: #Iterate the combined roots of trees until all is merged
            current = self.trees[i] #Current tree of iteration
            next_ = self.trees[i + 1] #Next tree of iteration

            if current.order == next_.order: #If both trees are of the same order
                if (i + 1 < len(self.trees) - 1) and self.trees[i + 2].order == next_.order:
                    #If next tree and the next of next has the same order
                    next_of_next = self.trees[i + 2]

                    if next_.root.key < next_of_next.root.key: #If keys of next is smaller than the key of next of next
                        next_.add_at_end(next_of_next) #Add next of next at the end of next
                        del self.trees[i + 2] #Delete next of next because it was merged
                    else: #Next of next key is smaller than next key
                        next_of_next.add_at_end(next_) #Add next at the end of next of next
                        del self.trees[i + 1]
                else: #There's no next of next or the order is not the same
                    if current.root.key < next_.root.key: #Current is smaller than next
                        current.add_at_end(next_) #Add next at the end of current
                        del self.trees[i + 1] #Delete next
                    else: #Next is smaller than current
                        next_.add_at_end(current) #Add current at the end of next
                        del self.trees[i] #Delete current
            i += 1

    def extract_min(self):
        if len(self.trees) == 0: #Empty
            return None, None
        
        smallest_tree = self.trees[0]
        for tree in self.trees:
            if tree.root.key < smallest_tree.root.key: #New smallest
                smallest_tree.root.key = tree.root.key

        self.trees.remove(smallest_tree) #Remove smallest tree

        h = BinomialHeap() #Create a new heap 
        h.trees = smallest_tree.children #With the childrens of the smallest tree as the binomial trees
        self.merge(h) #Merge h with the current

        return smallest_tree.root.value, smallest_tree.root.key

    def insert(self, x, key):
        """Insert the element x in the heap with key"""
        g = BinomialHeap() #Generate a new order 1 binomial heap
        r = HeapNode(x, key) #Generate a Heap Node with value x and given key
        g.trees.append(BinomialTree(r)) #Add binomial tree
        self.merge(g) #Merge the generated order 1 binomial heap with the current heap

class BinomialMaxHeap(BinomialHeap):
    """Min binomial heal class

    Methods:
    -----------------
    maximum : T, int
        Get the maximum key of the heap. Complexity: O(logn)
    extract_max : T, int
        Get the maximum node of the heap and remove it. Complexity: O(logn)
    combine_roots(h) : void
        Combine the current heap binomial trees with the given heap binomial trees (max implementation). Complexity: O(logn)
    merge(h) : void
        Merge the current heap with the given heap while keeping the heap's property (max implementation). Complexity O(logn + logm)
    insert(x, key) : void
        Insert the value x with given key in the heap. Complexity O(logn)
    """

    def maximum(self):
        """Get the maximum value of the heap"""
        if len(self.trees) == 0: #Empty heap
            return None, None #Return none
        
        largest_root = self.trees[0].root
        for tree in self.trees:
            if tree.root.key > largest_root.key:
                largest_root = tree.root
        
        return largest_root.value, largest_root.key

    def combine_roots(self, h):
        """Combine the roots of two max heaps"""
        self.trees.extend(h.trees) #Extende current heap and incoming heap
        self.trees.sort(key=lambda tree: tree.order, reverse=True) #Sort by lambda and tree order descending

    def merge(self, h):
        """Merge the current heap and the given heap"""
        self.combine_roots(h) #Combine roots
        if self.trees == []: #Combining two empty heaps
            return #Do no ops

        i = 0 #Start from 0
        while i < len(self.trees) - 1: #Iterate the combined roots of trees until all is merged
            current = self.trees[i] #Current tree of iteration
            next_ = self.trees[i + 1] #Next tree of iteration

            if current.order == next_.order: #If both trees are of the same order
                if (i + 1 < len(self.trees) - 1) and self.trees[i + 2].order == next_.order:
                    #If next tree and the next of next has the same order
                    next_of_next = self.trees[i + 2]

                    if next_.root.key > next_of_next.root.key: #If keys of next is largest than next of next
                        next_.add_at_end(next_of_next) #Add next of next at the end of next
                        del self.trees[i + 2] #Delete next of next because it was merged
                    else: #Next of next is largest than next
                        next_of_next.add_at_end(next_) #Add next at the end of next of next
                        del self.trees[i + 1]
                else: #There's no next of next or the order is not the same
                    if current.root.key > next_.root.key: #Current is largest than next
                        current.add_at_end(next_) #Add next at the end of current
                        del self.trees[i + 1] #Delete next
                    else: #Next is largest than current
                        next_.add_at_end(current) #Add current at the end of next
                        del self.trees[i] #Delete current
            i += 1 #Move to next

    def extract_max(self):
        if len(self.trees) == 0: #Empty
            return None, None
        
        largest_tree = self.trees[0]
        for tree in self.trees:
            if tree.root.key > largest_tree.root.key: #New largest
                largest_tree.root.key = tree.root.key

        self.trees.remove(largest_tree) #Remove largest tree

        h = BinomialHeap() #Create a new heap 
        h.trees = largest_tree.children #With the childrens of the largest tree as the binomial trees
        self.merge(h) #Merge h with the current

        return largest_tree.root.value, largest_tree.root.key

    def insert(self, x, key):
        """Insert the element x in the heap with key"""
        g = BinomialHeap() #Generate a new order 1 binomial heap
        r = HeapNode(x, key) #Generate a Heap Node with value x and given key
        g.trees.append(BinomialTree(r)) #Add binomial tree
        self.merge(g) #Merge the generated order 1 binomial heap with the current heap
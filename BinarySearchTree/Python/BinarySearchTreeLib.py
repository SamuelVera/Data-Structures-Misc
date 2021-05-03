import math #Math library

class TreeNode:
    """Node of a Binary Search Tree"""
    key: int = -math.inf #Identification key for the tree
    value = None #Value stored in the node
    parent = None #Parent of the node
    leftChild = None #Left child of the node
    rightChild = None #Right child of the node

    #Initialization
    def __init__(self, key: int, value, parent=None, leftChild=None, rightChild=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

class BinarySearchTree:
    """Binary Search Tree"""
    root: TreeNode = None

    #Initialization
    def __init__(self, root: TreeNode=None):
        self.root = root

    #Inorder tree walk, initialized from root
    def inorderTreeWalk(self, x: TreeNode): 
        if x != None: #Stop condition
            self.inorderTreeWalk(x.leftChild) #Go to left
            print(x.key) #Print current in order
            self.inorderTreeWalk(x.rightChild) #Go to right

    #Preorder tree walk, initialized from root
    def preorderTreeWalk(self, x: TreeNode):
        if x != None: #Stop condition
            print(x.key) #Preorder print
            self.preorderTreeWalk(x.leftChild) #Go to left
            self.preorderTreeWalk(x.rightChild) #Go to right

    #Postorder tree walk, initialized from root
    def postorderTreeWalk(self, x: TreeNode):
        if x != None: #Stop condition
            self.postorderTreeWalk(x.leftChild) #Go to left
            self.postorderTreeWalk(x.rightChild) #Go to right
            print(x.key) #Postorder print

    #Search inside the tree based on the given key
    def treeSearch(self, k: int, x: TreeNode) -> TreeNode:
        if x == None or x.key == k: #Stop condition for the recursion
            return x #Return Node or None if found or not

        if k < x.key: #Desired node is on left subtree
            return self.treeSearch(k, x.leftChild)
        else: #Desired node is on the right subtree
            return self.treeSearch(k, x.rightChild)

    #Look for max in the tree
    def treeMaximum(self, x: TreeNode) -> TreeNode:
        while x != None and x.rightChild != None: #While tree is not empty and right subtree exists
            x = x.rightChild #Go to the right subtree

        return x #Return

    #Look for min in the tree
    def treeMinimum(self, x: TreeNode) -> TreeNode:
        while x != None and x.leftChild != None: #While tree is not empty and left subtree exists
            x = x.rightChild #Go to the left subtree

        return x #Return

    #Look for the successor of a given node
    def treeSuccesor(self, x: TreeNode) -> TreeNode:
        if x.rightChild != None: #Case: right subtree not empty
            return self.treeMinimum(x.rightChild)
        else: #Case: right subtree is empty
            y = x.parent

            while y != None and x == y.rightChild: #While parent exists and x is right child of y
                x = y
                y = y.parent

            return y #Final successor

    #Look for predecessor of a given node
    def treePredecessor(self, x: TreeNode) -> TreeNode:
        if x.leftChild != None: #Case: left subtree not empty
            return self.treeMaximum(x.leftChild)
        else: #Case: left subtree empty
            y = x.parent

            while y != None and x == y.leftChild: #While parent exists and x is left child of y
                x = y
                y = y.parent

            return y #Final predecessor

    #Insert a given node into the tree
    def treeInsert(self, z: TreeNode):
        y = None
        x = self.root

        while x != None: #Search where to insert
            y = x

            if z.key < x.key: #Should go to the left subtree
                x = x.leftChild 
            else: #Should go to the right subtree
                x = x.rightChild

        z.parent = y #Assign parent to node to insert

        if y == None: #Case: tree is empty
            self.root = z #Node to insert becomes root
        elif z.key < y.key: #Case: is left child
            y.leftChild = z
        else: #Case is right child
            y.rightChild = z

    #Transplant the two given nodes in the tree
    def treeTransplant(self, u: TreeNode, v: TreeNode):
        if u.parent == None: #Case: u is the root
            self.root = v #v becomes the new root
        elif u == u.parent.leftChild: #Case: u is a left child
            u.parent.leftChild = v #v becomes the left child of u's parent
        else: #Case: u is a right child
            u.parent.rightChild = v #v becomes the right child of u's parent

        if v != None: #Modify parent pointer to transplated node
            v.parent = u.parent #Transplant completed

    #Delete the given node from the tree
    def treeDelete(self, z: TreeNode):
        if z.leftChild == None: #Case 1: left subtree empty
            self.treeTransplant(z, z.rightChild) #Transplant with right child
        elif z.rightChild == None: #Case 2: right subtree empty
            self.treeTransplant(z, z.leftChild) #Transplant with left child
        else: #Case 3: has both childs
            y = self.treeMinimum(z.rightChild) #Minimum from right subtree

            if y.parent != z: #y is right child of z
                self.treeTransplant(y, y.rightChild) #Transplant with right child
                y.rightChild = z.rightChild #Change right child pointer
                y.rightChild.parent = y #Change child parent pointer

            self.treeTransplant(z, y) #Transplant z and y
            y.leftChild = z.leftChild #Change left child pointer
            y.leftChild.parent = y #Change child parent pointer

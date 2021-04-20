class LinkedListNode():
    """Linked list node"""
    def __init__(self, value, key, nextNode=None):
        self.value = value #Init value
        self.key = key #Init key
        self.nextNode = nextNode #Init next node

class DoubleLinkedListNode(LinkedListNode):
    """Double linked list node"""
    def __init__(self, value, key, nextNode=None, previousNode=None):
        self.previousNode = previousNode #Init previous node
        super(DoubleLinkedListNode, self).__init__(value, key, nextNode) #Init others

class LinkedList():
    """Regular linked list"""
    def __init__(self):
        self.head = None #Empty init

    def listSearch(self, key):
        """Search first element with the given key in the list"""
        x = self.head #Get head

        while x != None and x.key != key: #While key hasn't been found and end hasn't been reached
            x = x.nextNode #Move to next node

        return x #Return result None or a node

    def listInsert(self, value, key):
        """Insert given element with given key as first of list"""
        x = LinkedListNode(value, key, self.head) #Create node with head as next (Can be none if this is the first)
        self.head = x #Replace head with new node

    def listDelete(self, key):
        """Remove first element with the given key from the list"""
        x = self.head #Get head

        if x != None: #Validate not empty for 1 element border case check
            if x.nextNode == None and x.key == key: #One element and requested to delete that one
                self.head = None #Head becomes none
                return x #Return x

        while x != None: #While the end hasn't been reached
            nextNode = x.nextNode #Next node
            if nextNode.key == key: #Found the given key
                x.nextNode = nextNode.nextNode #Move reference from next node to the one next
                nextNode.nextNode = None #Remove next reference
                return nextNode #Return node
            x = x.nextNode #Move to next node

class DoubleLinkedList(LinkedList):
    """Double linked list"""
    def __init__(self):
        super(DoubleLinkedList, self).__init__() #Init empty

    def listInsert(self, value, key):
        """Insert as first, overriding for double linked list"""
        x = DoubleLinkedListNode(value, key, self.head)
        if self.head != None: #If head exists already
            self.head.previousNode = x #Set inserting as previous node
        
        self.head = x #Set x as the new head

    def listDelete(self, key):
        """Remove first element with the given key, override for double linked list"""
        x = self.head #Get head

        if x != None: #Validate not empty for 1 element border case check
            if x.nextNode == None and x.key == key: #One element and requested to delete that one
                self.head = None #Head becomes none
                return x #Return x

        while x != None: #While the end hasn't been reached
            nextNode = x.nextNode #Next node
            if nextNode.key == key: #Found the given key
                x.nextNode = nextNode.nextNode #Move reference from next node to the one next
                x.nextNode.previousNode = nextNode.previousNode #Move next next node previous reference to current
                nextNode.nextNode = None #Remove next reference
                nextNode.previousNode = None #Remove previous reference
                return nextNode #Return node
            x = x.nextNode #Move to next node

class CircularLinkedList(LinkedList):
    """Circular linked list"""
    def __init__(self):
        super(CircularLinkedList, self).__init__() #Empty init
        self.tail = None #Tail empty init

    def listSearch(self, key):
        """Look for the first element with the given key, override for circular linked list"""
        x = self.head #Get head
        while x != None and x.key != key: #Element not found yet and no elements
            x = x.nextNode #Move to next node
            if x == self.head: #Back in the head again
                return None #Means node doesn't exist

        return x #Node found

    def listInsert(self, value, key):
        """Insert element as first, override for circular linked list """
        x = LinkedListNode(value, key, self.head) #Create node with head as next

        if self.head == None: #List was empty
            self.tail = x #Set as tail
        else: #List wasn't empty
            self.tail.nextNode = x #Set as next of tail
        
        self.head = x #Set as head

    def listDelete(self, key):
        """Delete the first element with the given key, override for circular linked list"""
        x = self.head #Get head

        if x != None: #Check not None for 1 element border case checking
            if self.head == self.tail and x.key == key: #Head is tail, only one element, and requested to delete this element
                self.head = None #Empty head
                self.tail = None #Empty tail
                x.nextNode = None #Remove next reference
                return x #Return Node


        while x != None: #While end hasn't been reached
            nextNode = x.nextNode #Get next node

            if nextNode.key == key: #Node that will be delete found
                x.nextNode = nextNode.nextNode #Move next of next to next of current

                if nextNode == self.tail: #Node deleting is the tail
                    self.tail = x #Previous node (x) is the new tail

                nextNode.nextNode = None #Remove next node reference
                return nextNode #Return node

            x = nextNode #Move to next node
            if x == self.head: #If back in the head again
                x = None #Nothing to delete by key

        return x #Return delete

class CircularDoubleLinkedList(CircularLinkedList):
    """Circular double linked list, no need to override search"""
    def __init__(self):
        super(CircularDoubleLinkedList, self).__init__() #Empty init

    def listInsert(self, value, key):
        """Insert element as first, override for circular double linked list """
        x = DoubleLinkedListNode(value, key, self.head, self.tail) #Create node with head as next and tail as previous

        if self.head == None: #List was empty
            self.tail = x #Set as tail
        else: #List wasn't empty
            self.tail.nextNode = x #Set as next of tail

        self.head = x #Set as head

    def listDelete(self, key):
        """Delete the first element with the given key, override for circular double linked list"""
        x = self.head #Get head

        if x != None: #Check not None for 1 element border case checking
            if self.head == self.tail and x.key == key: #Head is tail, only one element, and requested to delete this element
                self.head = None #Empty head
                self.tail = None #Empty tail
                x.nextNode = None #Remove next reference
                x.previousNode = None #Remove previous reference
                return x #Return Node


        while x != None: #While end hasn't been reached
            nextNode = x.nextNode #Get next node

            if nextNode.key == key: #Node that will be delete found
                x.nextNode = nextNode.nextNode #Move next of next to next of current
                nextNode.nextNode.previousNode = x #Move next of next previous to current

                if nextNode == self.tail: #When node deleting is the tail
                    self.head.previousNode = nextNode.previousNode #Move head previous reference

                nextNode.nextNode = None #Remove next node reference
                nextNode.previousNode = None #Remove previous reference
                return nextNode #Return node

            x = nextNode #Move to next node
            if x == self.head: #If back in the head again
                x = None #Nothing to delete by key

        return x #Return delete

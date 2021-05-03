import BinarySearchTreeLib #Binary search tree
import sys #System import

if __name__=="__main__":
    #Validate script execution
    #Data to insert
    items = [2, 5, 7, 1, 9, 8, 2, 12]
    t = BinarySearchTreeLib.BinarySearchTree()

    for i in items:
        x = BinarySearchTreeLib.TreeNode(i, i)
        t.treeInsert(x)

    print("In order walk")
    t.inorderTreeWalk(t.root)
    
    print()

    #delete some items
    print("Delete", 7)
    t.treeDelete(t.treeSearch(7, t.root))
    print("Delete", 8)
    t.treeDelete(t.treeSearch(8, t.root))
    print("Delete", 12)
    t.treeDelete(t.treeSearch(12, t.root))
    print()

    print("In order walk")
    t.inorderTreeWalk(t.root)

    sys.exit(0) #Exit execution with code 0
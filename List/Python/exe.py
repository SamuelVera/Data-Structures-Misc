import sys
import lists

if __name__=="__main__":

    print("Lists")

    ll = lists.LinkedList()

    inserts = [2, 5, 6, 4, 8, 9, 10, 12, 11]
    queries = [10, 12, 20, 4, 22]
    removes = [6, 4, 8, 2, 5, 12, 11, 10, 9, 15]

    print("Linked list")
    ll.print()
    print("Inserts:")

    for i in inserts:
        print("Inserting", i)
        ll.listInsert(i, i) #Insert
        ll.print()

    print()
    print("Queries:")
    print()

    for i in queries:
        print("Searching", i)
        print("Result", ll.listSearch(i))
        print()

    print()
    print("Removes:")
    print()

    for i in removes:
        print("Removing", i)
        ll.listDelete(i)
        ll.print()

    print("Double linked list")
    dll = lists.DoubleLinkedList()

    dll.print()
    print("Inserts:")

    for i in inserts:
        print("Inserting", i)
        dll.listInsert(i, i) #Insert
        dll.print()

    print()
    print("Queries:")
    print()

    for i in queries:
        print("Searching", i)
        print("Result", ll.listSearch(i))
        print()

    print()
    print("Removes:")
    print()

    for i in removes:
        print("Removing", i)
        dll.listDelete(i)
        dll.print()

    sys.exit(0) #Stop execution
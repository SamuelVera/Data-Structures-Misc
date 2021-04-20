import sys
import lists

if __name__=="__main__":

    print("Circular list")

    cll = lists.CircularLinkedList()

    inserts = [2, 5, 6, 4, 8, 9, 10, 12, 11]
    queries = [10, 12, 20, 4, 22]
    removes = [6, 4, 8, 2, 5, 12, 11, 10, 9, 15]

    cll.print()
    print()
    print("Insertions:")

    for i in inserts:
        print("Inserting:", i)
        cll.listInsert(i, i)
        cll.print()

    print()
    print("Searching:")

    for q in queries:
        print("Searching:", q)
        print("Result:", cll.listSearch(q))

    print()
    print("Removes:")

    for r in removes:
        print("Removing:", r)
        cll.listDelete(r)
        cll.print()

    print("Circular double linked list")

    cdll = lists.CircularDoubleLinkedList()

    cdll.print()
    print()
    print("Insertions:")

    for i in inserts:
        print("Inserting:", i)
        cdll.listInsert(i, i)
        cdll.print()

    print()
    print("Searching:")

    for q in queries:
        print("Searching:", q)
        print("Result:", cdll.listSearch(q))

    print()
    print("Removes:")

    for r in removes:
        print("Removing:", r)
        cdll.listDelete(r)
        cdll.print()

    sys.exit(0) #Stop execution
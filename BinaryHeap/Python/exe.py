import sys
import binaryHeap

if __name__=="__main__":
    #Script execution
    #Data to insert
    data = [
        {
            "userId": 7,
            "name": "Mark"
        },
        {
            "userId": 2,
            "name": "Anna"
        },
        {
            "userId": 1,
            "name": "Ena"
        },
        {
            "userId": 5,
            "name": "Julia"
        },
    ]

    print("MAX HEAP")
    print("---------------------------------------------")
    #Generate max heap
    maxHeap = binaryHeap.BinaryMaxHeap()
    #Insert all of array
    maxHeap.printHeapArrayRepresentation()
    maxHeap.insert(data[0], data[0]["userId"])
    maxHeap.printHeapArrayRepresentation()
    maxHeap.insert(data[1], data[1]["userId"])
    maxHeap.printHeapArrayRepresentation()
    maxHeap.insert(data[2], data[2]["userId"])
    maxHeap.printHeapArrayRepresentation()
    maxHeap.insert(data[3], data[3]["userId"])
    maxHeap.printHeapArrayRepresentation()
    #Increase key
    print("Increase key of i=2 to 20")
    maxHeap.change_key(2, 20)
    maxHeap.printHeapArrayRepresentation()
    #Get max
    maxValue, maxKey = maxHeap.maximum()
    print("Max of heap value", maxValue, "key", maxKey)
    print()
    #Extract 2 maxes
    print("Extract 2 max")
    print()
    maxValue1, maxKey1 = maxHeap.extract_max()
    maxHeap.printHeapArrayRepresentation()
    maxValue2, maxKey2 = maxHeap.extract_max()
    maxHeap.printHeapArrayRepresentation()
    print("Max of heap 1", maxValue1, "key", maxKey1)
    print("Max of heap 2", maxValue2, "key", maxKey2)

    print("MIN HEAP")
    print("---------------------------------------------")
    #Generate min heap
    minHeap = binaryHeap.BinaryMinHeap()
    #Insert all of array
    minHeap.printHeapArrayRepresentation()
    minHeap.insert(data[0], data[0]["userId"])
    minHeap.printHeapArrayRepresentation()
    minHeap.insert(data[1], data[1]["userId"])
    minHeap.printHeapArrayRepresentation()
    minHeap.insert(data[2], data[2]["userId"])
    minHeap.printHeapArrayRepresentation()
    minHeap.insert(data[3], data[3]["userId"])
    minHeap.printHeapArrayRepresentation()
    #Decrease key
    print("Decrease key of i=3 to -10")
    minHeap.change_key(3, -10)
    minHeap.printHeapArrayRepresentation()
    #Get min
    minValue, minKey = minHeap.minimum()
    print("Min of heap value", minValue, "key", minKey)
    print()
    #Extract 2 min
    print("Extract 2 min")
    print()
    minValue1, minKey1 = minHeap.extract_min()
    minHeap.printHeapArrayRepresentation()
    minValue2, minKey2 = minHeap.extract_min()
    minHeap.printHeapArrayRepresentation()
    print("Min of heap 1", minValue1, "key", minKey1)
    print("Min of heap 2", minValue2, "key", minKey2)

    #Exit execution
    sys.exit(0)
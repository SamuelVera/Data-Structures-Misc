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
    #Get max
    maxOfHeap = maxHeap.maximum()
    print("Max of heap value", maxOfHeap)
    print()
    #Extract 2 maxes
    print("Extract 2 max")
    print()
    maxOfHeap1 = maxHeap.extract_max()
    maxHeap.printHeapArrayRepresentation()
    maxOfHeap2 = maxHeap.extract_max()
    maxHeap.printHeapArrayRepresentation()
    print("Max of heap 1", maxOfHeap1.value, "key", maxOfHeap1.key)
    print("Max of heap 2", maxOfHeap2.value, "key", maxOfHeap2.key)

    print("MIN HEAP")
    print("---------------------------------------------")
    #Generate min heap
    minHeap = binaryHeap.BinaryMinHeap()
    #Insert all of array
    maxHeap.printHeapArrayRepresentation()
    minHeap.insert(data[0], data[0]["userId"])
    minHeap.printHeapArrayRepresentation()
    minHeap.insert(data[1], data[1]["userId"])
    minHeap.printHeapArrayRepresentation()
    minHeap.insert(data[2], data[2]["userId"])
    minHeap.printHeapArrayRepresentation()
    minHeap.insert(data[3], data[3]["userId"])
    minHeap.printHeapArrayRepresentation()
    #Get min
    minOfHeap = minHeap.minimum()
    print("Min of heap value", minOfHeap)
    print()
    #Extract 2 min
    print("Extract 2 max")
    print()
    minOfHeap1 = minHeap.extract_min()
    minHeap.printHeapArrayRepresentation()
    minOfHeap2 = minHeap.extract_min()
    minHeap.printHeapArrayRepresentation()
    print("Min of heap 1", minOfHeap1.value, "key", minOfHeap1.key)
    print("Min of heap 2", minOfHeap2.value, "key", minOfHeap2.key)

    #Exit execution
    sys.exit(0)
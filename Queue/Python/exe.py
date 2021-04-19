import sys
import queueImplementation

if __name__=="__main__":
    q = queueImplementation.Queue(8) #16 size queue

    pushes = [2, 5, 1, 10, 5, 8, 12, 11, 7] #Amount of pushes
    pops = 9 #Amount of pops

    for i in pushes: #Iterate pushes
        print("Enqueueing", i)
        q.enqueue(i) #Enqueue element
        q.print()
        print()
    
    for _ in range(0, pops): #Do n pops
        print("Dequeueing", q.dequeue()) #Dequeue
        q.print()
        print()


    sys.exit(0) #Stop execution
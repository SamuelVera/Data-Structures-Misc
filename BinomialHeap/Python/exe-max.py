import sys #System import
import binomialHeap #Binomial heap module

if __name__=="__main__":
    #Script execution
    bheap = binomialHeap.BinomialMaxHeap() #Iniitialize empty max heap

    #Print possible operations
    print('Menu (Max binomial heap)')
    print('insert <data>')
    print('max get')
    print('max extract')
    print('print')
    print('quit')

    while True:
        do = input('What would you like to do? ').split() #Ask for operation

        operation = do[0].strip().lower() #Go lower case and strip

        if operation == 'insert': #Inser operation
            data = int(do[1]) #Get second argument as integer data
            bheap.insert(data, data) #Insert the data as value and key
        elif operation == 'max': #Operation is max
            suboperation = do[1].strip().lower() #Suboperation
            if suboperation == 'get': #Only get
                value, key = bheap.maximum() #Get maximum
                print('Maximum value:', value, 'key', key) #Print
            elif suboperation == 'extract': #xtract
                value, key = bheap.extract_max() #Get maximum
                print('Maximum value removed:', value, 'key', key)
        elif operation == 'print': #Print operation
            print("Printing trees:")
            bheap.print_trees() #Print trees
        elif operation == 'quit': #Quit operation
            break #Break asking loop
    else:
        sys.exit(0) #Exit execution with code 0
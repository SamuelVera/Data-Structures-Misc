import sys
import stack

if __name__=="__main__":
    s = stack.Stack(4)

    s.print()

    print("Pushing", 2)
    s.stackPush(2)
    print("Stack:")
    s.print()
    print("Pushing", 4)
    s.stackPush(4)
    print("Stack:")
    s.print()
    print("Pushing", 6)
    s.stackPush(6)
    print("Stack:")
    s.print()
    print("Pushing", 5)
    s.stackPush(5)
    print("Stack:")
    s.print()
    print("Pushing", 3)
    s.stackPush(3)
    print("Stack:")
    s.print()
    s.print()
    print("Popping", s.stackPop())
    print("Stack:")
    s.print()
    print("Popping", s.stackPop())
    print("Stack:")
    s.print()
    print("Popping", s.stackPop())
    print("Stack:")
    s.print()
    print("Popping", s.stackPop())
    print("Stack:")
    s.print()
    print("Popping", s.stackPop())
    print("Stack:")
    s.print()

    sys.exit(0) #Finish execution
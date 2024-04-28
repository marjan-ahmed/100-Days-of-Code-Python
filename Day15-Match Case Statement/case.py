x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case 5:
        print("x is 5")
    case 6:
        print("x is 6")
    case 7:
        print("x is 7")
    case 8:
        print("x is 8")
    case 9:
        print("x is 9")
    case 10:
        print("x is 10")
        
    case _ if x != 11:
        print("x is not between 0 and 10")
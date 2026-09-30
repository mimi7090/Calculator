def add(a,b) :
    return a+b
def subtract(a,b) :
    return a-b
def multiply(a,b) :
    return a*b
def divide(a,b) :
    return a/b
def percentage(a,b) :
    return (a*100)/b
def power(a,b) :
    return a**b
while True :
    print("===== Choose Operator =====")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.percentage")
    print("6.power")
    print("7.exit")
    choice = input("Enter your choice (1,2,3,4,5,6,7) :")
    if choice == "7" :
        print("Goodbye !")
        break
    n1 = eval(input("Enter first number :"))
    n2 = eval(input("Enter second number :"))
    if choice == "1" :
        print("Result :",add(n1,n2))
    elif choice == "2" :
        print("Result :",subtract(n1,n2))
    elif choice == "3" :
        print("Result :",multiply(n1,n2))
    elif choice == "4" :
        if n2 == 0 :
            print("Canoot divide by Zero")
        else :
            print("Result :",divide(n1,n2))
    elif choice == "5" :
        if n2 == 0 :
            print("Cannot divide by Zero")
        else :
            print("Result :",percentage(n1,n2))
    elif choice == "6" :
        print("Result :",power(n1,n2))
    else :
        print("Invalid choice")
    
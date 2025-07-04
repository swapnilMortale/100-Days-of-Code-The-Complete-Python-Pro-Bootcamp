# project 10 - calculater 

def calculator_logo():
    print("╔═════════════════╗")
    print("║   CALCULATOR    ║")
    print("╠═════════════════╣")
    print("║  ┌───┬───┬───┐  ║")
    print("║  │ 7 │ 8 │ 9 │  ║")
    print("║  ├───┼───┼───┤  ║")
    print("║  │ 4 │ 5 │ 6 │  ║")
    print("║  ├───┼───┼───┤  ║")
    print("║  │ 1 │ 2 │ 3 │  ║")
    print("║  ├───┼───┼───┤  ║")
    print("║  │ 0 │ + │ - │  ║")
    print("║  └───┴───┴───┘  ║")
    print("╚═════════════════╝")
    

calculator_logo()

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2
    
def multiply(num1,num2):
    return num1*num2
    
def divide(num1,num2):
    return num1/num2
    
def reminder(num1,num2):
    return num1%num2

operation  = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "%":reminder
}
def calculator():

    should_accumulate = True 

    while should_accumulate:
        num1 = float(input("What is first number  : "))

        for symbol in operation:
            print(symbol)

        operation_symbole = input("pick  an operation : ")
        num2 = float(input("What's is the next number :  "))
        ans = operation[operation_symbole](num1,num2)
        print(f"{num1} {operation_symbole} {num2} = {ans} ")

        choice = input(f"type ' yes'  to continue calculation with {ans} ,or type 'no' to start a new calculation :  ")

        if choice == "yes":
            num1 = ans 
            for symbol in operation:
                print(symbol)
        else:
            should_accumulate =False
            print("\n"*11)
            calculator()

        operation_symbole = input("pick  an operation : ")
        num2 = float(input("What's is the next number :  "))
        ans = operation[operation_symbole](num1,num2)
        print(f"{num1} {operation_symbole} {num2} = {ans} ")

calculator()
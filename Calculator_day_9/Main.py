from art import logo 
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

math_ops = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': div
}

def calculation ():    
    print(logo)  
    num1 = float(input("Enter your first number:\n"))
    num2 = float(input("Enter your second number:\n"))
    print("which of the following mathematical operation do you want to choose?\n")
    for symbol in math_ops:
        print(symbol)
    ops_type = input()
    calc_function = math_ops[ops_type]
    answer = calc_function(num1, num2)
    print(f"Your answer is {answer}")
    repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over:\n")


    continue_calc = True
    while continue_calc:
        
        if repeat == 'y':
            number = float(input("Enter your next number:\n"))
            print("which of the following mathematical operation do you want to choose?\n")
            for symbol in math_ops:
                print(symbol)
            ops_type = input()
            calc_function = math_ops[ops_type]
            new_answer = calc_function(answer, number)
            print(f"Your answer is {new_answer}")
            repeat = input(f"Type 'y' to continue calculating with {new_answer}, or type 'n' to exit:\n")
        elif repeat == 'n':
            continue_calc = False
            calculation()

calculation()   
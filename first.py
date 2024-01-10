print("""
    This is a sample Calculator:
      Please Choose from following operation:
      1. Add
      2.Subtract
      3. Multiplication
      4. Divide
      """)
choice = int(input('Enter your choice:'))


def take_input():
    num1 = int(input('Enter first number :'))
    num2 = int(input('Enter second number :'))

    return num1 , num2
    
def add():
    num1 , num2 = take_input()
    return (num1 + num2)

def sub():
    num1 , num2 = take_input()
    return (num1 - num2)

def multiply():
    num1 , num2 = take_input()
    return (num1 * num2)

def div():
    num1 , num2 = take_input()
    return (num1 / num2)










if choice == 1: 
    print('The sum of the numbers is :', add())

elif choice == 2:
    print('The difference of the numbers is :', sub())

elif choice == 3:
    print('The result of the numbers is :', multiply())

elif choice == 4:
    print('The result of the numbers is :', div())



else:
    print('TATA')
    exit()



    


num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number :'))



    



choice = int()

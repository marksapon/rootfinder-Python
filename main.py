import sympy as sympy
from tabulate import tabulate
import os
import math

'''
Made by:
    - Mark Dharel A. Sapon
    - Rey Anthony M. De Luna
    - Bradley Jlord Pinpin
'''




cont = True

# Prompt for continuing the program
def prompt():
    global cont
    state = input("\nDo you want to continue? (y/n): ")
    if (state.lower() == 'n'):
        cont = False
    else:
        os.system('cls')
        cont = True

# Input Format for the equation
def inputFormat():
    print('''
|Equation Format|
    - Basic Arithmetic Operations: +, -, *, /
          e.g. 2 + 3 - 4 / 5 is equivalent to 2 + 3 - 4 / 5
          
    - Variables: number*x
          e.g. 2*x + 3*x - 4*x / 5*x is equivalent to 2x + 3x - 4x / 5x
          
    - Exponential: ** or ^
            e.g. 2**3 or 2^3 is equivalent to 2^3
          
    - Trigonometric Functions: sin(), cos(), tan(), cot(), sec(), csc()
          
    - Inverse Trigonometric Functions: asin(), acos(), atan(), acot(), asec(), acsc()
          
    - Square Root: sqrt()
    
    - Euler's Number: exp()
          ''')
    
def displaylogo():
    print('''
  _____             _     ______ _           _           
 |  __ \           | |   |  ____(_)         | |          
 | |__) |___   ___ | |_  | |__   _ _ __   __| | ___ _ __ 
 |  _  // _ \ / _ \| __| |  __| | | '_ \ / _` |/ _ \ '__|
 | | \ \ (_) | (_) | |_  | |    | | | | | (_| |  __/ |   
 |_|  \_\___/ \___/ \__| |_|    |_|_| |_|\__,_|\___|_|'''
              )
    


# [1] Bisection Method
def bisection():
    table = { 'Xl': [], 'Xm': [], 'Xr': [], 'Yl': [],  'Ym': [], 'Yr': []} # Table for storing the values
    iteration = 0
    os.system('cls')
    

# Getting the equation from the user
    while True:
        try:
            print("[Bisection Method]\n")
            inputFormat()
            equation = sympy.sympify(input("Enter the equation: "))
            break
        except:
            os.system('cls')
            print("Invalid Input! Please try again.\n")

# Checking the value of Xl and Xr are valid
    while True:
        xl = int(input("Enter the variable value Xl: ")) # Set Xl Value
        xr = int(input("Enter the variable value Xr: ")) # Set Xr Value

        if (xl < xr or xl * xr < 0):
            break

        else:
            print("(Xl and Xr should have opposite signs)\n")

    precision_value = input("Enter the precision: ")

    # Set the precision value to user input or default value 5
    precision = float(precision_value) if precision_value else 0.1 

# Halting Condition
    def haltingCondition(iteration, precision):
        if len(table['Ym']) >= 2:
            diff = abs(table['Ym'][-2] - table['Ym'][-1])
            if diff <= precision:
                return False
        return True

# Finding if xl or xr are opposite sign of xm
    def comparison(xl, xm, xr, yl, ym, yr, type):
        
            if yl * ym < 0:
                if (type == "y"):
                    return yl, ym
                else:
                    return xl, xm
            else:
                if (type == "y"):
                    return ym, yr
                else:
                    return xm, xr

# Operation
    while haltingCondition(iteration, precision):

        table['Xl'].append(xl)
        table['Xr'].append(xr)
        table['Xm'].append(math.ceil(((xl + xr) / 2) * 10**4) / 10**4)

        if (iteration == 0):
            table['Yl'].append(math.ceil(sympy.sympify(equation).subs('x', xl) * 10**4) / 10**4)
            table['Yr'].append(math.ceil(sympy.sympify(equation).subs('x', xr) * 10**4) / 10**4)
        else:
            table['Yl'].append(yl)
            table['Yr'].append(yr)

        table['Ym'].append(math.ceil(sympy.sympify(equation).subs('x', table['Xm'][iteration]) * 10**4) / 10**4)

        [yl, yr] = comparison(xl, table['Xm'][iteration], xr, table['Yl'][iteration], table['Ym'][iteration], table['Yr'][iteration],  "y")

        [xl, xr] = comparison(xl, table['Xm'][iteration], xr, table['Yl'][iteration], table['Ym'][iteration], table['Yr'][iteration],  "x")
        iteration += 1
    
    os.system('cls')
    displaylogo()
    print(tabulate(table, headers='keys', tablefmt='fancy_grid', showindex='always'))
    print("Roots: ", table['Xm'][-1])
    print("f(x): ", table['Ym'][-1],)
    prompt()

        


# [2] False Position Method
def false_position():
    table = { 'Xl': [], 'Xm': [], 'Xr': [], 'Yl': [],  'Ym': [], 'Yr': []} # Table for storing the values
    iteration = 0
    os.system('cls')

# Getting the equation from the user
    while True:
        try:
            print("[False Position Method]\n")
            inputFormat()
            equation = sympy.sympify(input("Enter the equation: "))
            break
        except:
            os.system('cls')
            print("Invalid Input! Please try again.\n")

# Checking the value of Xl and Xr are valid
    while True:
        xl = int(input("Enter the variable value Xl: ")) # Set Xl Value
        xr = int(input("Enter the variable value Xr: ")) # Set Xr Value

        if (xl < xr or xl * xr < 0):
            break

        else:
            print("(Xl and Xr should have opposite signs)\n")

    precision_value = input("Enter the precision: ")

    # Set the precision value to user input or default value 5
    precision = float(precision_value) if precision_value else 0.1 

# Halting Condition
    def haltingCondition(precision):
        if len(table['Ym']) >= 2:
            diff = abs(table['Ym'][-2] - table['Ym'][-1])
            if diff <= precision:
                return False
        return True

# Finding if xl or xr are opposite sign of xm
    def comparison(xl, xm, xr, yl, ym, yr, type):
        
            if yl * ym < 0:
                if (type == "y"):
                    return yl, ym
                else:
                    return xl, xm
            else:
                if (type == "y"):
                    return ym, yr
                else:
                    return xm, xr

# Operation
    while haltingCondition(precision):

        table['Xl'].append(xl)
        table['Xr'].append(xr)

        if (iteration == 0):
            yl = round(sympy.sympify(equation).subs('x', xl), 3)
            yr = round(sympy.sympify(equation).subs('x', xr), 3)
            table['Yl'].append(yl)
            table['Yr'].append(yr)

        else:
            table['Yl'].append(yl)
            table['Yr'].append(yr)

        
        # table['Xm'].append(math.ceil(( xl + (xr-xl) * ( yl/(yl-yr) )) * 10**4) / 10**4)
        xm = round(( xl + (xr-xl) * ( yl/(yl-yr) )), 5)
        table['Xm'].append(xm)

        # ym = (sympy.sympify(equation).subs('x', table['Xm'][iteration]))
        table['Ym'].append(math.ceil(sympy.sympify(equation).subs('x', table['Xm'][iteration]) * 10**4) / 10**4)
        # table['Ym'].append(round(ym,5))

        [yl, yr] = comparison(xl, table['Xm'][iteration], xr, table['Yl'][iteration], table['Ym'][iteration], table['Yr'][iteration],  "y")

        [xl, xr] = comparison(xl, table['Xm'][iteration], xr, table['Yl'][iteration], table['Ym'][iteration], table['Yr'][iteration],  "x")
        iteration += 1
    
    os.system('cls')
    displaylogo()
    print(tabulate(table, headers='keys', tablefmt='fancy_grid', showindex='always'))

    print("Roots: ", float(table['Xm'][-1]))
    print("f(x): ", float(table['Ym'][-1]))
    prompt()


     

# [3] Newton Raphson Method
def newton_raphson():
    table = {'X': [], 'f(x)': [], "f'(x)": [], 'rel.error': []} # Table for storing the values
    iteration = 0
    os.system('cls')

    # Getting the equation from the user
    while True:
        try:
            print("[Newton Raphson Method]\n")
            inputFormat()
            equation = input("Enter the f(x): ")
            break
        except:
            os.system('cls')
            print("Invalid Input! Please try again.\n")

    x_value = input("Enter the initial value of x: ")
    x_value = int(x_value) if x_value else 1

    x = sympy.symbols('x')
    parsed_equation = sympy.sympify(equation)
    derivative = sympy.diff(parsed_equation, x)

    print(f"\nThe derivative of {equation} is {derivative}")

    print("Processing...")

    # Halting Condition
    def rel_error():
        if len(table['rel.error']) != 0:
            # print(table['rel.error'][-1])

            if table['rel.error'][-1] == 0:
                return False
            
            else:
                return True
            
        else:
            return True

    # Operation
    while rel_error():
        print(f"\n[Iteration: {iteration}]")

        print("% Computing X...")
        table['X'].append(math.ceil(x_value * 10**4) / 10**4)

        print("% Computing f(x)...")
        table['f(x)'].append(math.ceil(parsed_equation.subs('x', x_value) * 10**4) / 10**4)
        
        print("% Computing f'(x)...")
        table["f'(x)"].append(math.ceil(derivative.subs('x', x_value) * 10**4) / 10**4)

        print("Computing rel.error...")
        if iteration != 0:
            table['rel.error'].append(round(abs((table['X'][-2] - table['X'][-1]) / table['X'][-1]), 6))
        else:
            table['rel.error'].append("")
        
        x_value = x_value - (parsed_equation.subs('x', x_value) / derivative.subs('x', x_value))
        iteration += 1
    
    os.system('cls')
    displaylogo()
    print(tabulate(table, headers='keys', tablefmt='fancy_grid', showindex='always'))

    print("Roots: ", float(table['X'][-1]))
    print("f(x) : ", float(table['f(x)'][-1]))
    prompt()




# [4] Secant Method
def secant():
    os.system('cls')
    print("[Secant Method]\n")
    table = {'Xa': [], 'Xb': [], 'f(Xa)': [], 'f(Xb)': [], 'rel.error': []} # Table for storing the values
    iteration = 0

    # Getting the equation from the user
    while True:
        try:
            print("[Secant Method]\n")
            inputFormat()
            equation = input("Enter the equation: ")
            break
        except:
            os.system('cls')
            print("Invalid Input! Please try again.\n")

    xa = int(input("Enter the initial value of Xa: "))
    xb = int(input("Enter the initial value of Xb: "))

    # Halting Condition
    def rel_error():
        if len(table['rel.error']) != 0:
            # print(table['rel.error'][-1])

            if table['rel.error'][-1] == 0:
                return False
            
            else:
                return True
            
        else:
            return True

    # Operation
    while rel_error():
        # if iteration == 5:
        #     break

        print(f"\n[Iteration: {iteration}]")

        print("% Computing Xa...")
        table['Xa'].append(xa)

        print("% Computing Xb...")
        table['Xb'].append(xb)

        print("% Computing f(Xa)...")
        table['f(Xa)'].append(math.ceil(sympy.sympify(equation).subs('x', xa) * 10**4) / 10**4)

        print("% Computing f(Xb)...")
        table['f(Xb)'].append(math.ceil(sympy.sympify(equation).subs('x', xb) * 10**4) / 10**4)
        

        print("Computing rel.error...")
        if(iteration != 0): 
            table['rel.error'].append(round(abs((table['Xb'][-2] - table['Xb'][-1]) / table['Xb'][-1]), 6))
        else:
            table['rel.error'].append("")

        placeholder = xb
        xb = xa - (table['f(Xa)'][-1] * (table['Xa'][-1] - table['Xb'][-1]) / (table['f(Xa)'][-1] - table['f(Xb)'][-1]))
        print(f"xb: {xb}")
        xa = placeholder
        iteration += 1

    os.system('cls')
    displaylogo()
    print(tabulate(table, headers='keys', tablefmt='fancy_grid', showindex='always'))

    print("Roots: ", float(table['Xb'][-1]))
    print("f(x) : ", float(table['f(Xa)'][-1]))

    prompt()




    
# Main Function
def Main():
    os.system('cls')
    while cont:
        displaylogo()
        print('''
Made by:
- Mark Dharel A. Sapon
- Rey Anthony M. De Luna
- Bradley Jlord Pinpin
              ''')

        print('''
            [1] Bisection Method
            [2] False Position Method
            [3] Newton Raphson Method
            [4] Secant Method
            ''')

        method = input("Enter the method of finding Root from above: ")

        if method == '1':
            bisection()

        elif method == '2':
            false_position()

        elif method == '3':
            newton_raphson()

        elif method == '4':
            secant()

        else:
            os.system('cls')
            print("|Invalid Input! Please try again.|")


Main()
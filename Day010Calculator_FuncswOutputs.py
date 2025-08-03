"""def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year %4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("year: "))
print(is_leap_year(year))"""

#calc

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calc():
    accumulate= True
    n1 = float(input("Enter first number: "))

    while accumulate:
        ops = input("+\n-\n*\n/\nChoose an operator: ")
        n2 = float(input("Enter second number: "))

        if ops in operators:
            result = operators[ops](n1,n2)
            if result.is_integer():
                print(f"{n1} {ops} {n2} = {int(result)}")
            else:
                print(f"{n1} {ops} {n2} = {result}")
            cont = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ")
            if cont == 'y':
                n1 = result
            elif cont == 'n':
                accumulate = False
                print("\n"*20)
                calc()
        else:
            print("Invalid operator")
            calc()

calc()

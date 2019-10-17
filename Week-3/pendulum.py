import math

def period(L,g):
    try:
        T = math.pi*2*(L/g)**0.5
        return T
    except ZeroDivisionError:
        print("You can't divide by zero bruh")
        return "Undefined"
    except TypeError:
        print("Please enter a number")
        return "Like 1,2,3"
    except NameError:
        print("Please enter a number")
        return "Like 1,2,3"


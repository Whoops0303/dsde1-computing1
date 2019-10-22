import math

def period(L,g):
    try:
        T = math.pi*2*(L/g)**0.5
        return T
    except ZeroDivisionError:
        raise ZeroDivisionError("You can't divide by zero bruh")
    except TypeError:
        raise TypeError("Please enter a number")
    except NameError:
        raise NameError("Please enter a number")


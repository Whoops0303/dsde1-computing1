import math

def period(L,g):
    try:
        if g == 0:
            raise ValueError("You can't divide by zero bruh")
        else:
            T = math.pi*2*(L/g)**0.5
        return T
    except TypeError:
        raise TypeError("Please enter a number")
    except NameError:
        raise NameError("Please enter a number")


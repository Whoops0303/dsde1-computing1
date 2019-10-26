import math

def period(leng, gra):
    '''period maker'''
    try:
        if gra == 0:
            raise ValueError("You can't divide by zero bruh")
        return math.pi*2*(leng/gra)**0.5
    except TypeError:
        raise TypeError("Please enter a number")
    except NameError:
        raise NameError("Please enter a number")

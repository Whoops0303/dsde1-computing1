'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def welcome_message(user_name=None, place=None):
    '''This function outputs messages and accepts username and place input'''
    if user_name is not None and place is not None:
        return "Hello, " + user_name + ", and welcome to " + place
    if user_name is not None:
        return "Hello, " + user_name + ", and welcome"
    if place is not None:
        return "Hello and welcome to " + place
    return "Hello and welcome"

# Create a function called list_average()
# without using any libraries to do the maths for you
# (the point of this exercise is to practice interacting
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
def list_average(lst, avg_type=None):
    '''This annoying long piece of junk gives you the mean, median and mode'''
    mean_total = 0
    types = []
    mode_count = 0
    modes = []
    sorted_list = sorted(lst)
    if avg_type in (None, 'mean'):
        if not lst:
            return 0
        for number in lst:
            mean_total += number
        return mean_total/len(lst)
    if avg_type == 'mode':
        for number in lst:
            if number not in types:
                types.append(number)
        for number in types:
            if lst.count(number) >= mode_count:
                mode_count = lst.count(number)
        for number in types:
            if lst.count(number) == mode_count:
                modes.append(number)
        return modes
    if avg_type == 'median':
        if not lst:
            return None
        if len(sorted_list)%2 == 0:
            return (sorted_list[int(len(lst)/2-1)] + sorted_list[int(len(lst)/2)])/2
        return sorted_list[int((len(lst)-1)/2)]
      
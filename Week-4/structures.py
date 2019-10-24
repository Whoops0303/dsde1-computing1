'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    '''Gives the first and last items in a list.'''
    lst = []
    lst.append(the_list[0])
    lst.append(the_list[-1])
    return lst


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    '''Returns part of the_list between indices in reverse order, inclusive of beginning but exclusive of end.'''
    if end > len(the_list) or beginning < -len(the_list):
        raise ValueError("Give an index in the list")
    else:
        new_list = the_list[beginning:end]
        reversed_list = []
        for i in range(len(new_list)):
            reversed_list.append(new_list[(i+1)*-1])
        return reversed_list

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    '''Repeats the index given in the_list 3 times.'''
    new_list = []
    new_list += the_list[:index]
    for i in range(3):
        new_list.append(the_list[index])
    new_list += the_list[index+1:]
    return new_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    '''Checks whether a word is a palindrome.'''
    lword = word.lower()
    bword = ''
    for i in range(-1,-len(lword)-1,-1):
        bword += lword[i]
    return lword == bword

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    '''Checks whether a sentence is a palindrome while ignoring spaces, fullstops and commas.'''
    lsentence = sentence.lower()
    lst = []
    for letter in lsentence:
        if letter == ' ' or letter == '.' or letter == ',':
            continue
        else:
            lst.append(letter)
    rlst = lst[::-1]
    return lst == rlst

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    '''Combines two sentences like a normal english essay, sentences must be capped at the start and end with a fullstop'''
    sen1 = sentence1
    sen2 = sentence2
    final_sen = ''
    while sen1[0] == ' ':
        sen1 = sen1.replace(' ','',1)
    sen1 = sen1[::-1]
    while sen1[0] == ' ':
        sen1 = sen1.replace(' ','',1)
    sen1 = sen1[::-1]

    while sen2[0] == ' ':
        sen2 = sen2.replace(' ','',1)
    sen2 = sen2[::-1]
    while sen2[0] == ' ':
        sen2 = sen2.replace(' ','',1)
    sen2 = sen2[::-1]

    if sen1[0].isupper() and sen2[0].isupper():
        if sen1[-1] == '.' or sen1[-1] == '?' or sen1[-1] == '!':
            if sen2[-1] == '.' or sen2[-1] == '?' or sen2[-1] == '!':
                final_sen = sen1 + ' ' + sen2
                return final_sen
            else:
                raise ValueError('End sentence 2 with . or ? or !')
        else:
            raise ValueError('End sentence 1 with . or ? or !')
    else: 
        raise ValueError('Use uppercase for first letter')


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    '''Checks whether a certain key is in a dictionary'''
    for keyy in dictionary.keys():
        if keyy == key:
            return True
        else:
            continue
    return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    '''Checks whether a certain value is in a dictionary'''
    for valuee in dictionary.values():
        if valuee == value:
            return True
        else:
            continue
    return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    '''Combines two dictionaries'''
    dict1 = dictionary1
    for key,value in dictionary2.items():
        dict1[key] = value
    return dict1

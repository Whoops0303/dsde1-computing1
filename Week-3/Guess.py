print("1 to 10, gimme number!")

import random
ans = random.randint(1,11)
#creating random number between 1 to 10

guess1 = int(input())
#prompting for 1st guess


if guess1 == ans:
    print("Well done, first try!!")
else:
    print("Two more tries, let's go!!")
    guess2 = int(input())
    if guess2 == ans:
        print("GGWP ;)")
    else:
        print("Third time's the charm!!")
        guess3 = int(input())
        if guess3 == ans:
            print("Nailed it!!")
        else:
            print("It's okay, let's go again!!")

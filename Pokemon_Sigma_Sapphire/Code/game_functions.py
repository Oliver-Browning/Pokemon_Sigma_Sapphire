import random

def award_candy():
    """
    Takes in no arguments. Generates a weighted random integer
    either 3, 5, or 10 and returns it. 
    comment here to see if logan macbook is bricked or not ig
    """
    candy_amounts = [3, 5, 10]
    rand_int = random.randint(0,2)

    candy_awarded = (random.choices(candy_amounts, weights=(50, 40, 10)))[0]

    return candy_awarded
    


#print(award_candy())





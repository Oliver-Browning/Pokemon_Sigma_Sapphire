import random

def award_candy():
    """
    Words
    """
    candy_amounts = [3, 5, 10]
    rand_int = random.randint(0,2)

    candy_awarded = (random.choices(candy_amounts, weights=(50, 40, 10)))[0]

    return candy_awarded
    


#print(award_candy())





import random


#Note for future Oliver or current Logan, change the dialogue from the reward isnt in my chest to: Im not the one who stole the pokemon
#Update other diualogue accordingly instead of something being in a chest, 
game = {
    1: {
        1: "I did not steal the Pokemon!",
        2: "One of us is telling the truth!",
        3: "They are both telling the truth. {p1} did not steal the Pokemon."
    },
    2: {
        1: "None of us stole the Pokemon.",
        2: "I did not steal the Pokemon. They are both lying.",
        3: "I stole the Pokemon"
    },
    3: {
        1: "I did not steal the Pokemon. We are all telling the truth.",
        2: "I did not steal the Pokemon. At least one of the others is telling the truth!",
        3: "One of the others is lying!"
    },
    4: {
        1: "I stole the Pokemon and I'm telling the truth!",
        2: "They are both lying, I stole the pokemon!",
        3: "They are both telling the truth, {p2} stole the Pokemon!"
    },
    5: {
        1: "At least one of them is lying, and {p3} did not steal the Pokemon!",
        2: "We are all telling the truth!",
        3: "{p2} is telling the truth and they stole the Pokemon."
    },
    6: {
        1: "Both of them are telling the truth. Also, {p2} stole the Pokemon!",
        2: "{p3} is telling the truth.",
        3: "I stole the Pokemon!"
    }
}

def three_weirdos():
    """
    Returns a list of three tuples, each containing:
    (person's name, their statement, whether they are telling the truth)
    The first person in the list is always telling the truth and then it shuffles it.
    """

    names = ["Okarin", "Mayushii", "Suzuha", "Faris Nyan", "Monika", "Yuri", "Sayori", "Daru", "Lelouch", "Shinei", "Light", "L", "Erwin Smith", "Eren", "Mikasa", "Levi", "Sans", "Papyrus", "Lucy", "David", "Maine", "Rebecca", "Adam Smasher", "Kiwi", "Ado"]

    chosen = random.sample(names, 3)

    seed = random.randint(1, 6)

    # print(chosen, seed)




    # player 1 must be correct

    p1_data = (chosen[0], game[seed][1].format(p1=chosen[0],p2=chosen[1],p3=chosen[2]), True)
    p2_data = (chosen[1], game[seed][2].format(p1=chosen[0],p2=chosen[1],p3=chosen[2]), False)
    p3_data = (chosen[2], game[seed][3].format(p1=chosen[0],p2=chosen[1],p3=chosen[2]), False)

    people = [p1_data, p2_data, p3_data]

    shuffled = random.sample(people, 3)

    # print(shuffled, seed)

    # print(shuffled[0])
    # print(shuffled[1])
    # print(shuffled[2])

    return shuffled # list of tuples


    # RETURN A <<< RANDOM SHUFFLING PERMUTATION THINGY MAJINGY >>> OF THIS THING SO PLAYER 1 IS NOT ALWAYS RIGHT
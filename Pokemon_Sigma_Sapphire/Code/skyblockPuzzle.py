import random

game = {
    1: {
        1: "The reward is not in my chest!",
        2: "One of us is telling the truth!",
        3: "They are both telling the truth. The reward isn't in {p1}'s chest."
    },
    2: {
        1: "The reward isn't in any of our chests.",
        2: "The reward is not in my chest. They are both lying.",
        3: "The reward is in my chest!"
    },
    3: {
        1: "My chest doesn't have the reward. We are all telling the truth.",
        2: "My chest doesn't have the reward. At least one of the others is telling the truth!",
        3: "One of the others is lying!"
    },
    4: {
        1: "My chest has the reward and I'm telling the truth!",
        2: "They are both lying, the reward is in my chest!",
        3: "They are both telling the truth, the reward is in {p2}'s chest!"
    },
    5: {
        1: "At least one of them is lying, and the reward is not in {p3}'s chest!",
        2: "We are all telling the truth!",
        3: "{p2} is telling the truth and the reward is in his chest."
    },
    6: {
        1: "Both of them are telling the truth. Also, {p2} has the reward in their chest!",
        2: "{p3} is telling the truth.",
        3: "My chest has the reward!"
    }
}

def three_weirdos():

    names = ["Okarin", "Mayushii", "Suzuha", "Daru", "Faris Nyan", "Daru", "Monika", "Yuri", "Sayori", "Daru", "Lelouch", "Shinei", "Light", "L", "Erwin Smith", "Eren", "Mikasa", "Levi", "Sans", "Papyrus", "Lucy", "David", "Maine", "Rebecca", "Adam Smasher", "Kiwi", "Ado"]

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
from random import randrange

def generate_card():
    '''This function was creating your BINGO card'''
    dct = {
        "B": [randrange(1, 15) for _ in range(5)],
        "I": [randrange(16, 30) for _ in range(5)],
        "N": [randrange(31, 45) for _ in range(5)],
        "G": [randrange(46, 60) for _ in range(5)],
        "O": [randrange(61, 75) for _ in range(5)]    
        }
    return dct

def change_if_num_repeats(card):
    '''This function checks if the game card has numbers which is repeats and changes it'''
    my_set = set()
    i = 0
    for key, value in card.items():
        for num in value:
            my_set.add(num)
        if len(my_set) < 5:
            value = list(my_set)
            if key == "B":
                while len(value) != 5:
                    i = randrange(1, 15)
                    if i not in value:
                        value.append(i)
                        card["B"] = value
            if key == "I":
                while len(value) != 5:
                    i = randrange(16, 30)
                    if i not in value:
                        value.append(i)
                        card["I"] = value
            if key == "N":
                while len(value) != 5:
                    i = randrange(31, 45)
                    if i not in value:
                        value.append(i)
                        card["N"] = value
            if key == "G":
                while len(value) != 5:
                    i = randrange(46, 60)
                    if i not in value:
                        value.append(i)
                        card["G"] = value
            if key == "O":
                while len(value) != 5:
                    i = randrange(61, 75)
                    if i not in value:
                        value.append(i)
                        card["O"] = value
        my_set = set()
    return card


# card = generate_card()
# print(change_if_num_repeats(card))

def show_card(card):
    '''This function was showing the BINGO card'''
    print(f"{'B':>5}{'I':>5}{'N':>5}{'G':>5}{'O':>5}")
    for i in range(len(card)):
        for value in card.keys():
            print(f"{card[value][i]:>5}", end="")
        print()


# if __name__ == "__main__":
#     card = generate_card()
#     show_card(card)





from random import randrange
for a in range(3):
    def generate_card():
        '''This function was creating your BINGO card'''
        card = {
            "B": [randrange(1, 15) for _ in range(5)],
            "I": [randrange(16, 30) for _ in range(5)],
            "N": [randrange(31, 45) for _ in range(5)],
            "G": [randrange(46, 60) for _ in range(5)],
            "O": [randrange(61, 75) for _ in range(5)]    
            }
        '''This function checks if the game card has numbers which is repeats and changes it 
            I JUST SOLVED THEM'''
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
    if a == 0:
        card1 = generate_card()
    elif a == 1:
        card2 = generate_card()
    elif a == 2:
        card3 = generate_card()


def show_cards(card1, card2, card3):
    '''This function was showing the BINGO card'''
    print(f"{'B':>5}{'I':>5}{'N':>5}{'G':>5}{'O':>5}\
    {'B':>5}{'I':>5}{'N':>5}{'G':>5}{'O':>5}\
    {'B':>5}{'I':>5}{'N':>5}{'G':>5}{'O':>5}")
    for i in range(len(card1)):
        for value in card1.keys():
            print(f"{card1[value][i]:>5}", end="")
        for _ in range(4):
            print(end=" ")
        for value in card2.keys():
            print(f"{card2[value][i]:>5}", end="")
        for _ in range(4):
            print(end=" ")
        for value in card3.keys():
            print(f"{card3[value][i]:>5}", end="")
        print()


    
    



# if __name__ == "__main__":
#     show_card(card1, card2, card3)





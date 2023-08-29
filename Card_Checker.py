from loto_card import generate_card, card1, card2, card3

def is_win_col1(card):
    '''This function was checks if in card have col winning numbers'''
    for i in card:
        if sum(card[i]) == 0:
            return True
    return False
def is_win_col2(card2):
    '''This function was checks if in card have col winning numbers'''
    for i in card2:
        if sum(card2[i]) == 0:
            return True
    return False
def is_win_col3(card3):
    '''This function was checks if in card have col winning numbers'''
    for i in card3:
        if sum(card3[i]) == 0:
            return True
    return False

def is_win_row1(card):
    '''This function was checks if in card have row winning numbers'''
    for i in range(5):
        sums = 0
        for value in card:
            sums += card[value][i]
        if sums == 0:
            return True
    return False
def is_win_row2(card2):
    '''This function was checks if in card have row winning numbers'''
    for i in range(5):
        sums = 0
        for value in card2:
            sums += card2[value][i]
        if sums == 0:
            return True
    return False
def is_win_row3(card3):
    '''This function was checks if in card have row winning numbers'''
    for i in range(5):
        sums = 0
        for value in card3:
            sums += card3[value][i]
        if sums == 0:
            return True
    return False

def is_win_diag1(card):
    '''This function was checks if in card have diagonal winning numbers'''
    suma = 0
    index = 0
    for i in card:
        suma += card[i][index]
        index += 1
    if suma == 0:
        return True
    return False
def is_win_diag2(card2):
    '''This function was checks if in card have diagonal winning numbers'''
    suma = 0
    index = 0
    for i in card2:
        suma += card2[i][index]
        index += 1
    if suma == 0:
        return True
    return False
def is_win_diag3(card3):
    '''This function was checks if in card have diagonal winning numbers'''
    suma = 0
    index = 0
    for i in card3:
        suma += card3[i][index]
        index += 1
    if suma == 0:
        return True
    return False




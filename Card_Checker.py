from Bingo.loto_card import generate_card

def is_win_col(card):
    '''This function was checks if in card have col winning numbers'''
    for i in card:
        if sum(card[i]) == 0:
            return True
    return False

def is_win_row(card):
    '''This function was checks if in card have row winning numbers'''
    for i in range(5):
        sums = 0
        for value in card:
            sums += card[value][i]
        if sums == 0:
            return True
    return False

def is_win_diag(card):
    '''This function was checks if in card have diagonal winning numbers'''
    suma = 0
    index = 0
    for i in card:
        suma += card[i][index]
        index += 1
    if suma == 0:
        return True
    return False



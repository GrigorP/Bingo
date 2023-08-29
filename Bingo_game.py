from loto_card import card1, card2, card3, show_cards
from Card_Checker import is_win_col1, is_win_col2, is_win_col3,\
    is_win_diag1, is_win_diag2, is_win_diag3,\
    is_win_row1, is_win_row2, is_win_row3
from random import randrange

def play_bingo1(card1):
    '''This function was plays the game and returns the card wich ones win'''
    while not any([is_win_col1(card1), is_win_diag1(card1), is_win_row1(card1)]):
        num = randrange(1, 75)
        for key in card1:
            if num in card1[key]:
                card1[key][card1[key].index(num)] = 0   
    return card1
def play_bingo2(card2):
    '''This function was plays the game and returns the card wich ones win'''
    while not any([is_win_col2(card2), is_win_diag2(card2), is_win_row2(card2)]):
        num = randrange(1, 75)
        for key in card2:
            if num in card2[key]:
                card2[key][card2[key].index(num)] = 0   
    return card2
def play_bingo3(card3):
    '''This function was plays the game and returns the card wich ones win'''
    while not any([is_win_col3(card3), is_win_diag3(card3), is_win_row3(card3)]):
        num = randrange(1, 75)
        for key in card3:
            if num in card3[key]:
                card3[key][card3[key].index(num)] = 0   
    return card3


win_card1 = play_bingo1(card1)
win_card2 = play_bingo1(card2)
win_card3 = play_bingo1(card3)
show_cards(win_card1, win_card2, win_card3)





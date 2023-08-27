import Bingo.loto_card as loto_card
from Bingo.Card_Checker import is_win_col, is_win_diag, is_win_row
from random import randrange

def play_bingo(card):
    '''This function was plays the game and returns the card wich ones win'''
    while not any([is_win_col(card), is_win_diag(card), is_win_row(card)]):
        num = randrange(1, 75)
        for key in card:
            if num in card[key]:
                card[key][card[key].index(num)] = 0    
    return card


card = loto_card.generate_card()
win_card = play_bingo(card)
loto_card.show_card(win_card)





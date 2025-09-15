import random
from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
    single_letter_list = []
    total_letter_list = []
    hand = []
    count = 0

    # make a list of all letters including repetition
    for letter in LETTER_POOL:
        single_letter_list = [letter] * LETTER_POOL[letter]
        total_letter_list.extend(single_letter_list)
    # print(total_letter_list) 

    # use random number as index and pop a letter and return a hand
    while count < 10:
        letter_index = random.randint(0, len(total_letter_list) - 1)    
        single_letter = total_letter_list.pop(letter_index)
        hand.append(single_letter)
        count += 1
    # print(hand)

    return hand

def uses_available_letters(word, letter_bank):

    letter_bank_copy = letter_bank[:]
    word_upper = word.upper()

    for char in word_upper:
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)

        else:
            return False
        
    return True

def score_word(word):
    score = 0
    for char in word.upper():
        if char in SCORE_CHART:
            score += SCORE_CHART[char]

    if len(word) >= 7 and len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    highest_score = 0
    for word in word_list:
        score = score_word(word)    
        if score > highest_score:
            highest_score = score
            highest_word = word
        elif score == highest_score:
            if len(word) < len(highest_word) and len(word) !=10 and len(highest_word) != 10:
                highest_word = word
            elif len(word) == 10 and len(highest_word) != 10:
                highest_word = word
            
    return highest_word, highest_score
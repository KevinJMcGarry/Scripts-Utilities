'''
Python 3
Script that prompts user for a word and outputs a dictionary definition for that word. If the word doesn't exits
in the dictionary, it offers up a close match recommendation.
'''

import os, json, difflib

os.chdir('../word_dictionary')  # outside the function as the location is relative to the user running the function
data = json.load(open('./data.json'))  # data structure containing an abridged dictionary used for testing


def word_dictionary(user_word):
    if user_word in data.keys():
        return '{}: {}'.format(user_word, data[user_word])
    elif len(difflib.get_close_matches(user_word, data.keys())) > 0:  # checking to see if there are any similar words:
        answer = input('did you by chance mean the word {}? Enter \'y\' for yes or \'n\' for no '.format(difflib.get_close_matches(user_word, data.keys())[0])).lower()
        while True:
            if answer == 'y':
                return '{}: {}'.format(difflib.get_close_matches(user_word, data.keys())[0], data[difflib.get_close_matches(user_word, data.keys())[0]])
                # by default the above method returns 3 matches in descending order by similarity
                # the sub[0] function uses the first one.
            elif answer == 'n':  # if user presses 'n'
                return 'ok, {} is not in the dictionary. Exiting the program.'.format(user_word)
            else:
                answer = input('I didn\'t understand your response. Please enter \'y\' for yes or \'n\' for no ')
                continue
    else:  # if there isn't a match or any similar words found
        return '{} is not in the dictionary. Please check your spelling and try again'.format(user_word)

user_word = input('Please enter a word to get its definition: ').lower()
print(word_dictionary(user_word))
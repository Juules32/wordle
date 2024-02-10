from parsing import *

def new_game(message, userdata) -> str:
    userdata[message.author.id] = {}
    userdata[message.author.id]['word'] = get_random_word()
    userdata[message.author.id]['guessed letters'] = []

def make_guess(word, message, userdata):
    for c in word:
        userdata[message.author.id]['guessed letters'].append(c)
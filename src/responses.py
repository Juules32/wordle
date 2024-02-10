from parsing import *
from game import *

GREY = ':white_large_square:'
YELLOW = ':yellow_square:'
GREEN = ':green_square:'

def format_guess(guess):
    result = ''
    for c in guess:
        result += f':regional_indicator_{c}:'
    return result

def format_guess_result(guess, message, userdata):
    result = ''
    for i, c in enumerate(guess):
        if c == userdata[message.author.id]["word"][i]:
            result += GREEN
        elif c in userdata[message.author.id]["word"]:
            result += YELLOW
        else:
            result += GREY
    return result

def is_game_inactive(message, userdata):
    return userdata.get(message.author.id) is None or userdata[message.author.id].get("guessed letters") is None

def get_response(message, userdata) -> str:
    text: str = message.content.lower()

    if text == 'newgame' or text == 'new game' :
        new_game(message, userdata)
        return 'Your word is: \n' + userdata[message.author.id]["word"]
    
    elif text.startswith('guess'):
        if len(text.split(' ')) < 2:
            return 'Invalid guess'
        guess = text.split(' ')[1]
        
        if len(guess) != 5:
            return 'Word is not 5 letters :rage:'
        
        if is_game_inactive(message, userdata):
            return 'Game is inactive'
        
        print(guess)
        
        make_guess(guess, message, userdata)
        return f'{format_guess(guess)}\n{format_guess_result(guess, message, userdata)}'
    
    elif text == 'status':
        pass #make visual keyboard using emojis to show which letters have been used
    
    return 'Command not found'
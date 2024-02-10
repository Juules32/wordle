import json, random

userdata = {}
with open('words.json', 'r') as file:
    secret_words = json.load(file)


GREY = ':white_large_square:'
YELLOW = ':yellow_square:'
GREEN = ':green_square:'

def format_guess(guess):
    result = ''
    for c in guess:
        result += f':regional_indicator_{c}:'
    return result

def format_guess_result(guess, secret_word):
    result = ''
    for i, c in enumerate(guess):
        if c == secret_word[i]:
            result += GREEN
        elif c in secret_word:
            result += YELLOW
        else:
            result += GREY
    return result

def new_game(userid):
    userdata[userid] = {}
    userdata[userid]['secret word'] = random.choice(secret_words)
    userdata[userid]['guessed letters'] = []
    userdata[userid]['guesses left'] = 6

async def make_guess(message, user, guess):
    
    # Verify that input is valid
    if len(guess) != 5:
        return await message.channel.send('Word is not 5 letters :rage:')
    if user is None:
        return await message.channel.send('Game is inactive')
    if not guess in secret_words:
        return await message.channel.send('Guess is not a valid word')
    
    # Modify user state
    for c in guess:
        user['guessed letters'].append(c)
    user['guesses left'] -= 1
    
    # Visualize guess
    await message.channel.send(f'{format_guess(guess)}\n{format_guess_result(guess, user["secret word"])}\n')
    
    # Check if guess is correct
    if guess == user['secret word']:
        await message.channel.send('You won!')
        userdata[message.author.id] = None
    
    # Check if there are no guesses left
    elif user['guesses left'] == 0:
        await message.channel.send(f'You lost! The correct answer was: {user["secret word"]}')
        userdata[message.author.id] = None
        
    # Otherwise, display guesses left
    else:
        await message.channel.send(f'You have {user["guesses left"]} guess{"es" if user["guesses left"] > 1 else ""} left')
        

async def get_responses(message) -> None:
    
    if not message.content:
        print('(Message was empty because intents were not enabled probably)')
        return
    
    try:
        text = message.content.lower()
        userid = message.author.id
        user = userdata.get(userid)

        if text == 'newgame' or text == 'new game':
            new_game(userid)
            return await message.channel.send('New game started')
        
        elif text.startswith('guess'):
            if len(text.split(' ')) >= 2:
                return await make_guess(message, user, text.split(' ')[1]) 
            else:
                return await message.channel.send('Invalid guess')
                
        elif text == 'status':
            pass #make visual keyboard using emojis to show which letters have been used
        
        else:
            return await message.channel.send('Command not found')
    except Exception as e:
        print(e)
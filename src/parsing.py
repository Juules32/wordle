import json, random

def get_userdata_path(userid):
    return f'userdata/{userid}.json'

def load_data(userid):
    try:
        # Try to open the file for reading
        with open(get_userdata_path(userid), 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        with open(get_userdata_path(userid), 'w') as file:
            save_data(userid, [])

def save_data(userid, data):
    with open(get_userdata_path(userid), 'w') as path:
        json.dump(data, path, indent=4)
        
def get_random_word():
    with open('words.json', 'r') as file:
        return random.choice(json.load(file))
    

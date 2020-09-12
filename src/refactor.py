import config

def refactor(recipient, text):
    for key, value in config.recipients[recipient].items():
        text = text.replace('$' + key + '$', value)
    
    return text
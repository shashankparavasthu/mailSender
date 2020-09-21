import config

def refactor(recipient, text):
    # recipient is the recipient username
    for detail, detail_value in config.recipients[recipient].items() :
        key  = config.dynamic_character + detail + config.dynamic_character
        #replace key with detail_value if it is found in the text
        if key in text: 
            text = text.replace(key, detail_value) 

    return text
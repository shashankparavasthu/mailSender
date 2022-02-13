import config

def refactor(recipient_number, text):
    # recipient is the recipient username
    for detail, detail_value in config.recipients[recipient_number].items() :
        key  = config.dynamic_character + detail + config.dynamic_character
        #replace key with detail_value if it is found in the text
        if key in text: 
            text = text.replace(key, str(detail_value)) 

    return text
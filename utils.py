

def text_filter_based_on_key(filter: str, content: str, separator: str) -> dict:
    """
    Filters the content based on defined filter, separator will separate key and value 
    (e.g in key: value separator is ':')
    """
    not_ok_state = {}
    purified_text = content.strip().split('\n')
    purified_text = [item for item in purified_text if item] # removes the empty string made from empty \n
    for line in purified_text:
        separated_line = line.split(separator)
        separated_line = [item.strip() for item in separated_line] # removed the space in "key: value"
        if filter not in separated_line:
            not_ok_state[separated_line[0]] = separated_line[1] # creates a dictionary that service name is the key and status is the value
    return not_ok_state



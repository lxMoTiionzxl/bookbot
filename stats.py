def get_num_words (book):
    """
        Input: book, str
        Ouput: number of words, int
    """

    words = book.split()
    return len(words)

def get_letters_count (book):
    """
        Input: book, str
        Output: letter/symbols/spaces count, dict
    """

    count_dict = {}

    for letter in book.lower():
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return count_dict

def sort_on(items):
    return items["num"]

def sort_dict_value (dict):
    """
        Input: dict
        Output: list of dict {'char','num'} 
    """

    list_entries = []
    
    for key in dict.keys():
        dict_entry = {}
        dict_entry['char'] = key
        dict_entry['num'] = dict[key]  
        list_entries.append(dict_entry)

    list_entries.sort(reverse=True, key=sort_on)
    return list_entries
def num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1       
    return char_dict

def sort_on(items):
    return items["num"]

def report_gen(char_dictionary):
    dict_list = []
    for key, value in char_dictionary.items():
        if key.isalpha():
            temp_dict = {}
            temp_dict["char"] = key
            temp_dict["num"] = value
            dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

#character_count("Hello my name is luca")
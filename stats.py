# Count the number of words in the file
def word_count(file_contents):
    word_list = file_contents.split()
    word_number = len(word_list)
    return word_number

# Count the number of characters and file it into a list of dictionaries
def char_count(file_contents):
    lowered_string = f"{file_contents.lower()}"
    character_list = list(lowered_string)
    characters_set = set()
    character_dict = {}
    for character in character_list:
        if character not in characters_set:
            characters_set.add(character)
            character_dict[f"{character}"] = 1
        else:
            character_dict[f"{character}"] += 1
    return character_dict

# Define what value we're sorting on
def sort_on(items):
    return items["count"]

# Sort the dictionary list we've created
def sort_dict(character_dict):
    dict_list = []
    for character in character_dict:
        char = character
        value = character_dict[character]
        dict_list.append({"character": f"{char}", "count": value})
    dict_list.sort(reverse=True, key=sort_on)
    #print(f"Sorted dictionary looks like...")
    #print(dict_list)
    return dict_list


    
        
    

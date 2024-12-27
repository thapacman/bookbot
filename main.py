def main():
    book_path = "books/frankenstein.txt"
    text = get_full_text(book_path)
    wordcount = get_word_count(text)
    characterdict = count_characters(text)
    chardictlist = convert_dict_to_dictlist(characterdict)
    chardictlist.sort(reverse=True, key=sort_on)
    print(f"=== Begin report of {book_path} ===")
    print(f"{wordcount} words in the text.")
    for chardict in chardictlist:
        print(f"The '{chardict.get("char")}' character appears {chardict.get("count")} times")
    print(f"=== End report on {book_path} ===")

def get_full_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(fulltext):
#Create array by splitting words
    wordarray = fulltext.split()
#Return word count using length of array
    return len(wordarray)


def count_characters(counttext):
    #convert to lowercase
    lowcharacters = counttext.lower()
    #create character count dictionary
    characterdictionary = {}
    for character in lowcharacters:
        if characterdictionary.get(character) is not None:
            characterdictionary[character] += 1
        else:
            characterdictionary[character] = 1
    return characterdictionary


def convert_dict_to_dictlist(charDict):
#Create new list
    chardlist = []
    for k in charDict:
#check if the key is an alpha, thn proceed
        if k.isalpha():
#Create a temporary dictionary to append into the character dictionary list
            tDict = {}
            tDict = {"char": f"{k}", "count": charDict.get(k)}
            chardlist.append(tDict)
    return chardlist


def sort_on(dict):
#Define the count key for sorting
    return dict["count"]

main()
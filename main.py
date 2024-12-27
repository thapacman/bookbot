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


#    print(f"{chardictlist}")
#    print(f"characterdict looks like {characterdict}")
#    print(f"chardlist looks like... {chardictlist}")

def get_word_count(fulltext):
    wordarray = fulltext.split()
    return len(wordarray)

def get_full_text(path):
    with open(path) as f:
        return f.read()

def count_characters(counttext):
    #convert to lowercase
    lowcharacters = counttext.lower()
    #create character dictionary using for loop
    characterdictionary = {}
    for character in lowcharacters:
        if characterdictionary.get(character) is not None:
            characterdictionary[character] += 1
        else:
            characterdictionary[character] = 1
    return characterdictionary

def convert_dict_to_dictlist(charDict):
    chardlist = []
    for k in charDict:
        if k.isalpha():
            tDict = {}
            tDict = {"char": f"{k}", "count": charDict.get(k)}
#            print(f"tDict set to: {tDict}")
            chardlist.append(tDict)
#            print(f"chardlist appended, now contains: {chardlist}")
    return chardlist

def sort_on(dict):
    return dict["count"]

main()
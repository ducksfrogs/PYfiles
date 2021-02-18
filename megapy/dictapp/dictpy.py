import json
from difflib import get_close_matches



data = json.load(open('data.json'))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("did you mean %s instead? Enter Y if yes" % get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
    else:
        return "The word does not exist"

word = input("Enter a word ")

li = translate(word)
if type(li) == list:
    for i in li:
        print(i)
else:
    print(li)

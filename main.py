import json

# File read and store the json in to a dictionary.

f = open('./dict.json', 'r')
dictionarydata = json.load(f)
f.close()

word = input('Enter word : ')
print(word)

# Find the word in the dictionary
if word in dictionarydata.keys():
    resultList = dictionarydata[word]
    for meaning in resultList:
        print(meaning)
else:
    print('Word not found')        
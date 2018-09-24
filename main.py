import json

# File read and store the json in to a dictionary.

f = open('./dict.json', 'r')
dictionarydata = json.load(f)
f.close()

print(dictionarydata['India'])
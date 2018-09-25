import json

# File read and store the json in to a dictionary.
dictionarydata = {}
try:
    f = open('./dict.json', 'r')
    dictionarydata = json.load(f)
    f.close()
except:
    print('Error occured while reading from the file')

def write_dic_data(data):
    try:
        jstring = json.dumps(data)
        if type(data) is dict:
            f = open('./dict.json','w')
            f.write(jstring)
            f.close()
        else:
            print('type err')   
    except:
        print('Check your data')   
        

# Find the word in the dictionary
def search_dictionary():
    word = input('Enter word : ')

    if word in dictionarydata.keys():
        resultList = dictionarydata[word]
        for idx, meaning in enumerate(resultList):
            print(idx + 1,'.', meaning)
    else:
        print('Word not found')
        new_word_def = []
        def_counter = 1
        while def_counter > 0:
            definition = input('Enter definition of the entered word / X to quit : ')
            if definition != 'X':
                new_word_def.append(definition)
            else:
                def_counter = 0

        # Append to the dictionary
        if len(new_word_def) > 0 :
            dictionarydata[word] = new_word_def
            #update the data file
            write_dic_data(dictionarydata)
            search_dictionary()

search_dictionary()  
#write_dic_data({'ABC':'bcs'})          

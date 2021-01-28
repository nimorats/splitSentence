## Importing the libraries

import nltk
import re
from nltk.corpus import stopwords
#nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

## Initiating the variables

text=''' I went to Pune but nice Mumbai'''   # This will be our statement which will be processed further by calling the functions
count=0
conjunctions = []
split_definite_list = ('but', 'yet') #This is the first list
split_undefinite_list = ('and')      #This is the second list

## Functions

def split_definite():
    print("Function split definite was called.")
    #some code here
    
def return_tokens(text):
    token = nltk.word_tokenize(text)
    return token

def return_pos_tag(token):
    pos_tagged_tokens = nltk.pos_tag(token)
    return pos_tagged_tokens

def return_sentiment(text):
    print(" ")

def return_true_if_verb(text):
    count = 0
    tagged_tokens = return_tokens(text)
    split_sentence_token = return_pos_tag(tagged_tokens)
    for i in range(0,len(split_sentence_token)):
        print(str(i) + " . " + str(split_sentence_token[i]))
        if split_sentence_token[i][1] in ['VB','VBD','VBG','VBN','VBP','VBZ'] :
            count = count + 1

    if (count > 0):
        return True
    else:
        return False
    


## Main set of the code

# Step 1: Tag the words
text_token = return_tokens(text)
pos_tagged_tokens = return_pos_tag(text_token)


for i in range(0,len(pos_tagged_tokens)):
    #print("Word: " + str(pos_tagged_tokens[i][0] + " ---- and its characteristic : " + str(pos_tagged_tokens[i][1])))
    if(pos_tagged_tokens[i][1] == 'CC'):
        conjunctions.append(pos_tagged_tokens[i][0])
        #print(pos_tagged_tokens[i][0])
        count=count+1
        
# Step 2 : Do we ned to split
seperator = '|'
list_of_conjunctions = seperator.join(conjunctions)
#print(list_of_conjunctions)
split_text = re.split(list_of_conjunctions,text)
if count>0:
    print(" Report for the statement ")
    print(" There are " + str(len(split_text)) + " sentences as follows ")
    print("\n")
    for statement in range(0,len(split_text)):
        print(str(statement + 1) + ". " + str(split_text[statement]))
        text = split_text[statement]
        print("The text is " + text)
        #pos_tagged_token_split = return_pos_tag(text)
        verb_status = return_true_if_verb(text)
        if(verb_status == True):
            print("Yes it has verb in it")
            
        else:
            print("No it doesnt have any verb in it")
            
else:
    print(" No need to Split ")







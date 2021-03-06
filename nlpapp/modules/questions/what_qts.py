#Author: Indrajith Indraprastham
#Date:  Wed Dec 20 00:12:39 IST 2017 (last update)
from textblob import TextBlob
from textblob import Word

import requests
import json
import nltk
from nltk.tag.stanford import CoreNLPPOSTagger

import sys
from nltk import sent_tokenize
try:
    from .Questions import Questions
except:
    from Questions import Questions

def parse(string):
    """
    Parse a paragraph. Devide it into sentences and try to generate quesstions from each sentences.
    """
    
    try:
        txt = TextBlob(string)
        # Each sentence is taken from the string input and passed to genQuestion() to generate questions.
        for sentence in sent_tokenize(string):  #modified
            genQuestion(sentence)

    except Exception as e:
        raise e



def genQuestion(line):
    print('yooo', line)
    """
    outputs question from the given text
    """
    bucket = {}               # Create an empty dictionary

    # POS tagging
    text = CoreNLPPOSTagger(url='http://localhost:9000').tag(line.split())
    for i,j in enumerate(text):  # text is the parts-of-speach tags in English
        if j[1] not in bucket:
            bucket[j[1]] = i  # Add all tags to the dictionary or bucket variable

    

    if type(line) is str:     # If the passed variable is of type string.
            line = TextBlob(line) # Create object of type textblob.blob.TextBlob

     
    print('hey', line)
    question = ''
    l1 = ['NNP', 'VBG', 'VBZ', 'IN']
    l2 = ['NNP', 'VBG', 'VBZ']
    

    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l5 = ['PRP', 'VBG', 'VBD']
    l6 = ['NNP', 'VBG', 'VBD']
    l7 = ['NN', 'VBG', 'VBZ']

    l8 = ['NNP', 'VBZ', 'JJ']
    l9 = ['NNP', 'VBZ', 'NN']

    l10 = ['NNP', 'VBZ']
    l11 = ['PRP', 'VBZ']
    l12 = ['NNP', 'NN', 'IN']
    l13 = ['NN', 'VBZ']


    # With the use of conditional statements the dictionary is compared with the list created above

    
    if all(key in  bucket for key in l1): #'NNP', 'VBG', 'VBZ', 'IN' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['NNP']]+ ' '+ line.words[bucket['VBG']] + '?'

    
    elif all(key in  bucket for key in l2): #'NNP', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['NNP']] +' '+ line.words[bucket['VBG']] + '?'

    
    elif all(key in  bucket for key in l3): #'PRP', 'VBG', 'VBZ', 'IN' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['PRP']]+ ' '+ line.words[bucket['VBG']] + '?'

    
    elif all(key in  bucket for key in l4): #'PRP', 'VBG', 'VBZ' in sentence.
        question = 'What ' + line.words[bucket['PRP']] +' '+  ' does ' + line.words[bucket['VBG']]+ ' '+  line.words[bucket['VBG']] + '?'

    elif all(key in  bucket for key in l7): #'NN', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['NN']] +' '+ line.words[bucket['VBG']] + '?'

    elif all(key in bucket for key in l8): #'NNP', 'VBZ', 'JJ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?'

    elif all(key in bucket for key in l9): #'NNP', 'VBZ', 'NN' in sentence
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?'

    elif all(key in bucket for key in l11): #'PRP', 'VBZ' in sentence.
        if line.words[bucket['PRP']] in ['she','he']:
            question = 'What' + ' does ' + line.words[bucket['PRP']].lower() + ' ' + line.words[bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l10): #'NNP', 'VBZ' in sentence.
        question = 'What' + ' does ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l13): #'NN', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NN']] + '?'

    # When the tags are generated 's is split to ' and s. To overcome this issue.
    if 'VBZ' in bucket and line.words[bucket['VBZ']] == "’":
        question = question.replace(" ’ ","'s ")

    # Print the genetated questions as output.
    print(question)
    if question != '':
        print('\n', 'Question: ' + question )
    return question
   

def main():  
    """
    Accepts a text file as an argument and generates questions from it.
    """
    #verbose mode is activated when we give -v as argument.
    #global verbose 
    #verbose = False

    # Set verbose if -v option is given as argument.
    """
    if len(sys.argv) >= 3: 
        if sys.argv[2] == '-v':
            print('Verbose Mode Activated\n')
            verbose = True
    """
    # Open the file given as argument in read-only mode.
    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    print('\n-----------INPUT TEXT-------------\n')
    print(textinput,'\n')
    print('\n-----------INPUT END---------------\n')

    # Send the content of text file as string to function parse()
    parse(textinput)


class What(Questions):
    def modify(self):
        return genQuestion(self.text)

if __name__ == "__main__":
    w = What(input())
    print(w.get_text())


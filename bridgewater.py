#!/usr/bin/python
#Chris Reeves
#Bridgewater Interview Question
# assume I can use python to solve
# assume text input can fit in memory
# assume text input is ascii
# assume that I can make many passes over the text document, because python replace searches the entire document.
# assume I can make more than one pass over the document / not a streaming algorithm
# assume that there are many edge cases I missed such as Inc. that can be added to the replacement list
# assume I can replace . with _ or some other special character to deal with abbreviations / Initials


import sys
import re
import collections

WordDictionary = {}


def ReadFile(articleUrl):
    fh = open(articleUrl,"r")
    return fh.read()

def Populate(sentenceItem,sentenceIndex):
    for currentWord in sentenceItem.split(" "):
        currentWord = currentWord.replace(".","").replace('"','')
        if(currentWord not in WordDictionary):
            WordDictionary[currentWord] = [sentenceIndex]
        else:
            WordDictionary[currentWord] += [sentenceIndex]

def Display():
    for key in sorted(WordDictionary.keys()):
        print(key + "  {",len(WordDictionary[key])," : ",WordDictionary[key], "} \n")

if(len(sys.argv)> 1):
    fileName = sys.argv[1]

    # make the article text lowercase and strip out special characters
    articleText = ReadFile(fileName).lower().replace("\n"," ").replace(","," ").replace("-"," ").replace('"',' ')

    #remove commonly known edge cases Mrs. / Mr.  This list can be expanded, there are lots of missing edge cases
    articleText = articleText.replace("mrs.","mrs").replace("mr.","mr").replace("ms.","ms")

    articleText = articleText.replace("? ",". ").replace("! ",". ")
    # convert all of the terminations to the same termination string

    # this regex will look for any pattern of repeating . and letter which might indicate abbreviations / acronyms
    abbreviationPattern = r"((\w\.){2,})\s"

    # I do not handle cases like Inc. Corp. ...ect they can be added to the replacement list if necessary
    result = re.findall(abbreviationPattern,articleText)

    # I use a greedy regex so need to get the outer selection
    for abbreviation in result:
        articleText = articleText.replace(abbreviation[0],abbreviation[0].replace(".","_"))
        #print (abbreviation[0])

    # print (articleText)

    sentences = articleText.split(". ")
    for s in sentences:
        Populate(s,sentences.index(s))
    #print (sentences)

    # display the sorted dictionary
    Display()
else:
    print("expects file location as command line argument")
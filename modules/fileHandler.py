

from os import close
from .voikkoPipeline import handleGrammarCheck

from typing import ChainMap, List


# read file and make it into propper format
# aka a big string or list of strings

# if we have txt file then just read it if it it tex file then strip it from bs



def handleFile(path:str):

    #if path is .tex then do something lese
    #rn we only do plaintext

    if path[-4:] ==".txt":
        f=open(path)
        handleGrammarCheck(f.read())
        f.close()
    else:
        handleTexFile(path)



    pass



def removeLeadingWhitespace(line:str)->str:
    retstring=line
    for char in line:
        if char==' ' or char == "\n" or char =="\t":
            retstring=retstring[1:]
        else:
            break

    return retstring


def removeTrailingExcapeChars(line:str)->str:
    retstring=line
    #reverse loop string
    for charindex in range(len(line),0,-1):
        char=line[charindex-1]
        if char=="\\" :
            retstring=retstring[:-1]
        if char== '\n':
            retstring=retstring[:-1]
            

    return retstring



def handleTexFile(path:str):

    #tex rules
    #for starters if the line starts with % or a single \ then delet it
    # later we will handle the other things
    # then if the list is a normal thing then remove all \\ from the strings


    parsedLines:List[str]=[]

    file=open(path,"r")
    for line in file:
        line=removeLeadingWhitespace(line)

        if line=="":
            continue
        if line[0]=="\\" or line[0]=="%":
            continue

        line=removeTrailingExcapeChars(line)
        parsedLines.append(line)
        pass

    file.close()

    fullstr=""
    for i in parsedLines:
        if i[-1]!=" ":
            fullstr+=i+" "

    

    handleGrammarCheck(fullstr)








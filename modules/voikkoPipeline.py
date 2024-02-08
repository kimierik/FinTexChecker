
import libvoikko


from typing import List





def prettyPrintErrors(text:str,errors:List[libvoikko.GrammarError] ):
    for error in  errors:
        print(error.shortDescription)
        print(text[error.startPos:error.startPos+error.errorLen])
        print(" ")
        




def splitTextIntoWords(text:str)->List[str]:
    words=[]

    word=""
    for char in text:
        if char==' ' or char=='\n':
            words.append(word)
            word=""
        else:
            word+=char





    return words




def handleGrammarCheck(text:str):
    """ 
    the main function for doing the grammar check.
    takes in a string with all the text and analyses it with Voikko
    """

    v=libvoikko.Voikko("fi")


    # spell check typos
    # split text into words 
    #there is funciton for slittting into sentences but we dont want that 

    v.setIgnoreDot(True)
    words=splitTextIntoWords(text)
    for word in words:
        if not v.spell(word):
            print("\"",word,"\""," spelling mistake ", v.suggest(word))
            print("")


    v.setIgnoreDot(False)



    #grammar check whole text
    errors=v.grammarErrors(text,"fi")
    

    #prettry
    prettyPrintErrors(text,errors)

    #print(errors)












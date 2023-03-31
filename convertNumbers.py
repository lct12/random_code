# Create a function that converts a list containing words and numbers to one that is words and numerals

from num2words import num2words
def convertNumbers(document):
    newDocument = []
    # Assuming review is a list of words
    for word in document:
        try:
            newWord = num2words(word)
        except: # when the word is not a numeral but just a normal word
            newWord = word
        newDocument.append(newWord)
    return newDocument

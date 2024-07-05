#Imports to be used in the defined function
import pandas as pd
import string
import sys

def countWords(inputText: str, predefinedWords: str, raiseError: bool = False, displayResult:bool = True) -> None:
    #Initialize variables to take in both files and read them
    readText = None
    checkedWords = None
    with open(inputText, 'r') as f:
        readText = f.read()
    with open(predefinedWords, 'r') as f:
        checkedWords = f.read()

    #Check to see if an error should be thrown for empty or whitespace files
    if (raiseError):
        if (len(readText) == 0) or (readText.isspace()):
            raise Exception("Sorry, the inputText file is empty or only has whitespace")
        if (len(checkedWords) == 0) or (checkedWords.isspace()):
            raise Exception("Sorry, the predefinedWords file is empty or only has whitespace")

    #Create a dictionary from the predefined words file and split the input text by records
    predefCount = dict(zip(checkedWords.translate(str.maketrans('', '', string.punctuation)).lower().split(), [0]*len(checkedWords)))
    splitText = readText.translate(str.maketrans('', '', string.punctuation)).lower().split()

    #Loop through the input text file to search for matches and increment the count in predefined words dictionary
    for x in splitText:
        if x in predefCount:
            predefCount[x] += 1

    #Create a pandas dataframe from dictionary and print out the result as well as save it to a csv file
    result = pd.DataFrame(data=predefCount.items(), columns=['Predefined word','Match count'])
    if displayResult:
        print(result)
    result.to_csv('Output.csv',index=False)

if __name__ == "__main__":
    inputText = sys.argv[1]
    predefinedWords = sys.argv[2]
    raiseError = False
    displayResult = True

    if len(sys.argv) > 3:
        raiseError = sys.argv[3]
    if len(sys.argv) > 4:
        displayResult = sys.argv[4]

    countWords(inputText, predefinedWords, raiseError, displayResult)
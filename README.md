# predefined-word-match
## How to Run the Program
- There are three ways to run the program and produce the desired result
  - The First method is through the command line of the terminal.
    - Open a terminal into the folder where the program and input files are stored
    - Type into the terminal the command "python wordMatch.py variable1, variable2, variable3, variable4"
      - Each variable# should be replaced with either the filepath/filename or True/False. For more details check the Function Parameters section
    - The result will be printed on the terminal, but if the result is too long or unclear it is also saved in a "Output.csv" file located in the same directory
  - The Second method is through the included ipynb file.
    - Open the ipynb file and in the navigation bar under "Run" click "Run Selected Cell"
    - Repeat the above step for every cell (box with code) except the very last one
    - Before running the last cell ensure that the two variables "inputText" and "predefinedWords" are set to the correct filepath
      - For which file to set in which variable look under the section "countWords(inputText, predefinedWords, raiseError, displayResult) Function Parameters"
    - Run the last cell with the correct values
    - The result will be printed below the cell and saved to a Output.csv file located in the same directory
  - The Third method is by importing the funtion in another Python script
    - Make sure both scripts are located in the same directory
    - In the script you plan to run the code in type in "from wordMatch import countWords" to import the countWords function from the wordMatch script
    - Now simply call the function countWords with all parameters filled in
      - For information on what parameters the function supports check the Function Parameters section
- countWords(inputText, predefinedWords, raiseError, displayResult) Function Parameters:
  - inputText: The txt file containing the text document you would like to look for word matches from
  - predefinedWords: The txt file containing the list of predefined words you would like to search for
  - raiseError: Set to True if you would like an error to occur if either input files are empty or only whitespace. Default False
  - displayResult: Set to True if you would like the output to be printed in the terminal or False if you would not. Default True

## What Has Been Tested
- A variety of different standard and edge case uses have been tested including but not limited to:
  - Records that have punctuation in the middle of the word (-, :, etc.)
  - Records that contain the predefined words as a substring (Firstname vs. name)
  - Different case words
  - Trailing and leading whitespaces in both provided files
  - Empty predefined words file
  - Empty input text file
  - Single line text file and single line predefined words
  - 10K line predefined word file
  - Files located in different directories

## Assumptions
- The file sizes are small and the predefined words list is guaranteed not to exceed 10K entries, so loading data into memory should not be an issue (No need for chunking)
- Input file has records separated by new line, so assumption is there will not be any words spilled over to the next line
- Punctuation will be entirely removed from both predefined words and the input file (e.g. temp@gmail.com will be tempgmailcom and hyper-fixated will be hyperfixated)
- If hyphens or other special characters exist in a word in one file but not the other they will be treated as the same word
- Results will be displayed as "Predefined word" and "Match count" across entire text document (not individual match count of each line)
- Output order does not matter
- Input files will be provided to the function in the same directory as the function
- No restrictions provided on programming language or what imports are allowed
- Whichever machine is running the program will have minimum Python 3, Pandas, and NumPy installed

# Import Pandas Library
import pandas as pd

# Assigning Values to Alphabets Dictionary
alphabets =    {'1': ['A', 'H', 'O', 'V'],
                '2': ['B', 'I', 'P', 'W'],
                '3': ['C', 'J', 'Q', 'X'],
                '4': ['D', 'K', 'R', 'Y'],
                '5': ['E', 'L', 'S', 'Z'],
                '6': ['F', 'M', 'T', ''],
                '7': ['G', 'N', 'U', '']
}
# Making Data Frame of Alphabets using Pandas
data = pd.DataFrame(alphabets)

# Printing Necessary Instructions
print('\nWelcome to the Game named " - Guess Your Name - "\n')
print('Think about a Name and Let me Guess')
print('Enter Empty space when Spellings are finished.\n')
print(data)

# Appending First Input
words = []
while True:
    word = input('Start Entering the Columns Name from Table Below :').upper()
    if word != ' ' and word != '':
        words.append(word)
    else:
        break

# Appending First Selection
selected = []
for w in words:
    selected.append(alphabets[w])

# Printing Second Table
print(pd.DataFrame(selected))

# Inputting Second Guessing Table and Final Word
final_words = []
guessed_word = []
while True:
    final_word = input('Start Entering the New Columns from Table Below :')
    if final_word != ' ' and final_word != '':
        final_words.append(int(final_word))
    else:
        break

# Saving Guessed Word
for i in range(len(selected)):
    guessed_word.append(selected[i][final_words[i]])

# The Guessed Word
print('\n\nGuessed Word :', guessed_word, '\n')
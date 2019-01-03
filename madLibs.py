#! python3
# Program reads in text files and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re

# Define words to replace.
grammarRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# Create duplicate file of original.
sampleFile = open('sample.txt')
sampleContent = sampleFile.read()
newFile = open('sample1.txt', 'w')
newFile.write(sampleContent)
newFile.close()
sampleFile.close()

# Prompt user for substitutes after identifying to be replaced words.
subs = []
for capWord in grammarRegex.findall(sampleContent):
    if capWord.startswith('A'):
        subs.append(input('Enter an ' + capWord.lower() + ': '))
    elif capWord.startswith('V'):
        subs.append(input('Enter a verb in past tense: '))
    else:
        subs.append(input('Enter a ' + capWord.lower() + ': '))

# Open duplicate file and replace words one-by-one.
for i in range(len(subs)):
    newFile = open('sample1.txt')
    newFileContent = newFile.read()
    newFile.close()
    newFile = open('sample1.txt', 'w')
    newFile.write(grammarRegex.sub(subs[i], newFileContent, 1))
    newFile.close()

newFile = open('sample1.txt')
newFileContent = newFile.read()
print(newFileContent)

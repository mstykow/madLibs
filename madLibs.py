#! python3
# Program reads in text files and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re

# Define words to replace.
grammarRegex = [re.compile('ADJECTIVE'), re.compile('NOUN'), re.compile('ADVERB'), re.compile('VERB')]

# Create duplicate file of original.
sampleFile = open('sample.txt')
newFile = open('sample1.txt', 'w')
newFile.write(sampleFile.read())
newFile.close()
sampleFile.close()

# Prompt user for substitutes.
subs = []
subs.append(input('Enter an adjective: '))
subs.append(input('Enter a noun: '))
subs.append(input('Enter an adverb: '))
subs.append(input('Enter a verb: '))

# Open duplicate file and replace words one-by-one.
for i in range(len(grammarRegex)):
    newFile = open('sample1.txt', 'r')
    newFileContent = newFile.read()
    newFile.close()
    newFile = open('sample1.txt', 'w')
    # print(grammarRegex[i].sub(subs[i],newFileContent)) # Test line: uncomment if needed.
    newFile.write(grammarRegex[i].sub(subs[i],newFileContent))
    newFile.close()

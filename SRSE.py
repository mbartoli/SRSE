"""
SRSE (Spanish Readability Search Engine)

@author: mbartoli
"""

import time
import pprint
import sys
import nltk.data


def countSyllables(word): 
    """
    Returns the number of syllables in a word
    """
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!,")
        #If first letter is a vowel
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
            #Handles compound-vowel syllables
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
        #handles words like 'scene'
    if word.endswith('e'):
        count -= 1
        #handles words like 'rustle'
    if word.endswith('le'):
        count += 1
        #every word we miss must make a sound
    if count == 0:
        count +=1
    return count


def scoreHuerta(text):
    tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
    sample = tokenizer.tokenize(text.decode("utf8"), text)
    totalSentences = len(sample)
    totalWords = 0
    totalSyllables = 0

    for i in range(0, totalSentences):
        sentence = sample[i].split()
        numOfWords = len(sentence)
        for j in range(0, numOfWords):
            totalSyllables = totalSyllables + countSyllables(sentence[j])
        totalWords = totalWords + numOfWords


def main():
    sentence = "Hola, come estas mi amigo"
    print scoreHuerta(sentence)


if __name__ == "__main__":
    main()

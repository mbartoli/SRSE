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


def main():
    word = "Beetle"
    print countSyllables(word)


if __name__ == "__main__":
    main()

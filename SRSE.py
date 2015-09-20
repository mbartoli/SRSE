"""
SRSE (Spanish Readability Search Engine)

@author: mbartoli
"""

import time
import pprint
import sys
import nltk.data
import math

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
    """
    The Huerta Reading Ease is a Modified Flesch Reading Ease 
    for Spanish Texts.

    Scores run roughly from 30 to 100, with higher scores being easier to read.
    
    Huerta Reading Ease = 206.84 - (0.60 * P) - (1.02 * F)
    (Using 100 word chunks of text)
    P = Number of syllables per 100 words
    F = Number of sentences per 100 words
    """
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

    # avg number of syllabes per 100 words 
    buckets = float(totalWords) / 100
    #print "totalSyllables " + str(totalSyllables) 
    #print "totalWords " + str(totalWords)
    #print "totalSents " + str(totalSentences)
    P = (float(totalSyllables) / totalWords) * 100
    F = (float(totalSentences) / totalWords) * 100

    # Huerta Reading Ease = 206.84 - (0.60 * P) - (1.02 * F)
    score = 206.84 - (0.60 * P) - (1.02 * F) 
    return score


def main():
    sentence = "Un grupo de venezolanos y colombianos marcharon hoy por las calles de Nueva York para reclamar la liberacion del opositor venezolano Leopoldo Lopez y para pedir que se garanticen los derechos de la poblacion afectada por la crisis fronteriza entre los dos paises. Decenas de manifestantes se concentraron primero ante el consulado de Venezuela, en el Midtown de Manhattan, y luego se desplazaron a pie por esa centrica zona hasta concluir frente a la sede de la mision venezolana ante Naciones Unidas. Portando banderas venezolanas, colombianas y estadounidenses, los participantes en la protesta mostraron tambien numerosos carteles contra el Gobierno de Nicolas Maduro y expresando su solidaridad con los colombianos expulsados recientemente del pais vecino."
    print scoreHuerta(sentence)


if __name__ == "__main__":
    main()

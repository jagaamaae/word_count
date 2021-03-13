#file = open('./twain.txt')
#open our file and store it

from sys import argv
#from collections import counter

word_counts = {}
#creating an empty dictionary

def count_words(filename):

        text = open(filename).read()
        words = text.rstrip().split()
         # Set the word count to whatever it was + 1; if it wasn't found at all,
        # we'll use `.get(word, 0)` to return 0 if the word wasn't already in
        # the dictionary
        for word in words: 
            word_counts[word] = word_counts.get(word, 0) + 1 
        # Set the word count to whatever it was + 1; if it wasn't found at all,
        # we'll use `.get(word, 0)` to return 0 if the word wasn't already in
        # the dictionary
        # no_punct = ""
        # for char in text:
        #     if char.isalpha() or char == " ":
        #         no_punct += char
        # word_list = no_punct.split(" ")
        # word_counter = Counter(word_list)
        return word_counts
count_words('test.txt')

def print_words():
    for word, count in word_counts.items():
        print (word, count)
print_words()

#Alternate solutoin

def tokenize(filename):
    """Return list of words from file"""

    tokens = []

    with open(filename) as text_file:
        for line in text_file:
            # strip whitespace from the end of the line, and then split it into
            # words (the default argument in both rstrip() and split() is
            # whitespace)
            words = line.rstrip().split(" ")

            # add the words to our list of tokens
            tokens.extend(words)

    return tokens       

tokenize("test.txt")     

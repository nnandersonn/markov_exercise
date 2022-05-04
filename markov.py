"""Generate Markov text from text files."""

from posixpath import split
# from random import Random, choice
import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    source_string = open(file_path)

    return source_string.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    split_text = text_string.split()
    
    for i in range(len(split_text)):
        if i + 2 < len(split_text):
            if (split_text[i], split_text[i+1]) in chains:
                chains[(split_text[i], split_text[i+1])].append(split_text[i+2])
            else:
                chains[(split_text[i], split_text[i+1])] = [split_text[i+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    link = (random.choice(list(chains)))
    words = [link[0], link[1]]
    words.append(random.choice(chains[link]))
    
    while (words[-2], words[-1]) in chains:
        key = (words[-2], words[-1])
        words.append(random.choice(chains[key]))


    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

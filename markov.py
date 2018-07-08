"""Generate Markov text from text files."""

import random
#import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f = open(file_path,"r")
    file_contents = f.read()
    f.close()

    return file_contents

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

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
    words = text_string.split()

#    for item in ls:
    for i in range(len(words) - 2):
        bigram = words[i:i+2]
        bigram_t = tuple(bigram)
        chains[bigram_t] = chains.get(bigram_t,[]) + [words[i+2]]
        #print(bigram,words[i+2])



        # for i in chains.items():
        #     print (i)
    return chains

# print(make_chains(open_and_read_file("green-eggs.txt")))

def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = random.choice(list(chains.keys()))
    words += list(random_key)

    random_value = random.choice(chains[random_key])

    words.append(random_value)

    while True:

        new_bigram = tuple(words[-2:])

        if new_bigram not in chains.keys():
            break

        else:
            words.append(random.choice(chains[new_bigram]))

    words[0] = words[0].title()
    return " ".join(words)

# print(make_text(make_chains(open_and_read_file("green-eggs.txt"))))

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

#!/usr/bin/python3
# Arun Woosaree

# Acknowledgements:

# sorting dictionaries:
# got idea to use lambda function as argument in sorted() from here
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value/2258273#2258273

# stripping punctuation:
# list comprehension
# https://stackoverflow.com/questions/4371231/removing-punctuation-from-python-list-items
# for reference, I do know how to do this, but since I came across this link, and the
# code is somewhat similar, I thought I'd include it here just in case. My syntax was
# slightly off, and this helped me correct it

import sys
import argparse
import curses.ascii  # for detecting punctuation


def parse_args():
    """
    Parses command line arguments using argparse
    """

    parser = argparse.ArgumentParser(
        description='Text frequency analysis',
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--sort",
                        type=str,
                        choices=['byfreq', 'byword'],
                        help="""
        Frequency table sort options:
               byfreq - (default) sort by decreasing frequency.
                        Matching frequency is resolved by word in
                        increasing lexicographical order.

               byword - sort by word in increasing lexicographical order

               """,
                        default='byfreq',
                        # action="store_true",
                        dest="sortby")

    parser.add_argument("--ignore-case",
                        help="ignore upper/lower case when doing all actions\n ",
                        action="store_true",
                        dest="ignorecase")

    parser.add_argument("--remove-punct",
                        help="remove all punctuation characters in a word,\npreserving only the alphanumeric characters\n ",
                        action="store_true",
                        dest="rmpunct")

    parser.add_argument("infile",
                        help="""file to be sorted, stdin if omitted
        Press Enter then Ctrl+D (Linux) or Ctrl+Z (Windows)
        then Enter again to send EOF character.
        The script will then analyze the input text""",
                        nargs="?",
                        type=argparse.FileType('r'),
                        default=sys.stdin)

    return parser.parse_args()


def get_words():
    """
    Reads from a file, or stdin (which is treated like a file with argparse)
    And returns a list of each word
    """
    allwords = []
    for line in args.infile:
        line = line.strip().split()  # remove characters like \n and split lines into words
        for word in line:
            allwords.append(word)

    if(args.ignorecase):
        allwords = [word.lower()
                    for word in allwords]  # lowercase all the words!

    if(args.rmpunct):
        # remove all punctuation
        allwords = [''.join(char for char in word if not curses.ascii.ispunct(
            char)) for word in allwords]

    return allwords


def count_words(allwords):
    """
    Creates a tally of the frequency of words in a list using a python dictionary

    Args:
        allwords: a list of words

    Returns:
        a dictionary of the words in the format:
        word: frequency
    """

    wordict = {}
    for word in allwords:
        if word not in wordict:
            wordict[word] = 1
        elif word in wordict:
            wordict[word] += 1
    return wordict


def print_table(wordict, numwords):
    """
    Prints a frequency table to stdout, given a dictionary of words with their frequency count

    Args:
        wordict: a dictionary of words containing frequency data

        numwords: a tally of all the words, including repeated ones
    """

    if args.sortby == 'byfreq':
        tabledata = sorted(wordict.items(), key=lambda x: x[1])[::-1]
    elif args.sortby == 'byword':
        tabledata = sorted(wordict.items(), key=lambda x: x[0].lower())

    for word, count in tabledata:
        initialspace = ' ' * (20 - len(word))
        # not many words are over 20 characters long, so as long as that holds,
        # the table prints nicely. If words are longer than 20 characters, then
        # the table will still print properly, but not in nice columns, instead
        # there will only be one space separating the word from its count
        print('{0} {1} {2}   {3}'.format(
            word, initialspace, count, round(count / numwords, 2)))


args = parse_args()
words = get_words()
wordict = count_words(words)
print_table(wordict, len(words))

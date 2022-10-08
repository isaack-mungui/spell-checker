#!/usr/bin/python3

from bisect import bisect_left
import file_handle

def binary_search(words_list, word):

    # TODO: Analyze every word in the file using binary search
    # TODO: If word not found in dictionary, print it on the screen as potentially incorrect

    i = bisect_left(words_list, word)
    if i != len(words_list) and words_list[i] == word:
        return i
    else:
        return -1

# call the open_file method from file_handle module
words = file_handle.open_file('dictionary.txt', 'r')

# Prompt for user input
word = str(input("Enter word:"))
res = binary_search(words, word)
if res == -1:
    print(word, "is absent")
else:
    print("First occurrence of", word, "is present at", res)

#!/usr/bin/python3

#  TODO: Prompt for a file to analyze

def open_file(dictionary, file_mode):
    file_object = open(dictionary, file_mode)

    # create a list of words
    words = file_object.read().split()
    file_object.close()

    return words


res = open_file('dictionary.txt', 'r')
print(res)

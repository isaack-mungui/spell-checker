#!/usr/bin/python3
import file_handle

def binary_search(words_list, low, high, word):

    # TODO: Analyze every word in the file using binary search
    # TODO: If word not found in dictionary, print it on the screen as potentially incorrect

    if high >= low:
        mid = (high + low) // 2

        if words_list[mid] == word:
            return mid
        elif words_list[mid] > word:
            return binary_search(words_list, low, mid - 1, word)
        else:
            return binary_search(words_list, mid + 1, high, word)
    else:
        return -1

# call the open_file method from file_handle module
words_list = file_handle.open_file('dictionary.txt', 'r')
word = str(input("Enter word: "))
res = binary_search(words_list, 0, len(words_list) - 1, word)
if res == -1:
    print(word, "is absent")
else:
    print("First occurrence of", word, "is present at index", res)

"""
File: boggle.py
Name: Audrey Tsang
----------------------------------------
This file asks user input 16 alphabets, and search all the anagram for it then print them out.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    This file asks user input 16 alphabets, and search all the anagram for it then print them out.
    """
    boggle = []
    for i in range(4):
        row = input(f"{i + 1} row of letters: ")
        letters = row.split()
        #  If user input doesn't meet the requirements.
        if len(letters) != 4 or not all(letter.isalpha() and len(letter) == 1 for letter in letters):
            print("Illegal input")
            break
        #  Stores input as value and the position of it as key in boggle.
        boggle.append(letters)
    if len(boggle) == 4:
        start = time.time()
        ####################
        anagrams_lst = []
        for x in range(len(boggle[0])):
            for y in range(len(boggle)):
                find_anagrams(boggle, boggle[x][y], [(x, y)], anagrams_lst, read_dictionary(), (x, y))
        print(f'There are {len(anagrams_lst)} words in total.')
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagrams(boggle, new_s, cur_lst, anagrams_lst, dictionary, coordinate):
    """
        :param boggle: (dictionary) A dictionary contains user inputs.
        :param new_s: (str) An empty string stores an anagram.
        :param cur_lst: (lst) An empty list stores indexes of param lst for param new_s.
        :param anagrams_lst: (lst) A list stores all anagrams for param s.
        :param dictionary: (dictionary) A dictionary stores all words in dictionary.txt.
        :param coordinate: (tuple) (x, y) for current coordinate.
        :return: Print out all the new words found one after the other.
    """
    if len(new_s) >= 4:  # Base case
        if new_s not in anagrams_lst and new_s in dictionary:
            print('Found: ' + new_s)
            anagrams_lst.append(new_s)
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            new_x = coordinate[0] + i
            new_y = coordinate[1] + j
            if 0 <= new_x <= 3 and 0 <= new_y <= 3:
                if (new_x, new_y) not in cur_lst:
                    cur_lst.append((new_x, new_y))
                    new_s += boggle[new_x][new_y]
                    if has_prefix(new_s, dictionary):  # Early stopping
                        find_anagrams(boggle, new_s, cur_lst, anagrams_lst, dictionary, (new_x, new_y))
                    #  Un-choose
                    cur_lst.pop()
                    new_s = new_s[:-1]


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python dictionary.
    """
    dictionary = []
    with open(FILE, "r") as f:
        for line in f:
            if len(line.strip()) >= 4:  # Choose the word has more than 4 alphabet.
                dictionary.append(line.strip())
    dictionary = set(dictionary)
    return dictionary


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid.
    :param dictionary: (dictionary) A dictionary contains words in dictionary.txt.
    :return: (bool) If there is any words with prefix stored in sub_s.
    """
    for key in dictionary:
        if key.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

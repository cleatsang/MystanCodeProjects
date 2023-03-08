"""
File: anagram.py
Name: Audrey Tsang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program recursively finds all the anagram(s) for the word input by user
    and terminates when the input string matches the EXIT constant.
    """
    while True:
        print('Welcome to stanCode \"Anagram Generator" (or -1 to quit)')
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:  # Boundary condition.
            break
        else:
            print('Searching...')
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    This function will read dictionary.txt and store all words into a list.
    """
    with open(FILE, 'r') as f:
        dict_lst = [line[:-1] for line in f]
    return dict_lst


def find_anagrams(s):
    """
    :param s: str, the word user input.
    :return: Print out the list of anagram(s).
    """
    anagrams_lst = []   # A list stores all anagrams for param s.
    lst = [i for i in range(len(s))]    # A list stores indexes of alphabets in param s.
    find_anagrams_helper(s, '', lst, [], anagrams_lst, read_dictionary())
    print(str(len(anagrams_lst))+' anagrams: '+str(anagrams_lst))


def find_anagrams_helper(s, new_s, lst, current_lst, anagrams_lst, dictionary):
    """
        :param s: str, the word user input.
        :param new_s: str, an empty string stores an anagram.
        :param lst: lst, a list stores indexes of alphabets in param s.
        :param current_lst: lst, an empty list stores indexes of param lst for param new_s.
        :param anagrams_lst: lst, a list stores all anagrams for param s.
        :param dictionary: lst, a list stores all words in dictionary.txt.
        :return: Print out all the new words found one after the other.
    """
    if has_prefix(new_s, dictionary):   # Early stopping.
        if len(new_s) == len(s):    # Base case!
            #  Avoid double results or results not in dictionary.
            if new_s not in anagrams_lst and new_s in dictionary:
                print('Found: '+new_s)
                print('Searching...')
                anagrams_lst.append(new_s)
        else:
            for num in lst:
                if num in current_lst:  # Check if the same position alphabet already exist
                    pass
                else:
                    #  Choose
                    current_lst.append(num)
                    new_s += s[num]
                    #  Explore
                    find_anagrams_helper(s, new_s, lst, current_lst, anagrams_lst, dictionary)
                    #  Un-choose
                    current_lst.pop()
                    new_s = new_s[:-1]


def has_prefix(sub_s, dict_lst):
    """
    :param sub_s: str, A part of target word to check if it's in the dict_lst.
    :param dict_lst: list, The list of word in dictionary.txt.
    :return: Boolean,  the result of whether this sub_word is in dict_lst.
    """
    for word in dict_lst:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()

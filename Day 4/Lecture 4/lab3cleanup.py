""" CS 5001 - Fall 2023 - Lab 3 - Part 2 - Palindromes

by Steve Shafer
"""
import string


def test_palindrome(test_string):
    """ Test to see if a string is a palindrome and print yes or no

    Return:  True if the string is a palindrome, False if it is not

    Args:
        test_string (string): The string to be tested
    """
    prepared_string = prepare_string(test_string)
    is_it = (prepared_string == prepared_string[::-1])
    return is_it


def prepare_string(test_string):
    """ Prepare string for palindrome test

    Args:
        test_string (string): string to be prepared
    """
    prepared_string = "".join(ch for ch in test_string
                              if ch not in unwanted_characters).lower()
    return prepared_string


candidates = ["Madam, I'm Adam!", "Never even or odd", "Never odd or even",
              "Was it a cat I saw?", "Was it a rat I saw?",
              "A man, a plan, a canal: Suez!",
              "A man, a plan, a canal: Panama!",
              "12/12/1212", "12/12/2121",
              "noon", "midnight"]

unwanted_characters = string.punctuation + string.whitespace

for candidate_string in candidates:
    print(f"{test_palindrome(candidate_string)} - {candidate_string}")

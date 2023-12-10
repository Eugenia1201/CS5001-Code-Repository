""" CS 5001 - Fall 2023 - Lab 3 - Part 2 - Palindromes

by Steve Shafer
"""
import string


def test_palindrome(test_string):
    """ Test to see if a string is a palindrome and print yes or no

    Args:
        test_string (string): The string to be tested
    """
    is_it = "Yes!" if test_string == test_string[::-1] else "No."
    # might be a little bit faster to use slices to compare the first half and
    # second half instead of comparing the whole string and its reverse
    print(f"{is_it}  {test_string}")


candidates = ["Madam, I'm Adam!", "Never even or odd", "Never odd or even",
              "Was it a cat I saw?", "Was it a rat I saw?",
              "A man, a plan, a canal: Suez!",
              "A man, a plan, a canal: Panama!",
              "12/12/1212", "12/12/2121",
              "noon", "midnight"]
print(candidates)

unwanted_characters = string.punctuation + string.whitespace
prepared_strings = []
for candidate_string in candidates:
    prepared_string = "".join(ch for ch in candidate_string
                              if ch not in unwanted_characters).lower()
    prepared_strings.append(prepared_string)
print()
print(prepared_strings)
print()

for prepared_string in prepared_strings:
    test_palindrome(prepared_string)

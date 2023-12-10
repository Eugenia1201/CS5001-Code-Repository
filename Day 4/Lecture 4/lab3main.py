""" CS 5001 - Fall 2023 - Lab 3 - Part 2 - Palindromes

by Steve Shafer
"""

import lab3module


if __name__ == "__main__":

    candidates = ["Madam, I'm Adam!", "Never even or odd", "Never odd or even",
                "Was it a cat I saw?", "Was it a rat I saw?",
                "A man, a plan, a canal: Suez!",
                "A man, a plan, a canal: Panama!",
                "12/12/1212", "12/12/2121",
                "noon", "midnight"]


    for candidate_string in candidates:
        print(f"{lab3module.test_palindrome(candidate_string)} - {candidate_string}")

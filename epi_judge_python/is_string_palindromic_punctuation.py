from test_framework import generic_test
import string

# My solution, O(n^2)T
def is_palindrome(s: str) -> bool:
    low, high = 0, len(s) - 1
    alphanumeric_characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    while low < high:
        if s[low] not in alphanumeric_characters:
            low += 1
            continue
        if s[high] not in alphanumeric_characters:
            high -= 1
            continue
        if (s[low].lower() != s[high].lower()):
            return False
        low, high = low + 1, high - 1
    return True

# EPI Solution O(n)T
def is_palindrome(s: str) -> bool:
    low, high = 0, len(s) - 1
    while low < high:
        while not s[low].isalnum() and low < high:
            low += 1
        while not s[high].isalnum() and low < high:
            high -= 1
        if (s[low].lower() != s[high].lower()):
            return False
        low, high = low + 1, high - 1
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
from inspect import currentframe
from unittest import result
from test_framework import generic_test

# My solution
def look_and_say(n: int) -> str:
    def compute_nth_element(previous: str):
        i = 0
        current_digit = previous[i]
        result = ""
        while True:
            count = 0
            while i < len(previous) and previous[i] == current_digit:
                count += 1
                i += 1
            result += str(count) + current_digit
            if i == len(previous):
                break
            else:
                current_digit = previous[i]
        return result

    result = "1"
    for _ in range(1, n):
        result = compute_nth_element(result)
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))

from test_framework import generic_test
import functools

# My solution
def roman_to_integer(s: str) -> int:
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    sum = i = 0
    while i < len(s) - 1:
        current_value = map[s[i]]
        next_value = map[s[i+1]]
        
        if next_value > current_value:
            sum += next_value - current_value
            i += 2
        else:
            sum += map[s[i]]
            i += 1
    if i == len(s) - 1:
        sum += map[s[-1]]
    return sum

def roman_to_integer(s: str) -> int:
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(
        lambda count, i: count + (-map[s[i]] if map[s[i]] < map[s[i+1]] else map[s[i]]),
        reversed(range(len(s) - 1)), map[s[-1]]
    )
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))

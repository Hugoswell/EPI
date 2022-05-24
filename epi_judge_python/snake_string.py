from test_framework import generic_test

# My solution O(n^2)T O(n)S
def snake_string(s: str) -> str:
    positions = [0,1] + [0] * (len(s) - 2)
    result = ""

    for i in range(2, len(s)):
        if (positions[i-2] == 0 and positions[i-1] == 1) or (positions[i-2] == 0 and positions[i-1] == -1):
            positions[i] = 0
        elif positions[i-2] == 1 and positions[i-1] == 0:
            positions[i] = -1
        else:
            positions[i] = 1

    for i in range(len(s)):
        if positions[i] == 1:
            result += s[i]
    for i in range(len(s)):
        if positions[i] == 0:
            result += s[i]
    for i in range(len(s)):
        if positions[i] == -1:
            result += s[i]

    return result

# EPI solution
# def snake_string(s: str) -> str:
#     result = []
#     for i in range(1, len(s), 4):
#         result.append(s[i])
#     for i in range(0, len(s), 2):
#         result.append(s[i])
#     for i in range(3, len(s), 4):
#         result.append(s[i])
#     return ''.join(result)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))

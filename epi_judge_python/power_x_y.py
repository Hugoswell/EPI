from test_framework import generic_test

# O(y)T, O(1)S Brute force
def power(x: float, y: int) -> float:
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res if y < 0 else res

# O(Log(y))T, O(1)S Iterative version
def power(x: float, y: int) -> float:
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power % 2:
            result *= x
        x, power = x * x, power // 2
    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))

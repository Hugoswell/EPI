from test_framework import generic_test


def power(x: float, y: int) -> float:
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res if y < 0 else res

#does not work with y negative
# def power(x: float, y: int) -> float:
#     if y == 1:
#         return x
#     res = x * power(x, y - 1)
#     return 1 / res if y < 0 else res

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
    #  print(power(2.54654, 3))

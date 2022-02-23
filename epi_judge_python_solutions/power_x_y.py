from test_framework import generic_test

# Iterative version
# def power(x: float, y: int) -> float:
#     result, power = 1.0, y
#     if y < 0:
#         power, x = -power, 1.0 / x
#     while power:
#         if power & 1:
#             result *= x
#         x, power = x * x, power >> 1
#     return result

# Recursive version
def power(x: float, y: int) -> float:
    def helper(x, y):
        if x == 0: return 0
        if y == 0: return 1
        
        res = helper(x * x, y // 2)
        return x * res if y % 2 else res

    res = helper(x, abs(y))
    return res if y >= 0 else 1 / res
    
if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))

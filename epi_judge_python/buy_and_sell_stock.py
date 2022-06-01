from typing import List

from test_framework import generic_test

# EPI solution O(n)T, O(1)S
def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_value_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        min_value_so_far = min(min_value_so_far, price)
        max_profit = max(max_profit, price - min_value_so_far)
    return max_profit

# My solution O(n)T, O(1)S
def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_diff, min_idx = 0.0, 0
    for i in range(1, len(prices)):
        max_diff = max(prices[i] - prices[min_idx], max_diff)
        if prices[i] < prices[min_idx]:
                min_idx = i
    return max_diff

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
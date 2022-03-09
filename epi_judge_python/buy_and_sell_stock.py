from typing import List

from test_framework import generic_test


# def buy_and_sell_stock_once(prices: List[float]) -> float:
#     max_profit = 0.0
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             current_profit = prices[j] - prices[i]
#             if current_profit > max_profit:
#                 max_profit = current_profit
#     return max_profit

def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_value_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        min_value_so_far = min(min_value_so_far, price)
        max_profit = max(max_profit, price - min_value_so_far)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
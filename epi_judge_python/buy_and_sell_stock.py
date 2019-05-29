from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    max_return_ever = float('-inf')
    for i,v in enumerate(prices):
        for j in prices[i:]:
            max_return_ever = max(max_return_ever, j-v)
    return max_return_ever if max_return_ever>0 else 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))

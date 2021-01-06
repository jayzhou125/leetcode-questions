def findProfit(numSuppliers: int, inventory: List[int], order: int) -> int:
    from collections import Counter
    from itertools import accumulate
    def seq_sum(start: int, stop: int) -> int:
        return (start + stop - 1) * (stop - start) // 2
    count = sorted(Counter(inventory).items(), reverse=True)
    stocks = [c[0] for c in count] + [0]
    suppliers = list(accumulate(c[1] for c in count))
    profit = 0
    left = order
    for stock, next_stock, sups in zip(stocks, stocks[1:], suppliers):
        supply = sups * (stock - next_stock)
        full, part = divmod(min(left, supply), sups)
        profit += sups * seq_sum(stock - full + 1, stock + 1) \
            + part * (stock - full)
        left -= supply
        if left <= 0:
            return profit

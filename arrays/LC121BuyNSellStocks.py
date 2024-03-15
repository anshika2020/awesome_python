from typing import List


class BuyNSellStocksLC121:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    stock = BuyNSellStocksLC121()
    prices = [7, 1, 5, 3, 6, 4]
    print(stock.maxProfit(prices)) # output is 5

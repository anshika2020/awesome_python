# 122. Best Time to Buy and Sell Stock II
'''
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''
from typing import List


class BuyNSellStocksII:
    def buyandSellSttocks(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                profit += prices[i]-prices[i - 1]
        return profit


if __name__ == "__main__":
    price = [7, 1, 5, 3, 6, 4]  # output should be 7
    stocks = BuyNSellStocksII()
print(stocks.buyandSellSttocks(price))

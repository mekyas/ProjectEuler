from typing import List

def maxProfit(prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        # max profit from 0 to k
        min_price = prices[0]
        max_profit1 = [0]
        for i in range(1, len(prices)):
            max_profit1.append(max(prices[i]-min_price, max_profit1[-1]))
            if prices[i]<min_price:
                min_price = prices[i]
        
        # max profit from k to n
        max_price = prices[-1]
        max_profit2 = [0]
        for i in range(len(prices)-2, -1, -1):
            max_profit2.insert(0, max(max_price-prices[i], max_profit2[0]))
            if prices[i]>max_price:
                max_price = prices[i]
        ans = 0
        print(max_profit1, max_profit2)
        for p1, p2 in zip(max_profit1, max_profit2):
            ans = max(ans, p1+p2)
        return ans

print(maxProfit([6,1,3,2,4,7]))
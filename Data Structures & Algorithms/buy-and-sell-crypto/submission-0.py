class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Ground truth: no profit can be made if there are fewer than 2 days
        if not prices or len(prices) < 2:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            # Update the cheapest day to buy found so far
            if price < min_price:
                min_price = price
            # Check if selling today beats our previous maximum profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

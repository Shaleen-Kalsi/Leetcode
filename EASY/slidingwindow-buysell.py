class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy, sell = 0, 1
        maxProfit = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > maxProfit:
                    maxProfit = profit
            else:
                buy = sell
                
            sell+=1
            
        return maxProfit
        
'''
你可以在买入的时候交这个手续费
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        if not prices:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0] -fee

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]-fee)
        
        return dp[-1][0]
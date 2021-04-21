'''
状态定义：
状态一：cash in hand after selling 卖出股票后， 钱在手的状态
状态二：stock in hand ：股票在手，即花钱买了股票的状态
状态三：freeze 冷冻期， 即卖出股票当天的状态，我们将其定义为冷冻期， 冷冻期导致后一天的钱在手的状态只能是跟冷冻期时一样

初始化：
状态一：第一天不可能钱在手， 没有股票可买， 初始化为0
状态二：股票在手， 初始化为-prices[i]， 即花了prices[i]的价格买入股票
状态三：不存在前一天， 即也不存在前一天卖掉股票， 初始化为0

状态转换：
状态一：钱在手， 可能前一天钱就在手， 今天不做任何操作。也可以由状态三转化而来

状态二：股票在手， 可能钱一天股票在手， 今天不做任何操作。 也可能由昨天的状态一今天买入股票
状态三：冷冻期， 即卖了前一天的股票， 即由状态二股票在手卖出股票
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0,0,0] for _ in range(len(prices))]

        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]
        
        return max(dp[-1][0], dp[-1][2])
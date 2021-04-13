```
### dp思想
对于一个长度为n的绳子， 我们将其分为m份， n,m均为整数， 且m>1，即至少分成两份
那么对于长度为0和1的绳子就不存在切分方法
对于长度为2的绳子我们可以切分为1和1， 乘积最大为1
用一个数组dp记录从0到n长度的绳子切分后的最大乘积， 则dp[0] = 0, dp[1] = 0, dp[2] = 1
我们先把绳子剪掉一段， 假设长度为j(j>=1, j<n), 那么剩下的绳子长度为(n-j), 如果剩下的绳子不需要剪， 则乘积为(n-j)*j, 如果剩下的绳子需要剪辑
则(n-j)的绳子剪辑的最大乘积为dp[n-j]， 即j*(dp[n-j])， 那么我在(j>=1, j<n)的循环里去寻求最大值
最后返回dp[n]或dp[-1]即可
```


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[2] = 1

        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
        
        return dp[-1]
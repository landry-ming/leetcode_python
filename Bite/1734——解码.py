"""给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。
它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。
给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。

思路：
1. 假设我们知道原始数组第一个数x0， 那么第二个数就是x0 ^ encoded[0], 第三个数就是x1 ^ encoded[1], 依次类推
2. 那么问题就来到了我们怎么求出第一个数， 由于该整数数组是前n个数的排列， 则perm[0]到perm[n-1]的异或结果可以通过求出
3. 那么怎么求出perm[1]到perm[n-1]的异或结果呢， 即由于其为奇数数组，则encoded[1]^encoded[3]^encoded[5]即为perm[1], perm[2]到perm[n-1] 

"""
class Solution:
    from functools import reduce
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1   ### perm数组的长度为encoded的长度+1
        total = reduce(xor, range(1, n+1)) ### 由于perm数组是前n个数， 用reduce函数求解其疑惑
        odd = 0
        for i in range(1, n-1, 2):
            odd ^= encoded[i]   ### 这里求得是perm数组除了第一个数的异或
        perm = [total ^ odd]
        for i in range(n-1):
            perm.append(perm[-1] ^ encoded[i])
        return perm

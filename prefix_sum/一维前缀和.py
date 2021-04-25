#### 区域和检索-数组不可变
'''
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

时间复杂度：初始化O(n)，每次检索O(1),其中n是数组nums的长度。
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sum = self.sums

        for num in nums:
            _sum.append(_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        _sum = self.sums
        return _sum[right+1] - _sum[left]
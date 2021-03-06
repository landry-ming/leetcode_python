"""
二分查找 但是注意边界位置
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        if nums[-1] < target:
            return len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1 
            else:
                right = mid
        
        return left
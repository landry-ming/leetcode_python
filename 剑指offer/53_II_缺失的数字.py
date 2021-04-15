class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count == mid + 1:
                left = mid + 1
            else:
                right = mid
        return left
                
        
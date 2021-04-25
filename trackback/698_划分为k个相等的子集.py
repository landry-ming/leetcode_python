class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, res = divmod(sum(nums), k)
        if res:return False

        def search(groups):
            if not nums:
                return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups):
                        return True
                    groups[i] -= v
                if not group:
                    break     ### 如果这个group是0加这个数都不行， 那么后面的估计也不行， 故直接break。
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target:
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return search([0] * k)                
def canPartitionKSubsets(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem: return False

    def search(groups):
        if not nums: return True
        v = nums.pop()
        for i, group in enumerate(groups):
            if group + v <= target:
                groups[i] += v
                if search(groups): return True
                groups[i] -= v
            if not group: break
        nums.append(v)
        return False

    nums.sort()
    if nums[-1] > target: return False
    while nums and nums[-1] == target:
        nums.pop()
        k -= 1

    return search([0] * k)

nums = [10,10,10,7,7,7,7,7,7,6,6,6]
k = 3
a = canPartitionKSubsets(nums, k)
print(a)

```
穷举法
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        inv_count = 0
        inv_list = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] >  nums[j]:
                    inv_count += 1
                    inv_list.append([nums[i], nums[j]])
        return inv_list, inv_count

```

```
分治
利用归并排序中的并， 归并排序并的时候分为左右列表， 分别指定左右两个指针， 当左指针指向的数值小于右指针指向的数值时， 这时注意， 右指针移动了多少位置，则说明有多少数
小于左指针位置的数， 即可以更新inv_count

这里注意的是， 在每次并之后， 一定要更新列表，保证左右列表都是排序完成的。
```
class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort(nums, l, r, temp):
            if l >= r:
                return 0

            mid = (l + r) // 2
            inv_count = merge_sort(nums, l, mid, temp) + merge_sort(nums, mid+1, r, temp)
            left_index = l
            right_index = mid+1
            pos = l

            while left_index <= mid and right_index  <= r:
                if nums[left_index] <= nums[right_index]:
                    inv_count += right_index - (mid+1)
                    temp[pos] = nums[left_index] 
                    left_index += 1
                else:
                    temp[pos] = nums[right_index]
                    right_index += 1
                pos += 1
            for k in range(left_index, mid+1):
                inv_count += (right_index - (mid+1))
                temp[pos] = nums[k]
                pos += 1
            for k in range(right_index, r+1):
                temp[pos] = nums[k]
                pos += 1
            nums[l:r+1] = temp[l:r+1]
            return inv_count
        
        l = 0
        r = len(nums) - 1
        temp = [0 for _ in range(len(nums))]
        return merge_sort(nums, l, r, temp)















```
归并排序的思路
```
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    left_index = 0
    right_index = 0
    res = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1
    res += left[left_index:]
    res += right_index[right_index:]
    return res





    
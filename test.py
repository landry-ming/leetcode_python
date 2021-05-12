def smallestK(arr, k):
    def helper(arr, start, end):
        if start >= end:
            return 
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            if arr[left] > arr[pivot] and arr[right] <= arr[pivot]:
                arr[left], arr[right] = arr[right], arr[left]
            if arr[left] <= arr[pivot]:
                left += 1
            if arr[right] > arr[pivot]:
                right -= 1
        arr[pivot], arr[right] = arr[right], arr[pivot]
        if right == k-1:
            return arr
        if right > k-1:
            return helper(arr, start, right-1)
        if right < k-1:
            return helper(arr, right+1, end)
    helper(arr, 0, len(arr)-1)
    return arr[:k]

arr = [1,3,5,7,2,4,6,8]
k = 4
smallestK(arr, k)
class Solution:
    def minArray(self, numbers: List[int]) -> int:

        left = 0
        right = len(numbers) - 1

        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                right = right - 1
            else:
                right = mid
        return numbers[left]
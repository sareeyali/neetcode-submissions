class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        idx = []

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                idx.append(left + 1)
                idx.append(right + 1)
                return idx
            if sum < target:
                left += 1
            else:
                right -= 1


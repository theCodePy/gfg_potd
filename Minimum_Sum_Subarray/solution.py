# kadane's  algorithm
class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        current_min = float('inf')
        ans = float('inf')

        for num in arr:
            if current_min > 0:
                current_min = num
            else:
                current_min += num

            ans = min(ans, current_min)
        return ans




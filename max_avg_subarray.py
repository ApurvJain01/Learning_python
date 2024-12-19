class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        max_sum = 0.0
        i = 0
        j = 0 
        for i in range(n-k+1): 
            curr_sum = 0.0
            for j in range(k):
                curr_sum = float(curr_sum + nums[i + j])
            max_sum = max(curr_sum, max_sum)
            if n == 1 and nums[i] < 0:
                return nums[i]
        max_avg = float(max_sum / k )
        return max_avg
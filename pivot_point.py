class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0  # initializing the left sum to 0 
        pivot = 0 # setting the pivot to 0 
        right = sum(nums[1:])  # iniital right sum is sum of all the elements apart from index 0 

      # running the loop till array length and left sum != right sum
        while pivot < (len(nums) - 1) and left != right: 
            pivot += 1 
            right -= nums[pivot]
            left += nums[pivot - 1]

        return pivot   if left == right else -1

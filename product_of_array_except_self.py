'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums) -1
        answer = []
        for i in nums:
            if nums[i] == 0:
                answer[i] = 0
            if i == 0:
                answer[i] = num[i+1] * num [j]
                i += 1 
                j -= 1
            if i > 0 and nums[i] != 0: 
                answer[i] = nums[i-1] * nums[i+1] * nums[j]
                i += 1
                j -= 1
            answer.append(answer[i])
        return answer

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # We initialize 2 pointers for our sliding window
        l = 0  # left pointer
        r = 0  # right pointer
        
        # for loop for iterating on right 
        
        for r in range(len(nums)):
            # checking if the value at right is 0 then we reduce the count of number of zeros by 1 
            if nums[r] == 0:
                k -= 1
            # if value of k is negetive then we will have to add one to it. We cannot have negetive values of k which is zero
            if k < 0: 
                # if num at l index is zero then we increase the number of k by 1 
                if nums[l] == 0:
                    k += 1 
                # increasing the left pointer
                l+=1
                
        # finally returning the window of max consecutive 1
        return r-l+1
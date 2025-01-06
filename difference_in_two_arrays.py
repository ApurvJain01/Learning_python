class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # Here we are creating 2 hashsets for the input arrays. This will help us do the operations faster
        
        h1 = set(nums1)
        h2 = set(nums2)

        # iterating over the nums2 and checking if the nums2 
        for i in nums2:
            if i in h1: 
                # if the element in h2 at ith index present in h1 then remove the element from H1
                h1.remove(i)
                # gracefully removing the element from H2 also
                h2.discard(i)
        
        # returning the list as expected in the output
        return [list(h1), list(h2)]

class Solution:
    '''
    here we are creating a new string merged. 
    We will be checking the length of each word. and we start a pointer from 0 and once we traverse the strings 
    '''
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i = 0
        # min_len = min(len(word1), len(word2))
        while i <= len(word1) or i <= len(word2):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
            i += 1
        return merged
            



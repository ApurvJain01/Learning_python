'''
Reverse Vowels of a string
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        # Creating a list of the string we are getting in the input
        word = list(s)
        # Starting a pointer from start of the string
        i = 0
        # starting a pointer from last of the string
        j = len(s) - 1
        
        while i < j:
            while i < j and vowels.find(word[i]) == -1:
                i += 1
            while i < j and vowels.find(word[j]) == -1:
                j -= 1
            word[i], word[j] = word[j], word[i]

            i += 1
            j -= 1

        return ''.join(word)

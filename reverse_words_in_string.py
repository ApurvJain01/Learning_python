class Solution:
    def reverseWords(self, s: str) -> str:
        # for i in range(len(s)):

        split_s = s.split()
        rev_list = split_s[::-1]
        return ' '.join(rev_list)
      
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip()
        counter = 0 
        i = len(s) - 1

        while i >= 0 and s[i] != ' ':
            counter += 1
            i -= 1
        return counter



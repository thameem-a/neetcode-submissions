class Solution:
    def maxDifference(self, s: str) -> int:
        
        seen = {}

        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1

            #  get largest odd value
            a1 = max((val for val in seen.values() if val % 2 != 0), default=None)
            # get largest even value
            a2 = min((val for val in seen.values() if val % 2 == 0), default=None)
   
        return a1 - a2
                
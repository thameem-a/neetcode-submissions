class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # break up the first word
        common = list(words[0])

        # start loop from second word
        for word in words[1:]:
            temp = []
            # loop through letters 
            for ch in common:
                if ch in word:
                    temp.append(ch)
                    word = word.replace(ch, "", 1)
            common = temp

        return common
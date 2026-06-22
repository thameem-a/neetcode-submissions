class Solution:

    def encode(self, strs: List[str]) -> str:
        rslt = ""
        for s in strs:
            rslt += str(len(s)) + "#" + s
        return rslt

    def decode(self, s: str) -> List[str]:
        rslt = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            rslt.append(word)
            i = j +1 + length
        return rslt

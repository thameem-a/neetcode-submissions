class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []
        total = 0

        for op in operations:
            # if "+" add the last two elements in the array and append it to score
            if op == "+":
                score.append(int(score[-1]) + int(score[-2]))
            # if "c" pop the last emlement in the score
            elif op == "C":
                score.pop()
            # if "d" double the the last score
            elif op == "D":
                score.append(int(score[-1] * 2))
            # anything else add it to the score
            else:
                score.append(int(op))
        
        # calc total
        for scores in score:
            total += scores
        
        return total
        



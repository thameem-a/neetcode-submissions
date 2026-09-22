class Solution:
    def countSeniors(self, details: List[str]) -> int:

        counter = 0



        # we know string length is 15, age is after gender so age is 11:13 index
        for strings in details:
            age = strings[11:13]
            # > 60 add 1 to counter
            if age > "60":
                counter += 1
        return counter
        
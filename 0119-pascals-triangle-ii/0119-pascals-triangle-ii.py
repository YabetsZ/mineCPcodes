class Solution:
    def getRow(self, row: int) -> List[int]:
        result = []
        factorial = [1]
        for i in range(1,34):
            factorial.append(i* factorial[-1])
        for i in range(row+1):
            val = factorial[row]/(factorial[row-i]*factorial[i])
            result.append(int(val))

        return result
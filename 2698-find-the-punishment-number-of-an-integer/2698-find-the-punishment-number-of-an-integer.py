class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check_for_i(i, sqri, summed):
            if sqri == 0 and summed == i:
                return True
            elif sqri == 0:
                return False
            
            for p in range(len(str(sqri))):
                chopped = sqri//10**p
                summed +=  chopped 
            
                if check_for_i(i, sqri%10**p, summed):
                    return True
                summed -= chopped
            return False
        result = 0
        for i in range(1, n+1):
            if check_for_i(i, i**2, 0):
                print(i**2)
                result += i**2
        return result
class Solution:
    def kthCharacter(self, k: int) -> str:
        def generate(arr):
            if len(arr) >= k:
                return arr[k-1]
            for i in range(len(arr)):
                num = arr[i]
                arr.append((num+1)%26)
            return generate(arr)
        
        return chr(generate([0]) + ord("a"))
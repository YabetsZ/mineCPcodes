class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        table = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    table[i][j] = nums[i]
                else:
                    table[i][j] = max(nums[i] - table[i+1][j], nums[j] - table[i][j-1])
        # table[i][j] == 0 means if they play optimally they will have equal score and if table[i][j] > 0 if the current player pick optimally he is the winner from that subarray onwards
        return table[0][n-1] >= 0 # since player one starts first! wooow!


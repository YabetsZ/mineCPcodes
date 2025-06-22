class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        left, right, upper, lower = (0, -1), (0, 1), (-1, 0), (1, 0)
        street = {
            1: (left, right),
            2: (upper, lower),
            3: (left, lower),
            4: (right, lower),
            5: (left, upper),
            6: (right, upper),
        }

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        def is_valid(ci, cj, pi, pj):
            st_type = grid[ci][cj]
            if (pi - ci, pj - cj) not in street[st_type]:
                return False
            if (ci, cj) == (n - 1, m - 1):
                return True

            (ui, uj), (vi, vj) = street[st_type]
            ni, nj = None, None
            if (ci + ui, cj + uj) == (pi, pj):
                ni, nj = ci + vi, cj + vj
            else:
                ni, nj = ci + ui, cj + uj
            if inbound(ni, nj):
                return is_valid(ni, nj, ci, cj)
            return False

        result = False
        (ui, uj), (vi, vj) = street[grid[0][0]]
        if inbound(ui, uj):
            result |= is_valid(ui, uj, 0, 0)
        if not result and inbound(vi, vj):
            result |= is_valid(vi, vj, 0, 0)

        return True if n == m == 1 else result

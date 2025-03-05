# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)
        for money in bills:
            if money == 20:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
            elif money == 10:
                if changes[5] >= 1:
                    changes[5] -= 1
                else:
                    return False
            changes[money] += 1
        return True

                
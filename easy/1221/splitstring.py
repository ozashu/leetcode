class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        resutlt = 0
        for e in s:
            if e == 'R':
                r += 1
            if e == 'L':
                r -= 1

            if r == 0:
                result += 1
        return result

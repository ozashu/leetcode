class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                i += 1
            else:
                num -= 1
                i += 1
        return i


if __name__ == '__main__':
    ns = Solution()
    print(ns.numberOfSteps(14))
    print(ns.numberOfSteps(8))
    print(ns.numberOfSteps(123))

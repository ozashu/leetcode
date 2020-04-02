class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ignoresingle = [x for x in set(nums) if nums.count(x) > 1]
        result = list(set(nums.copy()))
        for i in ignoresingle:
            if i in result:
                result.remove(i)

        return result[0]


if __name__ == '__main__':
    sl = Solution()
    print(sl.singleNumber([2, 2, 1]))

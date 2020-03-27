class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        return [sorted(nums).index(i) for i in nums]


if __name__ == '__main__':
    sl = Solution()
    print(sl.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))

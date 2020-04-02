class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ignoresingle = [x for x in set(nums) if nums.count(x) > 1]
        result = list(set(nums.copy()))
        for i in ignoresingle:
            if i in result:
                result.remove(i)

        return result[0]

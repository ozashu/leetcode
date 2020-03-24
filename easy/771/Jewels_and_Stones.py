class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(j) for j in J)


if __name__ == '__main__':
    sl = Solution()
    print(sl.numJewelsInStones("aA", "aAAbbbb"))
    print(sl.numJewelsInStones("z", "ZZ"))

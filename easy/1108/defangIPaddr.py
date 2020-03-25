class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))


if __name__ == '__main__':
    sl = Solution()
    print(sl.defangIPaddr('1.1.1.1'))

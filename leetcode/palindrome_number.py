class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x % 10 == 0 and x != 0:
            return False
        remainder = 0
        while x > remainder:
            remainder = remainder * 10 + x % 10
            x = x // 10
        return x == remainder or x == remainder // 10
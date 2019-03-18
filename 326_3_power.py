class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #执行用时 : 384 ms, 在Power of Three的Python提交中击败了0.86% 的用户
        #内存消耗 : 10.9 MB, 在Power of Three的Python提交中击败了0.00% 的用户
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

        #执行用时 : 284 ms, 在Power of Three的Python提交中击败了2.41% 的用户
        #内存消耗 : 10.8 MB, 在Power of Three的Python提交中击败了0.00% 的用户
        if n < 1:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        return False

        #执行用时 : 284 ms, 在Power of Three的Python提交中击败了2.41% 的用户
        #内存消耗 : 10.7 MB, 在Power of Three的Python提交中击败了0.00% 的用户
        if n <= 0:
            return False
        max_num = 1162261467
        return max_num % n == 0

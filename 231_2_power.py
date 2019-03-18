class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #执行用时 : 48 ms, 在Power of Two的Python提交中击败了3.54% 的用户
        #内存消耗 : 10.7 MB, 在Power of Two的Python提交中击败了0.00% 的用户
        if n < 1:
            return False
        return (n & (n - 1) == 0)

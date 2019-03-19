class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #执行用时 : 36 ms, 在Binary Number with Alternating Bits的Python提交中击败了6.99% 的用户
        #内存消耗 : 10.9 MB, 在Binary Number with Alternating Bits的Python提交中击败了0.00% 的用户
        d = n & 1
        while (n & 1 == d):
            d ^= 1
            n = n >> 1
        return n == 0

        #执行用时 : 24 ms, 在Binary Number with Alternating Bits的Python提交中击败了100.00% 的用户
        #内存消耗 : 10.6 MB, 在Binary Number with Alternating Bits的Python提交中击败了0.00% 的用户
        t = n + (n >> 1)
        return (t + 1) & t == 0

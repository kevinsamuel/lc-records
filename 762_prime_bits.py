class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        #执行用时 : 268 ms, 在Prime Number of Set Bits in Binary Representation的Python提交中击败了77.70% 的用户
        #内存消耗 : 10.8 MB, 在Prime Number of Set Bits in Binary Representation的Python提交中击败了0.00% 的用户
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        res = 0
        i = L
        while i <= R:
            num = bin(i).count('1')
            i += 1
            if num in primes:
                res += 1
        return res

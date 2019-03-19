class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #执行用时 : 36 ms, 在Hamming Distance的Python提交中击败了8.99% 的用户
        #内存消耗 : 10.9 MB, 在Hamming Distance的Python提交中击败了0.00% 的用户
        return bin(x ^ y).count('1')

        执行用时 : 36 ms, 在Hamming Distance的Python提交中击败了8.99% 的用户
        #内存消耗 : 10.7 MB, 在Hamming Distance的Python提交中击败了0.00% 的用户
        val = x ^ y
        num = 0
        while val:
            num += 1
            val &= val - 1
        return num

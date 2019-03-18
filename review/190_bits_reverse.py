class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #执行用时 : 28 ms, 在Reverse Bits的Python提交中击败了95.92% 的用户
        #内存消耗 : 10.7 MB, 在Reverse Bits的Python提交中击败了0.67% 的用户
        return int(bin(n)[2:].zfill(32)[::-1], 2)

        #执行用时 : 40 ms, 在Reverse Bits的Python提交中击败了9.89% 的用户
        #内存消耗 : 10.7 MB, 在Reverse Bits的Python提交中击败了0.67% 的用户
        res = 0
        for _ in range(32):
            res = (res << 1) + n % 2
            n >>= 1
        return res

        #执行用时 : 44 ms, 在Reverse Bits的Python提交中击败了5.72% 的用户
        #内存消耗 : 10.8 MB, 在Reverse Bits的Python提交中击败了0.67% 的用户
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

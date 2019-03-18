class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #执行用时 : 40 ms, 在Number of 1 Bits的Python提交中击败了5.65% 的用户
        #内存消耗 : 10.8 MB, 在Number of 1 Bits的Python提交中击败了0.47% 的用户
        return (str(bin(n))[2:]).count('1')

        #执行用时 : 28 ms, 在Number of 1 Bits的Python提交中击败了92.82% 的用户
        #内存消耗 : 10.9 MB, 在Number of 1 Bits的Python提交中击败了0.47% 的用户
        return bin(n).count('1')

        #执行用时 : 32 ms, 在Number of 1 Bits的Python提交中击败了19.34% 的用户
        #内存消耗 : 10.8 MB, 在Number of 1 Bits的Python提交中击败了0.47% 的用户
        count = 0
        while n:
            if n %2:
                count += 1
            n = n / 2
        return count

        #执行用时 : 40 ms, 在Number of 1 Bits的Python提交中击败了5.65% 的用户
        #内存消耗 : 11 MB, 在Number of 1 Bits的Python提交中击败了0.47% 的用户
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count

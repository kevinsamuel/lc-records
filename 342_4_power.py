class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #执行用时 : 52 ms, 在Power of Four的Python提交中击败了1.52% 的用户
        #内存消耗 : 10.8 MB, 在Power of Four的Python提交中击败了0.00% 的用户
        if num < 1:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1

        #执行用时 : 52 ms, 在Power of Four的Python提交中击败了1.52% 的用户
        #内存消耗 : 10.7 MB, 在Power of Four的Python提交中击败了0.00% 的用户
        if num < 1:
            return False
        if num == 1:
            return True
        if num % 4 == 0:
            return self.isPowerOfFour(num / 4)
        return False

        #执行用时 : 36 ms, 在Power of Four的Python提交中击败了13.41% 的用户
        #内存消耗 : 10.8 MB, 在Power of Four的Python提交中击败了0.00% 的用户
        return num > 0 and num & (num-1) == 0 and len(bin(num)[3:]) % 2 == 0

        #执行用时 : 36 ms, 在Power of Four的Python提交中击败了13.41% 的用户
        #内存消耗 : 10.8 MB, 在Power of Four的Python提交中击败了0.00% 的用户
        return num & (num-1) == 0 and num % 3 == 1

        #执行用时 : 56 ms, 在Power of Four的Python提交中击败了1.22% 的用户
        #内存消耗 : 10.7 MB, 在Power of Four的Python提交中击败了0.00% 的用户
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 == num

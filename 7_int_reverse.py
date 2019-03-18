class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
#        执行用时 : 36 ms, 在Reverse Integer的Python提交中击败了93.45% 的用户
#        内存消耗 : 10.7 MB, 在Reverse Integer的Python提交中击败了2.37% 的用户
#        num_str = str(x)
#        if num_str[0] == '-':
#            is_negative = True
#            l = list(num_str[1:])
#        else:
#            is_negative = False
#            l = list(num_str)
#        l.reverse()
#        res_num_str = "".join(l)
#        if is_negative:
#            res_num_str = '-' + res_num_str
#        res_num = int(res_num_str)
##        执行用时 : 48 ms, 在Reverse Integer的Python提交中击败了9.72% 的用户
##        内存消耗 : 11 MB, 在Reverse Integer的Python提交中击败了2.37% 的用户
##        若下面的2**31更换成计算出的实际值，则结果如上~
#        if res_num > 2**31 -1 or res_num < -2**31:
#            res_num = 0
#        print res_num

#        执行用时 : 56 ms, 在Reverse Integer的Python提交中击败了4.92% 的用户
#        内存消耗 : 10.6 MB, 在Reverse Integer的Python提交中击败了2.37% 的用户
#        mark = 1 if x > 0 else -1
#        num = abs(x)
#        res = mark * (int(str(num)[::-1]))
#        return res if -2**31 <= res < 2**31 else 0

#        执行用时 : 36 ms, 在Reverse Integer的Python提交中击败了93.45% 的用户
#        内存消耗 : 10.7 MB, 在Reverse Integer的Python提交中击败了2.37% 的用户
#        x = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
#        x = 0 if abs(x) > 0x7FFFFFFF else x
#        return x

#        执行用时 : 36 ms, 在Reverse Integer的Python提交中击败了93.45% 的用户
#        内存消耗 : 10.9 MB, 在Reverse Integer的Python提交中击败了2.37% 的用户
#        if x < 0:
#            return -self.reverse(-x)
#        res = 0
#        while x:
#            res = res * 10 + x % 10
#            x /= 10
#        return res if res <= 0x7fffffff else 0

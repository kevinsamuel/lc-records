class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        #执行用时 : 24 ms, 在Convert a Number to Hexadecimal的Python提交中击败了98.48% 的用户
        #内存消耗 : 10.8 MB, 在Convert a Number to Hexadecimal的Python提交中击败了0.00% 的用户
        if not num:
            return '0'
        hex_str = "0123456789abcdef"
        res = []
        while num and len(res) != 8:
            h = num & 15
            res.append(hex_str[h])
            num >>= 4
        return ''.join(res[::-1])

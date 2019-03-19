class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #执行用时 : 32 ms, 在Find the Difference的Python提交中击败了57.44% 的用户
        #内存消耗 : 10.8 MB, 在Find the Difference的Python提交中击败了0.00% 的用户
        res = {}
        for ele in s:
            res[ele] = res.get(ele, 0) + 1
        for ele in t:
            res[ele] = res.get(ele, 0) - 1
        for key in res:
            if abs(res[key]) == 1:
                return key

        #执行用时 : 56 ms, 在Find the Difference的Python提交中击败了9.30% 的用户
        #内存消耗 : 10.6 MB, 在Find the Difference的Python提交中击败了0.00% 的用户
        from collections import Counter
        return list((Counter(t) - Counter(s)).keys()).pop()

        #python string不支持^=，所以要转成int类，操作完后转成char
        #执行用时 : 28 ms, 在Find the Difference的Python提交中击败了93.26% 的用户
        #内存消耗 : 10.7 MB, 在Find the Difference的Python提交中击败了0.00% 的用户
        leng = len(s)
        res = ord(t[leng])
        for i in range(leng):
            res ^= ord(s[i])
            res ^= ord(t[i])
        return chr(res)


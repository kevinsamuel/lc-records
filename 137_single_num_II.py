class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #执行用时 : 28 ms, 在Single Number II的Python提交中击败了98.61% 的用户
        #内存消耗 : 11.4 MB, 在Single Number II的Python提交中击败了0.00% 的用户
        #这种思路很巧，记一下
        a = b =0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return a|b

        #执行用时 : 40 ms, 在Single Number II的Python提交中击败了34.15% 的用户
        #内存消耗 : 12.3 MB, 在Single Number II的Python提交中击败了0.00% 的用户
        return (3*sum(set(nums)) - sum(nums))/2

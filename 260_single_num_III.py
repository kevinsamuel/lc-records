class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #执行用时 : 40 ms, 在Single Number III的Python提交中击败了28.78% 的用户
        #内存消耗 : 11.7 MB, 在Single Number III的Python提交中击败了0.00% 的用户
        xor = a = b = 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask = mask << 1
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]

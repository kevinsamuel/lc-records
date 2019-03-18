class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #执行用时 : 68 ms, 在Missing Number的Python提交中击败了6.16% 的用户
        #内存消耗 : 11.5 MB, 在Missing Number的Python提交中击败了4.00% 的用户
        # 异或
        res = n = len(nums)
        for i in range(n):
            res ^= i
            res ^= nums[i]
        return res

        #执行用时 : 32 ms, 在Missing Number的Python提交中击败了99.06% 的用户
        #内存消耗 : 11.4 MB, 在Missing Number的Python提交中击败了4.00% 的用户
        #取巧，求和差
        return len(nums) * (len(nums) + 1) / 2 - sum(nums)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #执行用时 : 44 ms, 在Find the Duplicate Number的Python提交中击败了39.86% 的用户
        #内存消耗 : 11.9 MB, 在Find the Duplicate Number的Python提交中击败了16.67% 的用户
        # 实现思路依赖了连表有环时的快慢指针
        # 关于快慢指针可以找到公共点的原理，参考此证明：
        # https://www.520mwx.com/view/3338
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#        # solution 1
#        hash_table = {}
#        loc = 0
#        for ele in nums:
#            hash_table[ele] = loc
#            loc += 1
#
#        loc = 0
#        for ele in nums:
#            another_ele = target - ele
#            if hash_table.get(another_ele) >= 0 and loc != hash_table.get(another_ele):
#                return [loc, hash_table[another_ele]]
#            loc += 1

        # solution 2
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return hash_table[target -num], i
            else:
                hash_table[num] = i

执行用时 : 28 ms, 在Two Sum的Python提交中击败了98.36% 的用户
内存消耗 : 11.9 MB, 在Two Sum的Python提交中击败了0.96% 的用户

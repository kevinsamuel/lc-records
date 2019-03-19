class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #执行用时 : 276 ms, 在Total Hamming Distance的Python提交中击败了84.21% 的用户
        #内存消耗 : 11.7 MB, 在Total Hamming Distance的Python提交中击败了33.33% 的用户
        res = 0
        for i in range(32):
            mask = 1 << i
            total_zero = total_one = 0
            for num in nums:
                if mask & num == 0:
                    total_one += 1
                else:
                    total_zero += 1
            res += total_one * total_zero
        return res

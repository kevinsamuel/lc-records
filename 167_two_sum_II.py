class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            num_sum = numbers[i] + numbers[j]
            if num_sum == target:
                return [i + 1, j + 1]
            elif num_sum > target:
                j -= 1
            else:
                i += 1

执行用时 : 28 ms, 在Two Sum II - Input array is sorted的Python提交中击败了94.41% 的用户
内存消耗 : 10.9 MB, 在Two Sum II - Input array is sorted的Python提交中击败了0.00% 的用户

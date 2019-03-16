# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # 执行用时 : 1028 ms, 在Two Sum IV - Input is a BST的Python提交中击败了0.60% 的用户
        # 内存消耗 : 15.5 MB, 在Two Sum IV - Input is a BST的Python提交中击败了12.90% 的用户
        # if root is None:
        #     return False
        # p_queue = []
        # p_queue.append(root)
        # reminder = []
        # while p_queue:
        #     tmp = p_queue.pop()
        #     if tmp.val in reminder:
        #         return True
        #     reminder.append(k - tmp.val)
        #     if tmp.left:
        #         p_queue.append(tmp.left)
        #     if tmp.right:
        #         p_queue.append(tmp.right)
        # return False

        # 执行用时 : 96 ms, 在Two Sum IV - Input is a BST的Python提交中击败了75.30% 的用户
        # 内存消耗 : 15.3 MB, 在Two Sum IV - Input is a BST的Python提交中击败了22.58% 的用户
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        nums = []
        inorder(root)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #执行用时 : 28 ms, 在Binary Tree Inorder Traversal的Python提交中击败了23.53% 的用户
        #内存消耗 : 10.6 MB, 在Binary Tree Inorder Traversal的Python提交中击败了0.89% 的用户
        res = []
        if root == None:
            return []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res

        #只修改root is None，时间下来4ms百分比就上去了，求心理阴影面积
        #执行用时 : 24 ms, 在Binary Tree Inorder Traversal的Python提交中击败了99.89% 的用户
        #内存消耗 : 10.8 MB, 在Binary Tree Inorder Traversal的Python提交中击败了0.89% 的用户
        res = []
        if root is None:
            return []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        queue = []
        result = []

        if root is None:
            return

        queue.append(root)
        while len(queue) > 0:
            result.append(queue[0].val)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.sort()
        return result[k - 1]


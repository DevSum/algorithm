# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        queue = [root]
        res = []
        while len(queue):
            node = queue.pop(0)
            res.append(node.val)
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
        return res

    def largestValues(self, root):
        root = self.bfs(root)
        level = -1
        tail = -1
        res = []
        maxValue = 0
        for i in range(len(root)):
            if i > tail:
                res.append(maxValue)
                maxValue = root[i]
                level += 1
                tail += 1 << level
            else:
                if (root[i] is not None and root[i] > maxValue) or maxValue is None:
                    maxValue = root[i]
        if root[i] > maxValue:
            maxValue = root[i]
        res.pop(0)
        res.append(maxValue)
        print(res)
        return res


s = Solution()
root = [1, 2, 3]
s.largestValues(root)
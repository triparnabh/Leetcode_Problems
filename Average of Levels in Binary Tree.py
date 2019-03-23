
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':

        q = Queue()
        q.put(root)
        result = []

        while (not q.empty()):
            sum = 0
            count = 0
            temp = Queue()

            while (not q.empty()):
                n = q.queue[0]
                q.get()
                sum += n.val
                count += 1

                if n.left != None:
                    temp.put(n.left)
                if n.right != None:
                    temp.put(n.right)

            q = temp
            result.append(sum * 1.0 / count)

        return result


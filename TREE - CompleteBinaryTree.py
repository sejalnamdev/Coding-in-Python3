
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildtree(a):
    if a is None or a[0] == -1:
        return None

    root = TreeNode(a[0])
    q = deque([root])
    i = 1

    while q and i < len(a):
        node = q.popleft()

        if a[i] != -1:
            node.left = TreeNode(a[i])
            q.append(node.left)

        i += 1

        if i < len(a) and a[i] != -1:
            node.right = TreeNode(a[i])
            q.append(node.right)

        i += 1

    return root

class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        

        q = deque([root])
        nullfound = False

        while q:
            node = q.popleft()

            if node is None:
                nullfound = True

            else:
                if nullfound :
                    return False
                q.append(node.left)
                q.append(node.right)

        return True

a = list(map(int,input().split()))
root = buildtree(a)
s = Solution()
print(s.isCompleteTree(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        level = 0

        q = deque()

        q.append(root)

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
                res[level].append(node.val)

            level += 1

        answer = []

        for result in res:
            answer.append(result[-1])
        
        return answer


        
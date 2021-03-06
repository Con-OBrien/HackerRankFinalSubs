# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        options, p = [], []

        def dfs(N):
            if N is None:
                return
            p.append(N.val)

            if N.left is None and N.right is None:
                options.append(list(p))
            else:
                dfs(N.left), dfs(N.right)

            p.pop()

        dfs(root)
        quickestPath = 99999
        fastestPath = []
        sum_tot = 0
        for i, path in enumerate(options):
            for number in path:
                sum_tot += number
            if sum_tot < quickestPath:
                quickestPath = sum_tot
                fastestPath = path
            sum_tot = 0

        return fastestPath

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
                # Append param value to list
            p.append(N.val)
            # Add this value to the sum

            if N.left is None and N.right is None and sum(p) == targetSum:
                options.append(list(p))
            else:
                dfs(N.left), dfs(N.right)
            p.pop()

        # start from root with blank cur list and 0 as the sum
        """
        dfs(root)
        quickestPath = 99999
        fastestPath = []
        sum = 0
        for i, path in enumerate(options):
            for number in path:
                sum += number
            if(sum < quickestPath):
                quickestPath = sum
                fastestPath = path
            sum = 0
        print(fastestPath)  
        """
        dfs(root)
        return options

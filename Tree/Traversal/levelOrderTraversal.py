class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root):
    if root is None:
        return -1
    # 1. Init Empty list
    vals = []
    # 2. Append root value
    vals.append(root)

    # 3. Loop through length of vals while is greater than 0
    while (len(vals)):
        # 4. Print first vals value, initially being root
        print(vals[0].info, end=' ')
        # 5. Get rid of this value in popped and use as check for where to move
        node = vals.pop(0)
        # 6. Check left side if option is there, if it is, append that value e.g. we get to 5, it will do
        # 3 first and then also 6
        if node.left is not None:
            vals.append(node.left)
        if node.right is not None:
            vals.append(node.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
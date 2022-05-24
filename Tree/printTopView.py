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


# What does top view mean? if we say root has horizontal distance of 0,
# each left movement is a -1 and
# every right movement is a +1
def topView(root):
    if root is None:
        return -1
    # Init empty list of vals
    vals = []
    # Init empty dictionary of horizontal distances
    options = {}
    # Default root level to 0
    root.level = 0
    # Add root value to values
    vals.append(root)

    while (len(vals)):

        root = vals[0]
        level = root.level

        if (level not in options):
            options[level] = root.info
        if (root.left):
            root.left.level = level - 1
            vals.append(root.left)
        if (root.right):
            root.right.level = level + 1
            vals.append(root.right)
        vals.pop(0)

    for i in sorted(options):
        print(options[i], end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
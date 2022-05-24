class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        # Check root value, is the val param greater than or less than root
        # If greater than, check if root.right is not None
        # if not none, increase root position to root.right, is val > or < than new root
        # If less, check if root.left is not None
        # In any of these situations, if root.left or root.right is None and that is where the val should            be, root.direction should be saved as val

        if self.root is None:
            self.root = Node(val)

        cur = self.root

        while True:
            if cur.info == val:
                break
            elif cur.info < val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

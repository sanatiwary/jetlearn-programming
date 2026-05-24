class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def inOrderTrav(root):
    if root:
        if root.left:
            inOrderTrav(root.left)
        print(root.data)
        if root.right:
            inOrderTrav(root.right)

def insert(root, a):
    if root == None:
        return TreeNode(a)
    if a < root.data:
        root.left = insert(root.left, a)
    else:
        root.right = insert(root.right, a)
    return root

def search(root, b):
    if b == root.data:
        return root
    elif root.right and b > root.data:
        return search(root.right, b)
    elif root.left and b < root.data:
        return search(root.left, b)
    else: return -1
        
l = int(input("enter the number of elements you want in the tree: "))
root = None
for i in range(l):
    x = int(input("enter the node value: "))
    root = insert(root, x)

inOrderTrav(root)

key = int(input("enter the key to be searched: "))
keyNode = search(root, key)

if keyNode == -1: print("the key was not found")
else: print("the key was found: ", keyNode.data)
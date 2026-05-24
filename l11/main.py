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
    if not root:
        return TreeNode(a)
    if a < root.data:
        root.left = insert(root.left, a)
    else:
        root.right = insert(root.right, a)
    return root

# def search(root, b):
#     if b == root.data:
#         return root
#     elif root.right and b > root.data:
#         return search(root.right, b)
#     elif root.left and b < root.data:
#         return search(root.left, b)
#     else:
#         return -1
    
def delete(root, c):
    if not root:
        return root
    
    if c < root.data:
        root.left = delete(root.left, c)
    elif c > root.data:
        root.right = delete(root.right, c)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        
        temp = minNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def minNode(node):
    current = node
    while current.left:
        current = current.left
    return current

l = int(input("enter the number of elements you want in the tree: "))
root = None
for i in range(l):
    x = int(input("enter the node value: "))
    root = insert(root, x)

inOrderTrav(root)

key = int(input("enter the key to be deleted: "))
keyNode = delete(root, key)

print("new tree: ", inOrderTrav(root))
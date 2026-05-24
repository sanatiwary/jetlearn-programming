class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# l, a, r
def inOrderTrav(node):
    if node:
        inOrderTrav(node.left)
        print(node.val, end=", ")
        inOrderTrav(node.right)

# a, l, r
def preOrderTrav(node):
    if node:
        print(node.val, end=", ")
        preOrderTrav(node.left)
        preOrderTrav(node.right)

# l, r, a
def postOrderTrav(node):
    if node:
        postOrderTrav(node.left)
        postOrderTrav(node.right)
        print(node.val, end=", ")

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")

print("\n in order traversal: ")
inOrderTrav(root)

print("\n pre order traversal: ")
preOrderTrav(root)

print("\n post order traversal: ")
postOrderTrav(root)
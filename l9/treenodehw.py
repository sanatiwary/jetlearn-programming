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

key = int(input("enter 1 for in order traversal, 2 for pre order traversal, or 3 for post order traversal: "))
if key == 1:
    print("\n in order traversal: ")
    inOrderTrav(root)
elif key == 2:
    print("\n pre order traversal: ")
    preOrderTrav(root)
elif key == 3:
    print("\n post order traversal: ")
    postOrderTrav(root)
else:
    print("please enter a valid option")
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print preorder traversal
def preorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    preorder(node.left)

    # Recur on right subtree
    preorder(node.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Preorder traversal of binary tree is:")
    preorder(root)        
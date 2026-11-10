# Binary Tree Creation and Traversal
# Recursive and Iterative Tree Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Binary Tree Creation
def create_tree():
    print("Enter -1 for no node")

    data = int(input("Enter root node: "))

    if data == -1:
        return None

    root = Node(data)

    queue = [root]

    while queue:
        current = queue.pop(0)

        left_data = int(input(f"Enter left child of {current.data}: "))

        if left_data != -1:
            current.left = Node(left_data)
            queue.append(current.left)

        right_data = int(input(f"Enter right child of {current.data}: "))

        if right_data != -1:
            current.right = Node(right_data)
            queue.append(current.right)

    return root


# Recursive Preorder Traversal
# Root -> Left -> Right
def preorder_recursive(root):
    if root:
        print(root.data, end=" ")
        preorder_recursive(root.left)
        preorder_recursive(root.right)


# Recursive Inorder Traversal
# Left -> Root -> Right
def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.data, end=" ")
        inorder_recursive(root.right)


# Recursive Postorder Traversal
# Left -> Right -> Root
def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.data, end=" ")


# Iterative Preorder Traversal
def preorder_iterative(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


# Iterative Inorder Traversal
def inorder_iterative(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right


# Iterative Postorder Traversal
def postorder_iterative(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    while stack2:
        print(stack2.pop().data, end=" ")


# Main Program
root = create_tree()

if root is None:
    print("Tree is empty")

else:
    while True:
        print("\n\n----- BINARY TREE TRAVERSAL MENU -----")
        print("1. Recursive Preorder Traversal")
        print("2. Recursive Inorder Traversal")
        print("3. Recursive Postorder Traversal")
        print("4. Iterative Preorder Traversal")
        print("5. Iterative Inorder Traversal")
        print("6. Iterative Postorder Traversal")
        print("7. Display All Recursive Traversals")
        print("8. Display All Iterative Traversals")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Recursive Preorder:")
            preorder_recursive(root)

        elif choice == 2:
            print("Recursive Inorder:")
            inorder_recursive(root)

        elif choice == 3:
            print("Recursive Postorder:")
            postorder_recursive(root)

        elif choice == 4:
            print("Iterative Preorder:")
            preorder_iterative(root)

        elif choice == 5:
            print("Iterative Inorder:")
            inorder_iterative(root)

        elif choice == 6:
            print("Iterative Postorder:")
            postorder_iterative(root)

        elif choice == 7:
            print("\nRecursive Preorder:")
            preorder_recursive(root)

            print("\nRecursive Inorder:")
            inorder_recursive(root)

            print("\nRecursive Postorder:")
            postorder_recursive(root)

        elif choice == 8:
            print("\nIterative Preorder:")
            preorder_iterative(root)

            print("\nIterative Inorder:")
            inorder_iterative(root)

            print("\nIterative Postorder:")
            postorder_iterative(root)

        elif choice == 9:
            print("Program terminated.")
            break

        else:
            print("Invalid choice! Please try again.")
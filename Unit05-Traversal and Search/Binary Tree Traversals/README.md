# Binary Tree Creation and Tree Traversal

## 1. Problem Statement

To implement a Binary Tree using Python and perform different tree traversal techniques. The program creates a binary tree using user input and performs Preorder, Inorder, and Postorder traversals using both recursive and iterative approaches.

The program demonstrates the concept of binary tree data structures, recursion, and stack-based traversal.

## 2. Objectives

- To understand the concept of a Binary Tree.
- To create a binary tree dynamically using user input.
- To implement Preorder Traversal.
- To implement Inorder Traversal.
- To implement Postorder Traversal.
- To perform recursive tree traversal.
- To perform iterative tree traversal using stacks.
- To compare recursive and iterative approaches.

## 3. Algorithm / Approach

### A. Binary Tree Creation

1. Define a Node class containing data, left child, and right child.
2. Take the root node as input.
3. If the input is -1, consider the tree empty.
4. Otherwise, create the root node.
5. Use a queue to insert nodes level by level.
6. Take left and right child values for each node.
7. If the value is not -1, create a new node and attach it to the respective child.
8. Repeat until all nodes are created.

### B. Recursive Preorder Traversal

1. Check whether the current node is NULL.
2. Visit the root node.
3. Traverse the left subtree.
4. Traverse the right subtree.

**Order:** Root → Left → Right

### C. Recursive Inorder Traversal

1. Check whether the current node is NULL.
2. Traverse the left subtree.
3. Visit the root node.
4. Traverse the right subtree.

**Order:** Left → Root → Right

### D. Recursive Postorder Traversal

1. Check whether the current node is NULL.
2. Traverse the left subtree.
3. Traverse the right subtree.
4. Visit the root node.

**Order:** Left → Right → Root

### E. Iterative Tree Traversal

Iterative traversal uses an explicit stack instead of recursive function calls.

- Preorder: Use a stack and push the right child before the left child.
- Inorder: Traverse the leftmost path, pop and visit nodes, then move to the right child.
- Postorder: Use two stacks to process nodes and reverse their order.

## 4. Pseudocode

### Binary Tree Creation

```text
CREATE_TREE()
    Read root data
    If root data = -1
        Return NULL

    Create root node
    Insert root into queue

    While queue is not empty
        Remove front node
        Read left child
        If left child != -1
            Create and attach left node
            Insert into queue

        Read right child
        If right child != -1
            Create and attach right node
            Insert into queue

    Return root
```

### Preorder Traversal

```text
PREORDER(root)
    If root is not NULL
        Visit root
        PREORDER(root.left)
        PREORDER(root.right)
```

### Inorder Traversal

```text
INORDER(root)
    If root is not NULL
        INORDER(root.left)
        Visit root
        INORDER(root.right)
```

### Postorder Traversal

```text
POSTORDER(root)
    If root is not NULL
        POSTORDER(root.left)
        POSTORDER(root.right)
        Visit root
```

### Iterative Traversal

```text
ITERATIVE_PREORDER(root)
    Push root into stack

    While stack is not empty
        Pop and visit node
        Push right child
        Push left child
```

```text
ITERATIVE_INORDER(root)
    While current is not NULL or stack is not empty
        Push all left nodes
        Pop and visit node
        Move to right child
```

```text
ITERATIVE_POSTORDER(root)
    Use two stacks
    Process nodes using first stack
    Store them in second stack
    Pop and visit nodes from second stack
```

## 5. Sample Input

Consider the following binary tree:

```text
          1
         / \
        2   3
       / \ / \
      4  5 6  7
```

Input during tree creation:

```text
Enter root node: 1
Enter left child of 1: 2
Enter right child of 1: 3
Enter left child of 2: 4
Enter right child of 2: 5
Enter left child of 3: 6
Enter right child of 3: 7
Enter left child of 4: -1
Enter right child of 4: -1
Enter left child of 5: -1
Enter right child of 5: -1
Enter left child of 6: -1
Enter right child of 6: -1
Enter left child of 7: -1
Enter right child of 7: -1
```

## 6. Sample Output

```text
----- BINARY TREE TRAVERSAL MENU -----

1. Recursive Preorder Traversal
2. Recursive Inorder Traversal
3. Recursive Postorder Traversal
4. Iterative Preorder Traversal
5. Iterative Inorder Traversal
6. Iterative Postorder Traversal
7. Display All Recursive Traversals
8. Display All Iterative Traversals
9. Exit
```

### Recursive Traversal Output

```text
Recursive Preorder:
1 2 4 5 3 6 7

Recursive Inorder:
4 2 5 1 6 3 7

Recursive Postorder:
4 5 2 6 7 3 1
```

### Iterative Traversal Output

```text
Iterative Preorder:
1 2 4 5 3 6 7

Iterative Inorder:
4 2 5 1 6 3 7

Iterative Postorder:
4 5 2 6 7 3 1
```

## 7. Time and Space Complexity

Let n represent the total number of nodes in the binary tree.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Binary Tree Creation | O(n) | O(n) |
| Recursive Preorder | O(n) | O(h) |
| Recursive Inorder | O(n) | O(h) |
| Recursive Postorder | O(n) | O(h) |
| Iterative Preorder | O(n) | O(n) |
| Iterative Inorder | O(n) | O(n) |
| Iterative Postorder | O(n) | O(n) |

Here, h represents the height of the tree. Recursive traversal uses O(h) function call stack space.

## 8. Applications

- Expression tree evaluation.
- Syntax tree processing in compilers.
- Searching and sorting operations.
- Hierarchical data representation.
- File system directory structures.
- Database indexing.
- Artificial Intelligence and decision trees.

## 9. Conclusion

In this experiment, a Binary Tree was successfully created using Python. Preorder, Inorder, and Postorder traversals were implemented using both recursive and iterative approaches.

Recursive traversal uses function calls to visit nodes, whereas iterative traversal uses an explicit stack. Both approaches produce the same traversal sequences. This experiment helps in understanding tree data structures, recursion, stack operations, and different methods of processing hierarchical data.
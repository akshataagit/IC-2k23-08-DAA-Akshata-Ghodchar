
# Algorithm Design & Analysis Laboratory

## About the Repository

This repository contains practical implementations of various algorithms and problem-solving techniques studied in the **Algorithm Design and Analysis Laboratory**.

The repository covers fundamental algorithmic concepts, including searching, sorting, complexity analysis, Divide and Conquer, Greedy Method, Dynamic Programming, Graph Traversal, Backtracking, and NP-Hard / NP-Complete problems.

All programs are implemented in Python to understand how different algorithms work, analyze their performance, and solve computational problems efficiently.

The repository is organized into seven units according to the laboratory syllabus.

---

## Objectives

- Understand the fundamentals of algorithm design and analysis.
- Learn different algorithm design techniques.
- Implement searching and sorting algorithms.
- Understand time and space complexity.
- Analyze theoretical and experimental algorithm performance.
- Apply Divide and Conquer, Greedy, and Dynamic Programming techniques.
- Understand graph representation and traversal algorithms.
- Solve constraint-satisfaction problems using Backtracking.
- Understand NP-Hard and NP-Complete problems.
- Compare algorithms based on their efficiency and performance.

---

## Repository Structure

```text
Algorithm-Design-Analysis-Laboratory/
│
├── Unit1_Introduction_and_Performance_Analysis/
│   ├── Searching/
│   ├── Complexity_Analysis/
│   ├── Performance_Measurement/
│   └── README.md
│
├── Unit2_Divide_and_Conquer/
│   ├── Binary_Search/
│   ├── Max_Min/
│   ├── Merge_Sort/
│   ├── Quick_Sort/
│   ├── Heap_Sort/
│   ├── Strassen_Matrix_Multiplication/
│   └── README.md
│
├── Unit3_Greedy_Method/
│   ├── Fractional_Knapsack/
│   ├── Job_Sequencing/
│   ├── Prims_Algorithm/
│   ├── Kruskals_Algorithm/
│   └── README.md
│
├── Unit4_Dynamic_Programming/
│   ├── Memoized_Fibonacci/
│   ├── Knapsack_01/
│   ├── Multistage_Graph/
│   ├── Floyd_Warshall/
│   ├── Shortest_Path/
│   ├── Traveling_Salesperson_Problem/
│   └── README.md
│
├── Unit5_Traversal_and_Search/
│   ├── Binary_Tree_Traversals/
│   ├── Graph_Representation/
│   ├── BFS/
│   ├── DFS/
│   └── README.md
│
├── Unit6_Backtracking/
│   ├── N_Queens/
│   ├── Sum_of_Subsets/
│   └── README.md
│
├── Unit7_NP_Hard_NP_Complete/
│   ├── Exhaustive_Search/
│   ├── Branch_and_Bound/
│   ├── Knapsack_01/
│   ├── Traveling_Salesperson_Problem/
│   └── README.md
│
└── README.md
```

---

# Units and Experiments

## Unit 1: Introduction to Algorithms & Performance Analysis

This unit introduces the basic concepts of algorithms and their performance evaluation. It focuses on understanding algorithm efficiency and measuring execution time.

### Topics Covered

- Searching Algorithms
- Complexity Analysis
- Performance Measurement

### Key Concepts
- Algorithm definition and characteristics
- Time complexity and space complexity
- Best-case, average-case, and worst-case analysis
- Asymptotic notations: Big O, Omega, and Theta
- Theoretical versus experimental analysis
- Execution time measurement

---

## Unit 2: Divide and Conquer

Divide and Conquer is an algorithm design technique that divides a large problem into smaller subproblems, solves them independently, and combines their results.

### Experiments

1. **Binary Search:** Finds an element in a sorted array by repeatedly dividing the search interval into two halves.
2. **Maximum and Minimum:** Finds the maximum and minimum elements of an array using a divide-and-conquer approach.
3. **Merge Sort:** Sorts an array by dividing it into smaller parts, sorting them, and merging the results.
4. **Quick Sort:** Uses a pivot element to partition an array into smaller subarrays and recursively sorts them.
5. **Heap Sort:** Uses a binary heap data structure to sort elements.
6. **Strassen Matrix Multiplication:** Performs matrix multiplication using seven recursive multiplications instead of eight.

### Key Concepts
- Recursion
- Problem decomposition
- Divide and combine strategies
- Recurrence relations
- Master Theorem
- Algorithm complexity analysis

---

## Unit 3: Greedy Method

The Greedy Method solves optimization problems by making the locally optimal choice at each step, aiming to achieve a globally optimal solution.

### Experiments

1. **Fractional Knapsack:** Selects items based on their value-to-weight ratio to maximize total profit.
2. **Job Sequencing with Deadlines:** Schedules jobs to maximize profit while satisfying their deadlines.
3. **Prim's Algorithm:** Finds a Minimum Spanning Tree by repeatedly selecting the minimum-weight edge connecting a visited vertex to an unvisited vertex.
4. **Kruskal's Algorithm:** Constructs a Minimum Spanning Tree by selecting edges in increasing order of weight while avoiding cycles.

### Key Concepts
- Greedy-choice property
- Optimal substructure
- Minimum Spanning Tree
- Sorting and selection
- Disjoint Set Union
- Optimization problems

---

## Unit 4: Dynamic Programming

Dynamic Programming solves complex problems by breaking them into overlapping subproblems and storing their results to avoid repeated calculations.

### Experiments

1. **Memoized Fibonacci:** Calculates Fibonacci numbers using recursion with memoization.
2. **0/1 Knapsack:** Maximizes the total value of selected items without exceeding the given capacity.
3. **Multistage Graph:** Finds the minimum-cost path from a source vertex to a destination vertex in a multistage directed graph.
4. **Floyd-Warshall Algorithm:** Finds shortest paths between all pairs of vertices in a weighted graph.
5. **Single-Source Shortest Path:** Finds shortest paths from one source vertex to other vertices in a graph.
6. **Traveling Salesperson Problem (TSP):** Finds a minimum-cost tour that visits every city exactly once and returns to the starting city using Dynamic Programming.

### Key Concepts
- Optimal substructure
- Overlapping subproblems
- Memoization
- Tabulation
- State transitions
- Space-time trade-offs

---

## Unit 5: Traversal & Search

This unit focuses on tree and graph data structures and different techniques used to traverse and search their elements.

### Experiments

1. **Binary Tree Traversals:** Implements inorder, preorder, and postorder traversal.
2. **Graph Representation:** Represents graphs using adjacency matrices and adjacency lists.
3. **Breadth-First Search (BFS):** Traverses a graph level by level using a queue.
4. **Depth-First Search (DFS):** Explores a graph deeply before backtracking, using recursion or a stack.

### Key Concepts
- Tree data structures
- Graph representation
- Adjacency matrix
- Adjacency list
- Queue and stack
- Recursive traversal
- Visited-node tracking

---

## Unit 6: Backtracking

Backtracking is an algorithmic technique that builds a solution incrementally and abandons a partial solution when it cannot lead to a valid complete solution.

### Experiments

1. **N-Queens Problem:** Places N queens on an N x N chessboard such that no two queens attack each other.
2. **Sum of Subsets:** Finds all subsets of a given set whose sum equals a specified target value.

### Key Concepts
- Recursive problem solving
- State space tree
- Constraint satisfaction
- Choice and exploration
- Backtracking and pruning

---


This unit introduces computationally difficult problems and techniques used to solve or approximate them.

### Experiments

1. **Exhaustive Search:** Explores all possible candidate solutions to identify a valid or optimal solution.
2. **Branch and Bound:** Uses bounding functions to eliminate branches that cannot produce a better solution.
3. **0/1 Knapsack:** Solves the optimization problem using exact search or Branch and Bound.
4. **Traveling Salesperson Problem (TSP):** Finds a minimum-cost tour by exploring possible city arrangements using exhaustive search or Branch and Bound.

### Key Concepts
- P and NP complexity classes
- NP-Hard problems
- NP-Complete problems
- Polynomial-time verification
- Exhaustive search
- State space tree
- Branch and Bound
- Bounding functions and pruning

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| Jupyter Notebook | Interactive experimentation (if used) |
| VS Code | Code editor |
| Git | Version control |
| GitHub | Repository hosting |

---

## Installation and Setup

### 1. Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/akshataagit/IC-2k23-08-DAA-Akshata-Ghodchar
```

### 3. Navigate to the Repository

```bash
cd Algorithm-Design-Analysis-Laboratory
```

### 4. Run a Program

Navigate to the required unit and experiment folder.

For example:

```bash
cd Unit2_Divide_and_Conquer
python Merge_Sort.py
```

**Note:** Replace the filename with the actual Python file name in your experiment folder.

---

## Algorithm Complexity Overview

The following table summarizes the typical time complexities of important algorithms covered in this repository.

| Algorithm | Time Complexity |
|---|---|
| Binary Search | O(log N) |
| Merge Sort | O(N log N) |
| Quick Sort | O(N log N) average |
| Heap Sort | O(N log N) |
| Strassen Matrix Multiplication | O(N^2.807) approximately |
| Fractional Knapsack | O(N log N) |
| Job Sequencing | O(N²) in a common implementation |
| Prim's Algorithm | O(E log V) with a binary heap |
| Kruskal's Algorithm | O(E log E) |
| Memoized Fibonacci | O(N) |
| 0/1 Knapsack | O(N × W) using DP |
| Floyd-Warshall | O(V³) |
| BFS | O(V + E) |
| DFS | O(V + E) |
| N-Queens | O(N!) upper bound |
| Sum of Subsets | O(2^N) |

*Note: Actual complexity can vary depending on the implementation, data structures, and input conditions.*

---

## Learning Outcomes

After completing these experiments, the following skills and concepts will be developed:

- Ability to design and implement algorithms using Python.
- Understanding of different algorithm design paradigms.
- Ability to analyze time and space complexity.
- Knowledge of sorting and searching techniques.
- Understanding of optimization using Greedy and Dynamic Programming.
- Ability to solve graph and tree-related problems.
- Understanding of recursive and backtracking algorithms.
- Knowledge of computational complexity and NP-Hard problems.
- Ability to compare algorithms based on theoretical and practical performance.

---

## How to Use This Repository

1. Navigate to the required unit folder.
2. Open the experiment folder.
3. Read its README.md file to understand the problem statement and algorithm.
4. Open the corresponding Python program.
5. Execute the program using Python.
6. Observe the output and analyze the algorithm's performance.

Each experiment folder can contain:
- Python source code (`.py`)
- Jupyter Notebook (`.ipynb`), if applicable
- README.md containing the problem statement, objective, algorithm, pseudocode, complexity analysis, sample output, and result.

---

## Conclusion

This repository provides a practical understanding of the major algorithm design and analysis techniques covered in the laboratory syllabus. Through the implementation of searching, sorting, Divide and Conquer, Greedy Method, Dynamic Programming, graph traversal, Backtracking, and NP-Hard / NP-Complete problems, it helps develop problem-solving and algorithmic thinking skills.

The experiments demonstrate how different approaches can be used to solve computational problems and how their efficiency can be evaluated through time and space complexity.

---

**Language:** Python 3

**Subject:** Algorithm Design & Analysis Laboratory

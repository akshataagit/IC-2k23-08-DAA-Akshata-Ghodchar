 Analyze Best, Average, and Worst-Case Complexity

1. Problem Statement

Analyze the best-case, average-case, and worst-case time complexity of Binary Search by counting the number of comparisons performed during searching.

2. Algorithm / Approach

Create a sorted array containing n elements.

Search for the middle element to demonstrate the best case.

Search for the last element to demonstrate a deeper search.

Search for an element that does not exist in the array.

Count the number of comparisons performed.

Compare the results with theoretical time complexity.

3. Pseudocode

START

INPUT n

CREATE sorted array

FOR each test case

    low = 0
    high = n - 1
    comparisons = 0

    WHILE low <= high

        mid = (low + high) // 2

        comparisons = comparisons + 1

        IF array[mid] = target
            RETURN index and comparisons

        ELSE IF array[mid] < target
            low = mid + 1

        ELSE
            high = mid - 1

    RETURN -1 and comparisons

STOP

4. Time & Space Complexity Analysis

Case

Condition

Complexity

Best Case

Target is at the middle

O(1)

Average Case

Target is found after multiple divisions

O(log n)

Worst Case

Maximum search divisions are required

O(log n)

Space Complexity: O(1) for iterative Binary Search.

5. Sample Input / Output

Input:

Enter number of elements: 15

Output:

Best Case:
Target: 8
Index: 7
Comparisons: 1

Worst-Style Case:
Target: 15
Index: 14
Comparisons: 4

Unsuccessful Search:
Target: 16
Index: -1
Comparisons: 4

Time Complexity Analysis:
Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)





6. Experimental Results

The experimental analysis shows that the best case requires only one comparison when the target is at the middle position. The average and worst cases require logarithmic comparisons because the search space is reduced by half in every iteration.

7. Learning Outcomes

Understood asymptotic complexity.

Learned best, average, and worst-case analysis.

Understood comparison counting.

Learned how to evaluate searching algorithms.
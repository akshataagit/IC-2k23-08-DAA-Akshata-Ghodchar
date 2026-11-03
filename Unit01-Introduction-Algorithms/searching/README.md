Iterative Binary Search

1. Problem Statement

Implement Binary Search using an iterative approach to find a given element in a sorted array.

2. Algorithm / Approach

Initialize two variables, low and high.

Calculate the middle index using the formula:

mid = (low + high) // 2

Compare the middle element with the target.

If both are equal, return the middle index.

If the target is greater, search the right half.

If the target is smaller, search the left half.

Repeat until the element is found or the search interval becomes empty.

3. Pseudocode

START

INPUT sorted array
INPUT target

low = 0
high = n - 1

WHILE low <= high

    mid = (low + high) // 2

    IF array[mid] = target
        RETURN mid

    ELSE IF array[mid] < target
        low = mid + 1

    ELSE
        high = mid - 1

RETURN -1

STOP

4. Time & Space Complexity Analysis

Case

Time Complexity

Best Case

O(1)

Average Case

O(log n)

Worst Case

O(log n)

Space Complexity: O(1), because the iterative approach uses a constant amount of extra memory.

5. Sample Input / Output

Input:

Enter sorted array elements: 10 20 30 40 50 60
Enter element to search: 40

Output:

Element found at index: 3



6. Experimental Results

The iterative Binary Search algorithm successfully searches for an element in a sorted array. It reduces the search space by half in every iteration, resulting in logarithmic time complexity.

7. Learning Outcomes

Understood the Binary Search algorithm.

Learned the iterative searching technique.

Understood the importance of sorted arrays.

Learned the divide-and-conquer approach.

Experiment 3: Recursive Binary Search

1. Problem Statement

Implement Binary Search using recursion to find a target element in a sorted array.

2. Algorithm / Approach

Pass the array, target, low, and high values to the recursive function.

Check whether low is greater than high.

If true, return -1 because the element is not present.

Calculate the middle index.

If the middle element matches the target, return its index.

If the target is greater, recursively search the right half.

Otherwise, recursively search the left half.

Continue until the element is found or the base condition is reached.

3. Pseudocode

BINARY_SEARCH(array, target, low, high)

    IF low > high
        RETURN -1

    mid = (low + high) // 2

    IF array[mid] = target
        RETURN mid

    ELSE IF array[mid] < target
        RETURN BINARY_SEARCH(
            array, target, mid + 1, high
        )

    ELSE
        RETURN BINARY_SEARCH(
            array, target, low, mid - 1
        )

END

4. Time & Space Complexity Analysis

Case

Time Complexity

Best Case

O(1)

Average Case

O(log n)

Worst Case

O(log n)

Space Complexity: O(log n), because recursive function calls require stack memory.

5. Sample Input / Output

Input:

Enter sorted array elements: 5 10 15 20 25 30 35
Enter element to search: 25

Output:

Element found at index: 4



6. Experimental Results

The recursive Binary Search program successfully finds elements in a sorted array. It produces the same searching result as the iterative approach but uses additional memory for recursive function calls.

7. Learning Outcomes

Understood recursion and recursive function calls.

Learned the base condition in recursion.

Implemented Binary Search using recursion.

Compared recursive and iterative approaches.
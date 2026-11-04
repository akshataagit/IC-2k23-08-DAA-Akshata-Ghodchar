Experiment 1: Binary Search Using Divide and Conquer

1. Problem Statement

Implement Binary Search using the Divide and Conquer technique to find a given element in a sorted array.

2. Algorithm / Approach

Initialize low and high pointers.

Calculate the middle index.

Compare the middle element with the target element.

If the target matches, return its index.

If the target is greater, recursively search the right half.

If the target is smaller, recursively search the left half.

Continue until the element is found or the search space becomes empty.

3. Pseudocode

BINARY_SEARCH(arr, target, low, high)

    IF low > high
        RETURN -1

    mid = (low + high) // 2

    IF arr[mid] == target
        RETURN mid

    ELSE IF arr[mid] < target
        RETURN BINARY_SEARCH(
            arr, target, mid+1, high
        )

    ELSE
        RETURN BINARY_SEARCH(
            arr, target, low, mid-1
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

Space Complexity: O(log n) because of recursive function calls.

5. Sample Input / Output

Input:

Enter sorted array elements: 10 20 30 40 50 60
Enter element to search: 40

Output:

Element found at index: 3


6. Experimental Results

The program successfully searches for an element using recursive Binary Search. The search space is divided into two halves at every recursive call, resulting in logarithmic time complexity.

7. Learning Outcomes

Understood the Divide and Conquer approach.

Learned recursive Binary Search.

Understood the importance of sorted arrays.

Learned logarithmic time complexity.
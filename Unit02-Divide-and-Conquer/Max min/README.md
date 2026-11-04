Experiment 2: Maximum and Minimum Using Divide and Conquer

1. Problem Statement

Write a Python program to find the maximum and minimum elements of an array using the Divide and Conquer technique.

2. Algorithm / Approach

Divide the array into two halves.

Find the maximum and minimum of the left half recursively.

Find the maximum and minimum of the right half recursively.

Compare the maximum values of both halves.

Compare the minimum values of both halves.

Return the final maximum and minimum elements.

3. Pseudocode

MAX_MIN(arr, low, high)

    IF low == high
        RETURN arr[low], arr[low]

    IF high == low + 1
        COMPARE arr[low] AND arr[high]
        RETURN maximum, minimum

    mid = (low + high) // 2

    max1, min1 = MAX_MIN(arr, low, mid)

    max2, min2 = MAX_MIN(arr, mid+1, high)

    maximum = MAX(max1, max2)

    minimum = MIN(min1, min2)

    RETURN maximum, minimum

END

4. Time & Space Complexity Analysis

Case

Time Complexity

Best Case

O(n)

Average Case

O(n)

Worst Case

O(n)

Space Complexity: O(log n) due to recursion.

5. Sample Input / Output

Input:

Enter array elements: 10 5 20 8 30 2 15

Output:

Maximum element: 30
Minimum element: 2



7. Experimental Results

The program successfully identifies the maximum and minimum elements by dividing the array into smaller parts and combining the results.

8. Learning Outcomes

Understood Divide and Conquer.

Learned recursive array processing.

Learned to find maximum and minimum efficiently.

Understood O(n) time complexity.
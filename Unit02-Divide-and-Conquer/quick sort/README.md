Experiment 4: Quick Sort

1. Problem Statement

Implement Quick Sort using the Divide and Conquer technique to sort an array in ascending order.

2. Algorithm / Approach

Select an element as the pivot.

Partition the array so that smaller elements are placed before the pivot and larger elements after it.

Place the pivot in its correct sorted position.

Recursively apply Quick Sort to the left partition.

Recursively apply Quick Sort to the right partition.

Continue until all elements are sorted.

3. Pseudocode

QUICK_SORT(arr, low, high)

    IF low < high

        pi = PARTITION(arr, low, high)

        QUICK_SORT(arr, low, pi-1)

        QUICK_SORT(arr, pi+1, high)

END


PARTITION(arr, low, high)

    pivot = arr[high]

    i = low - 1

    FOR j = low TO high-1

        IF arr[j] <= pivot

            i = i + 1

            SWAP arr[i] AND arr[j]

    SWAP arr[i+1] AND arr[high]

    RETURN i+1

END

4. Time & Space Complexity Analysis

Case

Time Complexity

Best Case

O(n log n)

Average Case

O(n log n)

Worst Case

O(n²)

Space Complexity:

Average Case: O(log n).

Worst Case: O(n).

5. Sample Input / Output

Input:

Enter array elements: 50 20 60 10 30 40

Output:

Sorted array: [10, 20, 30, 40, 50, 60]



7. Experimental Results

The Quick Sort algorithm successfully sorts the array using partitioning. Its average performance is O(n log n), but its worst-case complexity becomes O(n²) when partitions are highly unbalanced.

8. Learning Outcomes

Understood the concept of pivot selection.

Learned array partitioning.

Implemented recursive sorting.

Compared best, average, and worst-case complexity.
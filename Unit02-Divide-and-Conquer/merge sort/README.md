Experiment 3: Merge Sort

1. Problem Statement

Implement the Merge Sort algorithm using Divide and Conquer to sort an array in ascending order.

2. Algorithm / Approach

Divide the array into two halves.

Recursively divide each half until individual elements remain.

Compare the elements of the two smaller sorted arrays.

Merge them into a single sorted array.

Continue merging until the entire array is sorted.

3. Pseudocode

MERGE_SORT(arr, left, right)

    IF left < right

        mid = (left + right) // 2

        MERGE_SORT(arr, left, mid)

        MERGE_SORT(arr, mid+1, right)

        MERGE(arr, left, mid, right)

END


MERGE(arr, left, mid, right)

    CREATE left and right subarrays

    COMPARE elements of both arrays

    COPY smaller element into original array

    COPY remaining elements

END

4. Time & Space Complexity Analysis

Case

Time Complexity

Best Case

O(n log n)

Average Case

O(n log n)

Worst Case

O(n log n)

Space Complexity: O(n) for temporary arrays.

5. Sample Input / Output

Input:

Enter array elements: 38 27 43 3 9 82 10

Output:

Sorted array: [3, 9, 10, 27, 38, 43, 82]


7. Experimental Results

The Merge Sort algorithm successfully sorts the array in ascending order. It repeatedly divides the array into smaller parts and merges the sorted parts.

8. Learning Outcomes

Understood Divide and Conquer sorting.

Learned how merging works.

Understood recursion and subarrays.

Learned O(n log n) sorting complexity.
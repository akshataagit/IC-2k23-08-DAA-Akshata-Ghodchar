Experiment 5: Heap Sort

1. Problem Statement

Implement Heap Sort using a Max Heap to arrange the elements of an array in ascending order.

2. Algorithm / Approach

Convert the given array into a Max Heap.

A Max Heap is a complete binary tree in which every parent node is greater than or equal to its children.

Swap the root element with the last element.

Reduce the heap size.

Apply heapify to restore the Max Heap property.

Repeat until all elements are sorted.

3. Pseudocode

HEAP_SORT(arr)

    n = length(arr)

    BUILD_MAX_HEAP(arr)

    FOR i = n-1 DOWN TO 1

        SWAP arr[0] AND arr[i]

        HEAPIFY(arr, i, 0)

END


HEAPIFY(arr, n, i)

    largest = i

    left = 2*i + 1

    right = 2*i + 2

    IF left < n AND arr[left] > arr[largest]
        largest = left

    IF right < n AND arr[right] > arr[largest]
        largest = right

    IF largest != i

        SWAP arr[i] AND arr[largest]

        HEAPIFY(arr, n, largest)

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

Space Complexity: O(log n) for the recursive heapify implementation.

5. Sample Input / Output

Input:

Enter array elements: 12 11 13 5 6 7

Output:

Sorted array: [5, 6, 7, 11, 12, 13]



7. Experimental Results

The program successfully sorts the array using a Max Heap. The largest element is repeatedly extracted and placed at the end of the array until the complete array becomes sorted.

8. Learning Outcomes

Understood the Heap data structure.

Learned Max Heap construction.

Understood heapify operations.

Learned Heap Sort and its complexity.


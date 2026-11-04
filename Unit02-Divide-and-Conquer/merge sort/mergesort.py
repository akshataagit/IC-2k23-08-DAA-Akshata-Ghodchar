
# Merge Sort using Divide and Conquer

def merge(arr, left, mid, right):

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merge two sorted arrays
    while i < len(left_arr) and j < len(right_arr):

        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1

        else:
            arr[k] = right_arr[j]
            j += 1

        k += 1

    # Copy remaining elements
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):

    if left < right:

        # Divide
        mid = (left + right) // 2

        # Sort left half
        merge_sort(arr, left, mid)

        # Sort right half
        merge_sort(arr, mid + 1, right)

        # Combine
        merge(arr, left, mid, right)


# Main program
arr = list(map(int, input("Enter array elements: ").split()))

merge_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)

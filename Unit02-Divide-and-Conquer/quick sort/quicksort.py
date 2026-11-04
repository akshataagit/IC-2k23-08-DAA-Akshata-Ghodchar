
# Quick Sort using Divide and Conquer

def partition(arr, low, high):

    # Select last element as pivot
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):

    if low < high:

        # Divide using partition
        pi = partition(arr, low, high)

        # Sort left partition
        quick_sort(arr, low, pi - 1)

        # Sort right partition
        quick_sort(arr, pi + 1, high)


# Main program
arr = list(map(int, input("Enter array elements: ").split()))

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)

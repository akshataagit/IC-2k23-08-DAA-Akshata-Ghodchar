
# Binary Search using Divide and Conquer

def binary_search(arr, target, low, high):

    # Base condition
    if low > high:
        return -1

    # Divide
    mid = (low + high) // 2

    # Check middle element
    if arr[mid] == target:
        return mid

    # Conquer
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)

    else:
        return binary_search(arr, target, low, mid - 1)


# Main program
arr = list(map(int, input("Enter sorted array elements: ").split()))

target = int(input("Enter element to search: "))

result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

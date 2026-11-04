
# Maximum and Minimum using Divide and Conquer

def max_min(arr, low, high):

    # Only one element
    if low == high:
        return arr[low], arr[low]

    # Two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]

    # Divide the array
    mid = (low + high) // 2

    # Find max and min in left half
    max1, min1 = max_min(arr, low, mid)

    # Find max and min in right half
    max2, min2 = max_min(arr, mid + 1, high)

    # Combine results
    maximum = max(max1, max2)
    minimum = min(min1, min2)

    return maximum, minimum


# Main program
arr = list(map(int, input("Enter array elements: ").split()))

maximum, minimum = max_min(arr, 0, len(arr) - 1)

print("Maximum element:", maximum)
print("Minimum element:", minimum)

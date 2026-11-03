# Program to analyze binary search complexity

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


n = int(input("Enter number of elements: "))

arr = list(range(1, n + 1))

# Best case: middle element
best_target = arr[n // 2]

# Worst-style case: last element
worst_target = arr[-1]

# Unsuccessful search
missing_target = n + 1

print("\nBest Case:")
index, count = binary_search(arr, best_target)
print("Target:", best_target)
print("Index:", index)
print("Comparisons:", count)

print("\nWorst-Style Case:")
index, count = binary_search(arr, worst_target)
print("Target:", worst_target)
print("Index:", index)
print("Comparisons:", count)

print("\nUnsuccessful Search:")
index, count = binary_search(arr, missing_target)
print("Target:", missing_target)
print("Index:", index)
print("Comparisons:", count)

print("\nTime Complexity Analysis:")
print("Best Case: O(1)")
print("Average Case: O(log n)")
print("Worst Case: O(log n)")
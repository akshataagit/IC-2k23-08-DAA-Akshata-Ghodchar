
import time
import random
import csv
import matplotlib.pyplot as plt
import math


# ---------------- LINEAR SEARCH ----------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---------------- BINARY SEARCH ----------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ---------------- BUBBLE SORT ----------------
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---------------- EXECUTION TIME ----------------
def measure_time(function, *args):
    start = time.perf_counter()
    function(*args)
    end = time.perf_counter()

    return end - start


# ---------------- MAIN ANALYZER ----------------
def main():

    input_sizes = [100, 500, 1000, 2000, 5000]

    results = []

    print("\nALGORITHM PERFORMANCE ANALYZER")
    print("--------------------------------")

    for n in input_sizes:

        arr = [random.randint(1, 10000) for _ in range(n)]
        sorted_arr = sorted(arr)
        target = random.choice(arr)

        # Measure execution time
        linear_time = measure_time(
            linear_search, arr, target
        )

        binary_time = measure_time(
            binary_search, sorted_arr, target
        )

        bubble_time = measure_time(
            bubble_sort, arr
        )

        merge_time = measure_time(
            merge_sort, arr
        )

        # Theoretical complexity values
        theoretical_linear = n
        theoretical_binary = math.log2(n)
        theoretical_bubble = n ** 2
        theoretical_merge = n * math.log2(n)

        results.append([
            n,
            linear_time,
            binary_time,
            bubble_time,
            merge_time,
            theoretical_linear,
            theoretical_binary,
            theoretical_bubble,
            theoretical_merge
        ])

        print("\nInput Size:", n)
        print("Linear Search:", round(linear_time, 6), "seconds")
        print("Binary Search:", round(binary_time, 6), "seconds")
        print("Bubble Sort:", round(bubble_time, 6), "seconds")
        print("Merge Sort:", round(merge_time, 6), "seconds")

    # ---------------- SAVE CSV ----------------
    with open("algorithm_results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Input Size",
            "Linear Search Time",
            "Binary Search Time",
            "Bubble Sort Time",
            "Merge Sort Time",
            "Linear O(n)",
            "Binary O(log n)",
            "Bubble O(n^2)",
            "Merge O(n log n)"
        ])

        writer.writerows(results)

    # ---------------- EXPERIMENTAL GRAPH ----------------
    sizes = [row[0] for row in results]

    plt.figure(figsize=(10, 6))

    plt.plot(sizes, [row[1] for row in results],
             marker='o', label="Linear Search")

    plt.plot(sizes, [row[2] for row in results],
             marker='o', label="Binary Search")

    plt.plot(sizes, [row[3] for row in results],
             marker='o', label="Bubble Sort")

    plt.plot(sizes, [row[4] for row in results],
             marker='o', label="Merge Sort")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (Seconds)")
    plt.title("Experimental Algorithm Performance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("experimental_graph.png")
    plt.show()

    # ---------------- THEORETICAL GRAPH ----------------
    n_values = sizes

    plt.figure(figsize=(10, 6))

    plt.plot(n_values, n_values,
             marker='o', label="O(n)")

    plt.plot(n_values, [math.log2(n) for n in n_values],
             marker='o', label="O(log n)")

    plt.plot(n_values, [n**2 for n in n_values],
             marker='o', label="O(n²)")

    plt.plot(n_values, [n * math.log2(n) for n in n_values],
             marker='o', label="O(n log n)")

    plt.xlabel("Input Size")
    plt.ylabel("Theoretical Growth")
    plt.title("Theoretical Time Complexity Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("theoretical_graph.png")
    plt.show()

    print("\n--------------------------------")
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("Results saved in algorithm_results.csv")
    print("Experimental graph saved.")
    print("Theoretical graph saved.")


if __name__ == "__main__":
    main()

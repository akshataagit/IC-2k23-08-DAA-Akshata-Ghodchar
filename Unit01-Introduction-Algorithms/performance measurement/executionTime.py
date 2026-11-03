# Performance analysis of iterative and recursive binary search

import time
import csv
import random
import statistics
import matplotlib.pyplot as plt


# Iterative Binary Search
def iterative_search(arr, target):

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


# Recursive Binary Search
def recursive_search(arr, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, high)

    else:
        return recursive_search(arr, target, low, mid - 1)


# Function to calculate average execution time
def measure_time(function, arr, target):

    times = []

    for i in range(30):

        start = time.perf_counter()

        function(arr, target)

        end = time.perf_counter()

        times.append(end - start)

    return statistics.mean(times) * 1000000


# Different input sizes
sizes = [100, 1000, 5000, 10000, 50000, 100000]

iterative_times = []
recursive_times = []

results = []

for n in sizes:

    arr = list(range(n))

    target = random.choice(arr)

    # Measure iterative search
    it_time = measure_time(
        iterative_search, arr, target
    )

    # Measure recursive search
    rec_time = measure_time(
        lambda a, x: recursive_search(a, x, 0, len(a)-1),
        arr,
        target
    )

    iterative_times.append(it_time)
    recursive_times.append(rec_time)

    results.append([n, it_time, rec_time])

    print("Input Size:", n)
    print("Iterative Time:", round(it_time, 3), "microseconds")
    print("Recursive Time:", round(rec_time, 3), "microseconds")
    print("-----------------------------")


# Store results in CSV file
with open("performance_results.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Input Size",
        "Iterative Time (microseconds)",
        "Recursive Time (microseconds)"
    ])

    writer.writerows(results)


# Generate performance graph
plt.plot(
    sizes,
    iterative_times,
    marker='o',
    label="Iterative Binary Search"
)

plt.plot(
    sizes,
    recursive_times,
    marker='s',
    label="Recursive Binary Search"
)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (Microseconds)")

plt.title("Performance Comparison of Binary Search")

plt.legend()
plt.grid(True)

plt.savefig("performance_graph.png")

plt.show()

print("Results saved in performance_results.csv")
print("Graph saved as performance_graph.png")
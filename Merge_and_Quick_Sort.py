import random
import time
import tracemalloc
import matplotlib.pyplot as plt

# -----------------------------------------
# Merge Sort
# -----------------------------------------

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# -----------------------------------------
# Quick Sort
# -----------------------------------------

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]

    middle = [x for x in arr if x == pivot]

    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# -----------------------------------------
# Performance Testing
# -----------------------------------------

def test_algorithm(sort_function, data):

    tracemalloc.start()

    start = time.perf_counter()

    sort_function(data.copy())

    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    execution_time = end - start

    memory_used = peak / 1024

    return execution_time, memory_used


# -----------------------------------------
# Dataset Generation
# -----------------------------------------

SIZE = 10000

sorted_data = list(range(SIZE))

reverse_data = list(range(SIZE, 0, -1))

random_data = random.sample(range(SIZE), SIZE)


datasets = {
    "Sorted": sorted_data,
    "Reverse": reverse_data,
    "Random": random_data
}


results = []

print("="*70)

print("{:<12} {:<15} {:<15} {:<15}".format(
    "Dataset",
    "Algorithm",
    "Time (sec)",
    "Memory (KB)"
))

print("="*70)


merge_times = []
quick_times = []

dataset_names = []


for name, data in datasets.items():

    t, m = test_algorithm(merge_sort, data)

    merge_times.append(t)

    print("{:<12} {:<15} {:<15.6f} {:<15.2f}".format(
        name,
        "Merge Sort",
        t,
        m
    ))

    t2, m2 = test_algorithm(quick_sort, data)

    quick_times.append(t2)

    print("{:<12} {:<15} {:<15.6f} {:<15.2f}".format(
        "",
        "Quick Sort",
        t2,
        m2
    ))

    dataset_names.append(name)

print("="*70)


# -----------------------------------------
# Execution Time Graph
# -----------------------------------------

plt.figure(figsize=(8,5))

plt.plot(dataset_names, merge_times, marker='o')

plt.plot(dataset_names, quick_times, marker='o')

plt.title("Execution Time Comparison")

plt.xlabel("Dataset")

plt.ylabel("Time (seconds)")

plt.legend(["Merge Sort","Quick Sort"])

plt.grid(True)

plt.savefig("execution_time.png")

plt.show()
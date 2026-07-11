# Assignment 2: Analyzing and Implementing Divide-and-Conquer Algorithms

**Name:** Bilal Khalid

**Course:** Algorithms and Data Structures (MSCS-532-B01)

**Assignment:** Assignment 2

---

# Project Description

This project demonstrates the implementation and comparison of two divide-and-conquer sorting algorithms:

- Merge Sort
- Quick Sort

The algorithms are implemented in Python and compared using different datasets to evaluate their performance.

The comparison includes:

- Execution Time
- Memory Usage
- Performance on different input datasets

---


# Requirements

The program requires Python 3.14.2.

Install the required library before running the program:

```bash
pip install matplotlib
```

The following Python libraries are used:

- random
- time
- tracemalloc
- matplotlib

---

# Datasets Used

The algorithms are tested using three different datasets containing 10,000 integers.

1. **Sorted Dataset**
   - Numbers arranged in ascending order.

2. **Reverse Sorted Dataset**
   - Numbers arranged in descending order.

3. **Random Dataset**
   - Randomly generated numbers.

---

# Algorithms Implemented

## Merge Sort

Merge Sort divides the input array into two equal halves, recursively sorts each half, and then merges the sorted halves into a single sorted array.

Average Time Complexity:

```
Θ(n log n)
```

Worst Case:

```
O(n log n)
```

Best Case:

```
Ω(n log n)
```

---

## Quick Sort

Quick Sort selects a pivot element, partitions the array around the pivot, and recursively sorts the left and right partitions.

Average Time Complexity:

```
Θ(n log n)
```

Worst Case:

```
O(n²)
```

Best Case:

```
Ω(n log n)
```

---

# Performance Comparison

The program compares Merge Sort and Quick Sort using:

- Execution Time (seconds)
- Peak Memory Usage (KB)

An execution time graph is automatically generated after the program finishes.

The graph is:

<img width="752" height="474" alt="image" src="https://github.com/user-attachments/assets/7aafb920-5d00-4a9f-a000-2595886de561" />


---

# Output

The program displays a comparison table as following:

<img width="493" height="168" alt="image" src="https://github.com/user-attachments/assets/19fc46be-7440-4861-81a5-022068f23b38" />


---

# Conclusion

Both Merge Sort and Quick Sort efficiently sort large datasets using the divide-and-conquer approach.

Merge Sort provides consistent performance for all input types, while Quick Sort generally executes faster and uses less memory when balanced partitions are achieved.

---

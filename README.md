# Sorting Algorithms with Strategy Pattern

An implementation of the lassic sorting algorithms in Python, demonstrating the Strategy design pattern.

## Algorithms Implemented

- **Bubble Sort**: Compares adjacent elements and swaps them if they're in the wrong order. Optimized with early exit when the list is already sorted.
- **Insertion Sort**: Builds the sorted array one element at a time by inserting each element into its correct position.
- **Selection Sort**: Finds the minimum element from the unsorted portion and swaps it with the first unsorted element.
- **Quick Sort**:  Selects a pivot element and partitions the array into elements less than, equal to, and greater than the pivot, then recursively sorts each partition.

### Flexible Function-Based Design
- This implementation demonstrates Python's first-class functions - 
- Functions can be passed as arguments just like any other value. 
- This makes it easy to add new sorting algorithms without modifying any existing code.

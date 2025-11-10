from typing import Callable


def bubble_sort(data: list[int]) -> list[int]:
    """
    Compares adjacent elements and swaps them if they're in the wrong order.
    """

    data = data.copy()
    list_length = len(data)

    for pass_count in range(0, list_length - 1):

        isSwapped = False
        unsorted_end_index = list_length - pass_count

        for comparison_index in range(0, unsorted_end_index - 1):
            current_value = data[comparison_index]
            next_value = data[comparison_index + 1]

            if current_value > next_value:
                data[comparison_index], data[comparison_index + 1] = (
                    next_value,
                    current_value,
                )
                isSwapped = True

        if not isSwapped:
            break

    return data


def insertion_sort(data: list[int]) -> list[int]:
    """
    Builds the sorted array one element at a time by inserting each element into its correct position.
    """

    data = data.copy()
    list_length = len(data)

    for current_index in range(1, list_length):

        key = data[current_index]
        scan_index = current_index - 1

        while scan_index >= 0 and data[scan_index] > key:
            data[scan_index + 1] = data[scan_index]
            scan_index -= 1

        data[scan_index + 1] = key

    return data


def selection_sort(data: list[int]) -> list[int]:
    """
    Finds the minimum element from the unsorted portion and swaps it with the first unsorted element.
    """

    data = data.copy()
    list_length = len(data)

    for current_index in range(0, list_length - 1):

        min_value_index = current_index

        for scan_index in range(current_index + 1, list_length):
            if data[scan_index] < data[min_value_index]:
                min_value_index = scan_index

        data[current_index], data[min_value_index] = (
            data[min_value_index],
            data[current_index],
        )

    return data


SortFn = Callable[[list[int]], list[int]]


def context(strategy: SortFn, data: list[int]) -> list[int]:
    return strategy(data)  # pass_count = 0


def main() -> None:
    print(context(bubble_sort, [8, 4, 1, 3, 9]))
    print(context(insertion_sort, [8, 4, 1, 3, 9]))
    print(context(selection_sort, [8, 4, 1, 3, 9]))


if __name__ == "__main__":
    main()

def count_unique_values(values: list) -> int:
    """
    A function, which accepts a sorted array, and counts the unique values in the array.
    (There can be negative numbers in the array, but it will always be sorted).

    Time Complexity - O(n)
    Space Complexity - O(n)
    """
    if len(values) == 0:
        return 0

    i: int = 0
    for j in range(1, len(values)):
        if values[i] != values[j]:
            i = i + 1
            values[i] = values[j]

    return i + 1


print(count_unique_values([1, 1, 1, 1, 1, 2]) == 2)  # True
print(count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]) == 7)  # True
print(count_unique_values([]) == 0)  # True
print(count_unique_values([-2, -1, -1, 0, 1]) == 4)  # True

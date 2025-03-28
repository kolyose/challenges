def average_pair(values: list, average: float) -> bool:
    """
    Implement a function, that accepts a sorted array of integers and a target average,
    and determines if there is a pair of values in the array where the average of the pair equals the target average.
    (There may be more than one pair that matches the average target).

    Time: O(N)
    Space: O(1)

    Arguments:
      - values: list - a sorted list of interger numbers to search in
      - average: float - an average number with floating point to compare with

    Returns:
      True - if there's a pair of numbers with matching average, otherwise - False
    """
    if len(values) < 2 or average % 0.5 != 0:
        return False

    left = 0
    right = len(values) - 1

    while right > left:
        avg = (values[left] + values[right]) / 2
        if avg > average:
            right = right - 1
        elif avg < average:
            left = left + 1
        else:
            return True

    return False

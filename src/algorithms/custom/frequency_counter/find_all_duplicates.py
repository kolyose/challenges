def find_all_duplicates(values: list) -> list:
    """
    Implement a function to find all duplicates in a list.

    Time: O(N)
    Space: O(1)

    Arguments:
      - values: list - a sorted list of positive integers (some elements appear twice and others appear once)

    Returns:
      list - of duplicates found
    """
    if len(values) < 2:
        return []

    duplicates: dict = {}
    for value in values:
        duplicates[value] = 1 if not duplicates.get(value) else duplicates[value] + 1

    return [key for key, value in duplicates.items() if value > 1]

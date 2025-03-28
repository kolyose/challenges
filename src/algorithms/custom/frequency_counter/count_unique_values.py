def count_unique_values(values: list) -> int:
    if len(values) == 0:
        return 0

    unique_values: dict = {}

    for value in values:
        unique_values[value] = value

    return len(unique_values)

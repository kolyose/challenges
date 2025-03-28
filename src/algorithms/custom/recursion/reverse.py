def reverse(s: str) -> str:
    """
    Implement a function which accepts a string and returns a new string in reverse.
    """
    if len(s) == 1:
        return s

    return s[-1] + reverse(s[:-1])

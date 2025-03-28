def are_there_duplicates(*args):
    if len(args) < 2:
        return False

    unique_chars: dict = {}
    for char in args:
        if unique_chars.get(char):
            return True

        unique_chars[char] = char

    return False

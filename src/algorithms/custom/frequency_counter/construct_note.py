def construct_note(message: str, letters: str) -> bool:
    required_letters: dict = {}

    for char in message:
        count = required_letters.get(char)
        required_letters[char] = 1 if not count else count + 1

    for char in letters:
        count = required_letters.get(char)
        if count is not None:
            required_letters[char] = count - 1

    return not any([count != 0 for count in required_letters.values()])

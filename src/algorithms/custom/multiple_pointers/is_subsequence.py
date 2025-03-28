def is_subsequence(word1: str, word2: str) -> bool:
    """
    Implement a function which takes in two strings and checks
    whether the characters in the first string appear somewhere in the second string, without their order changing.

    Time Complexity - O(N + M)
    Space Complexity - O(1)

    Arguments:
        - word1 : str - a sequence of characters to look for
        - word2 : str - the target sequence to look in

    Returns:
    True if all the characters from the 1st sequence are included into the 2nd one in the same order, otherwise - False
    """
    len1 = len(word1)
    len2 = len(word2)

    if len2 < len1:
        return False

    left: int = 0
    right: int = 0

    while left < len1 and right < len2:
        if word1[left] == word2[right]:
            left = left + 1

        right = right + 1

    return left == len1

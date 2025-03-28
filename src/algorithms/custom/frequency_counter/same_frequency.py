def same_frequency(num1: int, num2: int):
    str1 = str(num1)
    str2 = str(num2)

    if len(str1) != len(str2):
        return False

    count_by_digit: dict = {}
    for i in range(len(str1)):
        char = str1[i]
        count = count_by_digit.get(char)
        count_by_digit[char] = 1 if count is None else count + 1

        char = str2[i]
        count = count_by_digit.get(char)
        count_by_digit[char] = -1 if count is None else count - 1

    return not any([count != 0 for count in count_by_digit.values()])

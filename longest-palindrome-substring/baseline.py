def check_palindrome(string) -> bool:
    half_length = len(string) // 2
    return string[:half_length] == string[:-half_length-1:-1]


def lps_baseline(string: str) -> str:
    # O(length ^ 3)
    length = len(string)
    max_length = 0
    max_index = (0, 1)
    for st in range(length):
        for ed in range(st + max_length + 1, length):
            if check_palindrome(string[st: ed]):
                max_length = ed - st
                max_index = (st, ed)

    return string[max_index[0]:max_index[1]]


if __name__ == '__main__':
    s = 'xyabxcxbaxy'
    print(lps_baseline(s))

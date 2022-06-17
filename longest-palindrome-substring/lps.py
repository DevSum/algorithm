def lps_square(string: str) -> str:
    # O(length ^ 2)
    flag_char = '\x00'
    str_with_flag_char = ''.join(['%c%c' % (c, flag_char) for c in string])
    length = len(str_with_flag_char)
    max_center_index = 0
    max_half_length = 1
    for center_index in range(length):
        half_length = 1
        while center_index - half_length >= 0 and center_index + half_length < length and str_with_flag_char[center_index - half_length] == str_with_flag_char[center_index + half_length]:
            half_length += 1
        if half_length > max_half_length:
            max_half_length = half_length
            max_center_index = center_index
    return str_with_flag_char[max_center_index - max_half_length + 1 : max_center_index + max_half_length].replace(flag_char, '')


if __name__ == '__main__':
    s1 = 'xyabxcxbaxy'
    print(lps_square(s1))
    s2 = 'xyabxxbaxy'
    print(lps_square(s2))
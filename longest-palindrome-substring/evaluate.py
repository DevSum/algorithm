from baseline import lps_baseline as lps
from lib import assert_palindrome


if __name__ == '__main__':
    s = 'xyabcbaxy'
    assert_palindrome(lps(s))
    s2 = 'xyabxxbaxy'
    assert_palindrome(lps(s))

def assert_palindrome(string: str):
    half_length = len(string) // 2
    assert string[:half_length] == string[:-half_length-1:-1]

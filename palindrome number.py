def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
print(is_palindrome(121))
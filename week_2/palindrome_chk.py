input = "abcba"

# without recursive function

# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n - i - 1]:
#             return False
#     return True

# with recursive function

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))

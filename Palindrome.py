# def check_palindrom(s):
#     if s==s[::-1]:
#         print("word is palindrome");
#     else:
#         print("word is not palindrome")
#
# check_palindrom("radar");
def is_palindrome(s):
   return s==s[::-1]
print(is_palindrome("radar"));
print(is_palindrome("road"));
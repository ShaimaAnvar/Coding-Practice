def is_palindrome(num): #121
    num_str= str(num); #"121"
    return num_str==num_str[::-1];

number=122;
if is_palindrome(number):
    print("number is palindrome");
else:
    print("number is not palindrome")
def is_palindrome(string):
    string = string.lower()
    if(string==string[::-1]):
        print(string.capitalize(), "is a palindrome")
    else:
        print(string.capitalize(), "isn't a palindrome")

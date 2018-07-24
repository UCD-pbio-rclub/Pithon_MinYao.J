def is_palindrome():
    while True:
        print('Welcome to is_palindrome.')
        user_input = input('Please enter a potential palindome: ')
        user_input = user_input.lower()
        if(user_input==user_input[::-1]):
            print(user_input.capitalize(), "is a palindrome")
        else:
            print(user_input.capitalize(), "isn't a palindrome")
        user_input = input('Do another search? [y/n]: ').lower()
        user_input = user_input or 'y'
        if user_input == 'n':
            break
            

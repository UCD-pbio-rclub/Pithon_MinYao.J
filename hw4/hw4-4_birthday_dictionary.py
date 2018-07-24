birthday = {'Yulia Zagoruychenko' : '09/11/1981',
            'Riccardo Cocchi' : '12/07/1977',
            'Joanna Leunis' : '05/22/1981',
            'Michael Malitowski' : '05/28/1980',
            'Bryan Watson' : '04/18/1969'}


def Champions_birthday_dictionary():
    while True:
        print('Welcome to the birthday dictionary.')
        print('We know the birthdays of 1999~2017 Professional Latin World Champions')
        Champions_name_list()
        print("Who's birthday do you want to look up?")
        user_input = input('Please enter a full name: ')
        if user_input in birthday:
            print(user_input,"'s birthday is",birthday.get(user_input))
        else:
            print('Name cannot be found')
        user_input = input('Do another search? [y/n]: ').lower()
        user_input = user_input or 'y'
        if user_input == 'n':
            break

def Champions_name_list():
    print('Names of Champions in the list:')
    for key in birthday.keys():
        print(key)          
        
        

        
    

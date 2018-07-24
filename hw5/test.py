import re

my_string = 'This is my string which contains words and numbers like : 123'


new_string = re.sub(' ', '_' , my_string)
new_string2 = re.sub(':', '_' , new_string)
new_string2
print(new_string2)



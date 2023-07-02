#password generator
#version 1, 7/1/23
#----------------------------------------------------------------------


import random
import string

#collect all potential characters
letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_lower = letters_upper.lower()
numbers = '0123456789'
symbols = string.punctuation

#combine all potential characters
all = letters_lower + letters_upper + numbers + symbols

#generate initial password of 20 characters
def password_create():
    
    print('Welcome to the Password Generator. You will now be given a password of 20 characters. Keep it secure. Your password is: ')
    password = ''
    while len(password) < 20:
        password += random.choice(all)

    #reverse password for added complexity
    password_reversed = password[::-1] 
    return password_reversed

print(password_create())



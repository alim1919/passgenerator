
#import the necessary modules!

import random
import string

print('hello, Welcome to Password generator!')

#input the length of password

user_input = int(input('\nEnter the length of password: '))

#define and combine data 

all = string.ascii_letters + string.digits + string.punctuation

#use random 

password = "".join(random.sample(all,user_input))




#print the password

print(password)

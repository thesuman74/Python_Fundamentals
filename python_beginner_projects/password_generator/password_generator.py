import random 
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
all_characters = lower + upper + digits + punctuation

#set password length 

password_length = int(input("Enter the length of password:"))


#loop through each character 
password = ''
for _ in range(password_length):
    password = ''.join([password, random.choice(all_characters)])


print(f"Generated password : {password}" )
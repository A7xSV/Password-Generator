import random

print('----Password Generator----')

choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('How many passwords do you need ? -> ')
number = int(number)

length = input('The length of the password(s) needed ? -> ')
length = int(length)

print('\nGenerating...')
print('\nHere are your passwords : ')

for i in range(number):
  password = ''
  for j in range(length):
    password += random.choice(choices)
  print(password)

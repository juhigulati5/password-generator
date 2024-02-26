#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Easy Level

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
password = []

for i in range(0,nr_letters):
  rand_letters = random.randint(0,51)
  letters_choose = letters[rand_letters]
  password.append(letters_choose)


nr_symbols = int(input("How many symbols would you like?\n"))
for i in range(0,nr_symbols):
  rand_symbols = random.randint(0,9)
  symbols_choose = symbols[rand_symbols]
  password.append(symbols_choose)

nr_numbers = int(input("How many numbers would you like?\n"))
for i in range(0,nr_numbers):
  rand_numbers = random.randint(0,8)
  numbers_choose = numbers[rand_numbers]
  password.append(numbers_choose)

#str_password = ''.join(password)
#print(str_password)
  
#Hard Level - Order of characters randomised:

random.shuffle(password)
print(''.join(password))

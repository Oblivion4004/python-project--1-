import random
print("Welcome to pass word generetor")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbols would you like in your password\n"))
nr_numbers = int(input("how many numbers would you like in your password\n"))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-="
numbers = "0123456789"
password_list = []
for char in range (0 , nr_letters):
    password_list += random.choice(letters)

for char in range (0, nr_symbols):
        password_list += random.choice(symbols)

for char in range (0 , nr_numbers):
        password_list += random.choice(numbers)


random.shuffle(password_list)

password = "" . join(password_list)
print(f"Your password is : {password}")
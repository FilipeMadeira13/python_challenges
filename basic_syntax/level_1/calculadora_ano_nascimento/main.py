CURRENT_YEAR = 2023

name = input('Enter your name: ').capitalize().strip()
age_input = input('Enter your age: ')

try:
    age = int(age_input)
    year_of_birth = CURRENT_YEAR - age
    
except ValueError:
    print('Invalid input! Please enter only integers.')
else:
    print(f'Hello {name}! You were born in {year_of_birth}.')
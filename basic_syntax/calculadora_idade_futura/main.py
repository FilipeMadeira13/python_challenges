name = input("Name: ")
try:
    age = int(input("Age: "))
    print(f"Hello {name}! Next year, you will be {age + 1} years old.")
except ValueError:
    print("Invalid age! Please enter an integer.")
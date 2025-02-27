try:
    celsius = float(input("Temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")
except ValueError:
    print("Invalid temperature! Please enter a number.")
# Program to check if it's suitable for light clothes

temp = float(input("Enter temperature in C: "))

if temp > 25:
    print("Wear light clothes.")
elif temp >= 15:
    print("Maybe light clothes, but take a jacket.")
else:
    print("It's cold, wear warm clothes.")

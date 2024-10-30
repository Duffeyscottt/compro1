weight = int(input("Enter package weight in kilograms: "))
length = int(input("Enter package length in centimeters: "))
width = int(input("Enter package width in centimeters: "))
height = int(input("Enter package height in centimeters: "))
size = length * width * height

if weight > 27 and size > 100000:
    mess1 = "Too heavy and too large"
    print(mess1)
elif weight > 27 and size <= 100000:
    mess2 = "Too heavy"
    print(mess2)
elif weight <= 27 and size > 100000:
    mess3 = "Too large"
    print(mess3)
else:
    mess4 = "You're all good!"
    print(mess4)

input()
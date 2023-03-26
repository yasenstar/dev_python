# Purpose: convert between Degree Celsius (c) and Degree Fahrenheit (f)
# Formular:
#     f = c * 9 / 5 + 32
#     c = (f - 32) * 5 / 9
# Author: Yasen Zhao
# Date: 2023-03-26
# Version: 1.0

print("Please tell me what you want to convert to: (c or f)")

choice = input()

if choice == "c":
    f_degree = float(input("please tell me the degree Fahrenheit:"))
    print("the degree Fahreheit you input is: ", f_degree)
    print("the converted degree Celsius is: ", (f_degree - 32) * 5 / 9)
elif choice == "f":
    c_degree = float(input("please tell me the degree Celsius:"))
    print("the degree Celsius you input is: ", c_degree)
    print("the converted degree Fahrenheit is: ", c_degree * 9 / 5 + 32)
else:
    print("sorry, you type in something I don't understand, please try between c or f only!")

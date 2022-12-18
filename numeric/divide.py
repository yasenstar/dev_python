# divide

dividend = int(input("please input the first number: "))
divisor = int(input("please input the second number: "))

quotient = dividend // divisor

remainder = dividend % divisor

print("=" * 50)

print(dividend, "/", divisor, "=", quotient, "......", remainder)

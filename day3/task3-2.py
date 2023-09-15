number1 = input("Please enter the first number: ")
number2 = input("Please enter the second number: ")
sum = float(number1) + float(number2)

if sum.is_integer():
    sum = int(sum)
print("The sum of the two provided numbers is", sum)
try:
 number = int(input("Enter a whole number: "))
 data_type = type(number)
 print(f"The data type of {number} is {data_type}.")
except ValueError:
 print("Data type is not valid please enter a whole number")


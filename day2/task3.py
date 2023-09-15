number_str= input("enter a number:")
digit_sum=0

for char in number_str:
    if char.isdigit():
        digit_sum += int(char)
        
print("sum of digits is:", digit_sum)        


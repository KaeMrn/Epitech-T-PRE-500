import time

number = int(input("enter a number: "))
power = int(input("enter a power: "))

start_time = time.time()

def function(number, power):
    result = 1
    for _ in range (power):
        result *= number
    return result

result = function(number, power)
end_time = time.time()
excution_time = end_time - start_time
print("the result is: ", result)
print("excution time is: ", excution_time, "seconds")


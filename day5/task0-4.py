[x + 10 for x in [3, 2, 6, 7, 1, 4]]
#code ads ten to each element of the list

# Original list
my_list = [9, 4, 36, 49, 1, 16]

# Find the smallest and largest elements
smallest = min(my_list)
largest = max(my_list)
mylist7 = [x for x in my_list if x < 7]
my_listreversed = sorted(my_list, reverse=True)

# Display the results
print("Smallest element:", smallest)
print("Largest element:", largest)
print(mylist7)
print(my_listreversed)

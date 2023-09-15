Numbers = [1, 2, 3, 4, 5, 6]
print(Numbers[0])
print(Numbers[-1])
print(Numbers)

#delete last element and display the rest.
del Numbers[-1]
print(Numbers)

#insert number at the beginning of the lsit.
Numbers.insert(0, 0)
print(Numbers)

#display from second to fifth element.
print(Numbers[1:5])

#reverse list and display it.
reversed_list = Numbers[::-1]
print(reversed_list)

#add 17 elements to the list
Numbers.extend(list(range(1,18))) 
print(Numbers)


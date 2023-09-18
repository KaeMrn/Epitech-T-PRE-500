#this code uses the elements of the second list to extend the first list
my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list.extend( my_second_list )
print(my_first_list)

#this code adds the elements of the second list after those of the first

My_first_list = [7 , 8 , 9]
My_second_list = [4 , 5 , 6]
My_first_list = [* My_first_list , * My_second_list ]
print(My_first_list)
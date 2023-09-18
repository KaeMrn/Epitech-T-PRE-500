def bread () :
 print (" <////////// > ")
def lettuce () :
 print (" ~~~~~~~~~~~~ ")
def tomato () :
 print ("O O O O O O")
def ham () :
 print (" ============ ")
def veggies() : 
 print (" &&&&&&&&&&&&& ")


def sandwich() :
 bread()
 ham()
 ham()
 tomato()
 lettuce()
 bread()

def veggiesandwich() :
 bread()
 veggies()
 veggies()
 tomato()
 lettuce()
 bread()



Number = int(input("Please enter number of desired sandwiches: "))
Veggie = input("Do you want the vegetarian option? ")

if Veggie == "yes":
 for _ in range(Number): 
  veggiesandwich()
  print()
else:
 for _ in range(Number): 
  sandwich()
  print()
 
 



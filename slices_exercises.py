##print first three items in a list
foods =["pizza", "falafel", "carrot cake","cannoli", "ice cream"]
print("The first three items in the list are:,foods[:3]")

##print three items in a list from the middle
print("The first three items from the middle in the list are:,foods[1:4]")

##print the last three items in a list 
print("The last three items in the list are:,foods[-3:]")

##copy the list 
pizzas = ["peperoni", "margerita", "hawaian"]
friend_pizzas = pizzas[:]


##Add new ingredients in lists
pizzas.append("mushroom")
friend_pizzas.append("bbq chicken")
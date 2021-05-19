food = input("Enter 4 types of food: \n").split()
print(food)
foodremove=int(input("Which food would you like to remove?: 1/2/3/4 \n")) -1
food.remove(food[foodremove])
print(food)

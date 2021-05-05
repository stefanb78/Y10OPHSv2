cars = []
end = False
while not end:
      caradd=input("enter brand: \n")
      cars.append(caradd)
      if caradd == "x":
            end = True
            print("Exiting...")
print("In the list is ", cars)

party=input("Enter 3 people you would like to invite to the party: \n").split()
print(party)
while True:
      moreinvites=input("would you like to add another?: y/n \n").lower()
      if moreinvites == "y":
            addname=input("Enter Name \n")
            party.append(addname)
      elif moreinvites == "n":
            print(len(party))
            break

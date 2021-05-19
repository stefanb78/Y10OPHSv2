nums = []
count = 0

while True:
    n = int(input("Enter a number "))
    nums.append(n)
    count += 1

    if count == 3:
        delete = input("Keep last num? y or n ").lower()

        if delete == "n":
            nums.remove(nums[-1])
            break
        
        else:
            break
    
print(nums)

def add(numbers_to_add):
     sum = 0
     for i in range(1, numbers_to_add + 1):
         number = int(input(f"Enter {i} index ko number: "))
         sum += number
    
     return sum

print(add(3))

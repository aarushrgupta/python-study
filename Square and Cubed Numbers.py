
##for i in range(1,11):
##    (i)
##    sq_num = i * i
##    cu_num = i * i * i
##    #print(sq_num)
##    Square_numbers.append(sq_num)
##    Cubed_numbers.append(cu_num)
##




# LIST COMPRESENTION

Square_numbers = []
Cubed_numbers = []

Square_numbers = [i * i for i in range(1,11)]
Cubed_numbers = [i * i * i for i in range(1,11)]

print("normal")
print(Square_numbers)    
print(Cubed_numbers)

print("------------------------")
print("min")
print(min(Square_numbers))

print(min(Cubed_numbers))

print("------------------------")
print("max")
print(max(Square_numbers))

print(max(Cubed_numbers))

print("------------------------")
print("sum")
print(sum(Square_numbers))

print(sum(Cubed_numbers))

print("------------------------")



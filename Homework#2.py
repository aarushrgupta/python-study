Duplicates = [1,1,2,3,1,3,6,2,4,5,1,2,4,6,7,3,2]
new_list = []

for my_item in Duplicates:
    if not my_item in new_list:
        new_list.append(my_item)
print(new_list)
    
    

    

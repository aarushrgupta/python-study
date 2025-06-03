Reverse_list = ["ABC"]
#reverse_word = ""
empty_list = []

num = len(Reverse_list)
print(num)

num = len(Reverse_list) - 1
#print(reverse_word)
while (num >= 0):
    #print(Reverse_list[num])
    empty_list.append(Reverse_list[num])
    #reverse_word = Reverse_list[num]
    #print(reverse_word)
    num = num -1
print(empty_list)
#print(reverse_word)

def multiplication(num):
    num = int(input("Pick a number for your multiplication table: "))
   
    for num2 in range(1,13):
        print(str(num) + " x " + str(num2) + " = " + str(num * num2))
    
       



multiplication(5)
multiplication(7)
multiplication(8)
multiplication(3)

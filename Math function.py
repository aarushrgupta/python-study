def do_math(num1, num2, op):
    if op == "add":
        print(num1 + num2)
    elif op == "times":
        print(num1 * num2)

while True:
    first_num = int(input("Pick a number:  "))
    second_num = int(input("Pick a number:  "))
    op_val = input("Type 'add' or 'times':  ")
    do_math(first_num, second_num, op_val)

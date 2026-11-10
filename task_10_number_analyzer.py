
num_list =[]
i=0

print("Enter 10 integers: ")

while i < 10:
    try:   
        num = int(input ())
    except ValueError:
        print("Please Enter an integer: ")
        continue
    num_list.append(num)
    i += 1

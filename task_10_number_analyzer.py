
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

num_list.sort()
largest = num_list[-1]
smallest = num_list[0]
total = sum(num_list)
avg = sum(num_list) / len(num_list)
even_list = [num for num in num_list if num % 2 == 0]
odd_list = [num for num in num_list if num % 2 != 0]
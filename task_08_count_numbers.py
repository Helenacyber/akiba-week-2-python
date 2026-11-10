#count numbers program
#This progarm asks the user for apositive number and 
# counts how many odd,even there are and find the sum

n = int(input('Enter a positive number: '))
if n <= 0:
    print('Please enter a positive number')
num_range = range(n)
even_list = []
odd_list = []
total_sum  =0

for num in num_range:
   total_sum += num
   if num % 2 == 0:
      even_list.append(num)
   else:
      odd_list.append(num)

print(f'The total Sum is : {total_sum}')
print(f'The total number of even numbers in the range is: {len(even_list)}')
print(f'The total number of odd numbers in the range is: {len(odd_list)}')
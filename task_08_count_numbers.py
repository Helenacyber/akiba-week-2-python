#count numbers
#This progarm asks the user for apositive number and 
# counts how many odd,even there are and find the sum

n = int(input('Enter a positive number: '))
if n <= 0:
    print('Please enter a positive number')
num_range = range(n)
even_list = []
odd_list = []
total_sum  = 0

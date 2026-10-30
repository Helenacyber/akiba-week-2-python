word = input('Enter a word: ')
word_list = []
for letter in word:
   word_list.append(letter)

reversed_word = ''
reversed_word = reversed_word.join(reversed(word_list))

if reversed_word.lower() == word.lower():
   print('The word you entered is a palindrome.')
else:
   print('The word you entered is not a palindrome.')
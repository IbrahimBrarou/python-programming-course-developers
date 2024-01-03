numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]


first1, second1, third1 = numbers
first2, second2, *other = numbers  # other is a list of remaining items
first2, *other, last = numbers

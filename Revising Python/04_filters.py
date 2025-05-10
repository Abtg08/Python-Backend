#Map function
numbers = [1,2,3]
double = lambda x: x * 2
print(f'Map: {list(map(double, numbers))}')

#Lambda function
numbers = [1,2,3]
print(f'Lambda: {list(map(lambda x: x * 2, numbers))}')

#Filter function
numbers = [1,2,3,4,5]
even = lambda x: x % 2 == 0
print(f'Filter: {list(filter(even, numbers))}')

#Reduce function
from functools import reduce
# grocery_list = {'milk': 40,'bread': 20,'muskmelon': 30,'banana': 10}
# total = reduce(lambda x,y: x + y, grocery_list)
grocery_list = [
  ('milk', 40),('bread', 20),('muskmelon', 30),('banana', 10)
]
total = reduce(lambda x,y: x[1] + y[1], [item[1] for item in grocery_list])
print(f'Reduce: {total}')
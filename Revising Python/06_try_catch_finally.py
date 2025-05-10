# try:
#   result = 10 / 0
# except ZeroDivisionError:
#   print('Can\'t divide by zero man!')
# finally:
#   result= 1

# print(result)

try:
  raise Exception('An Error!')
except Exception as error:
  print(error)
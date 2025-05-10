class Dog:
  def eat(self):
    print('Dog eats dog food')

class Cat:
  def eat(self):
    print('Cat eats cat food')

animal1= Dog()
animal2= Cat()

for i in (animal1, animal2):
  i.eat()
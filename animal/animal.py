class Animal(object):
 def __init__(self,name,health):
  self.name = name
  self.health = health

 def walk(self):
  self.health -= 1
  return self

 def run(self):
  self.health -= 5
  return self

 def display_health(self):
  print (self.health)


animal1 = Animal("cat",4)
animal1.walk()
animal1.walk()
animal1.walk()
animal1.run()
animal1.run()
animal1.display_health()

class Dog(Animal):
 def __init__(self):
  self.health = 150

 def pet(self):
  self.health += 150


dog1 = Dog()
dog1.walk()
dog1.walk()
dog1.walk()
dog1.run()
dog1.run()
dog1.pet()
dog1.display_health()


class Dragon(Animal):
 def __init__(self):
  self.health = 170

 def fly(self):
  self.health -= 10

 def display_health(self):
  super(Dragon,self).display_health()
  print ("I am a Dragon")

dragon1 = Dragon()
dragon1.fly()
dragon1.display_health()


class Snake(Animal):
 def __init__(self):
  self.health = 100

 def crawl(self):
  self.health += 20

 def display_health(self):
  super(Snake,self).display_health() # calls parent class Animal method named display_health
  print ("I am a snake")


snake1 = Snake()
snake1.crawl()
snake1.display_health()

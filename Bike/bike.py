#Declare a class called Bike
class Bike(object):
 def __init__(self,price,max_speed):
  self.price = price
  self.speed = max_speed
  self.miles = 0

 def displayInfo(self):
  print ("Price is"+ str(self.price))
  print ("Maximum speed is"+ self.speed)
  print ("Total miles is" + str(self.miles))

 def ride(self):
  self.miles += 10

 def reverse(self):
  self.miles = self.miles - 5


bike1 = Bike(300,"30mph")
bike2 = Bike(400,"25mph")
bike3 = Bike(200,"20mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()


bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()

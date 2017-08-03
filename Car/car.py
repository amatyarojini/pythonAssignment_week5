# declare a class named Car
class Car(object):
 def __init__(self,price,speed,fuel,mileage):

  self.price = price
  self.speed = speed
  self.fuel = fuel
  self.mileage = mileage
  self.tax = 0
  self.display_all()

 def display_all(self):
  print("reached inside display_all function")
  if self.price > 10000:
   self.tax = 0.15
  else:
   print ("reached inside else st")
   self.tax = 0.12

  print("Price: " + str(self.price))
  print("Speed: " + self.speed)
  print("Full: " + self.fuel)
  print("Mileage: " + self.mileage)
  print("Tax percentage: " + str(self.tax))


Car1 = Car(2000,"35mph","Full","15mpg")
Car2 = Car(2000,"5mph","Not Full","105mpg")
Car3 = Car(2000,"15mph"," Kind of Full","95mpg")
Car4 = Car(2000,"25mph","Full","25mpg")
Car5 = Car(2000,"45mph","Empty","25mpg")
Car6 = Car(20000000,"35mph","Empty","15mpg")

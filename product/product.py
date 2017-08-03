class Product(object):

 def __init__(self,price,itemName,itemId,weight,brand,desc):
  self.price = price
  self.itemName = itemName
  self.itemId = itemId
  self.weight = weight
  self.brand = brand
  self.desc = desc
  self.status = "for sale"
  self.tax = 0
  self.displayInfo()


 def displayInfo(self):
  self.addTax()
  self.returnItem()
  print ("Product Details:")
  print ("Item name :"+self.itemName)
  print ("Item Code :"+self.itemId)
  print ("price :"+str(self.price))
  print ("weight :"+self.weight)
  print ("status :"+self.status)


 def sellItem(self):
  self.status = "sold"

 def addTax(self):
  if self.price > 1000:
   self.tax = 0.15
  else:
   self.tax = 0.10
  self.price = self.price +self.price * self.tax
  return self
 def returnItem(self):
  if self.desc == "defective":
   self.status = "defective"
   self.price = 0
  elif self.desc == "box has been opened":
   self.status = "used"
   self.price = self.price - self.price * 0.2
  elif self.desc == "sold":
   self.sellItem()



product1 = Product(20.0,"Eyeliner","01","100gm","Covergirl","box has been opened")
product2 = Product(10.0,"Lipgloss","02","30gm","Maybellyn","defective")

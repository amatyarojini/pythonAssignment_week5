from Call import Call
class CallCenter(object):

 def __init__(self):
     self.list_of_callers = []
     self.queue = 0
     self.count = -1
     self.countCall = 0

 def add(self,call):
  self.list_of_callers.append(call)
  self.queue = len(self.list_of_callers)
  #print ("size is.........." + str(len(self.list_of_callers)))



 def remove(self):
  self.list_of_callers.pop(0)


 def info(self):
  for x in self.list_of_callers:
   print( x.caller_name,x.caller_number)
  print("total queue length is.........." + str(self.queue - (self.countCall)))
  #print (self.list_of_callers[3].caller_name)

 def removeCall(self,phNumber):
  for x in self.list_of_callers:
   self.count += 1
   if x.caller_number == phNumber:
    self.countCall += 1
    del self.list_of_callers[self.count]
    print("number found and entire call has been deleted")




call1 = Call(1,'Mark',"9841606066",'10','abc')
call2 = Call(2,'kevin',"98412115",'2','xyz')
call3 = Call(3,'John',"984111141",'3','asaf')
call4 = Call(4,'Anna',"984144163",'5','asdf')
callCenter = CallCenter()
callCenter.add(call1)
callCenter.add(call2)
callCenter.add(call3)
callCenter.add(call4)
callCenter.info()
#callCenter.remove()
callCenter.removeCall("984144163")
callCenter.info()

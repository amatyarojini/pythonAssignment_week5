class Call(object):
 def __init__(self,unique_id,caller_name,caller_number,time,reason):
  self.unique_id = unique_id
  self.caller_name = caller_name
  self.caller_number = caller_number
  self.time_of_call = time
  self.reason_of_call = reason

 def display(self):
  print("Caller Id is" + str(self.unique_id))
  print("Caller Name is" + self.caller_name)
  print("Caller Number is" + self.caller_number)
  print("Time of call  is" + self.time_of_call)
  print("Reason of call is" + self.reason_of_call)

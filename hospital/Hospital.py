from Patient import Patient
class Hospital(object):
 def __init__(self,hospitalName,capacity):
  self.list_of_patients = []
  self.hospitalName = hospitalName
  self.capacity = capacity
  self.count = -1

 def admit(self,patient):
  if len(self.list_of_patients) <  self.capacity:
   self.list_of_patients.append(patient)
   patient.bedNumber = input("Enter Bed Number: ")

  else:
   print("hospital is full")

 def patientInfo(self):
  for x in self.list_of_patients:
   print( x.id,x.name,x.allergies,x.bedNumber)

 def discharge(self,id):
  print("reached inside discharge method")
  for x in self.list_of_patients:
   self.count += 1
   if x.id == id:
    del self.list_of_patients[self.count]
    self.list_of_patients[self.count].bedNumber = "None"


patient1 = Patient(1,"jenny","fever")
patient2 = Patient(2,"Ross","Infection")
patient3= Patient(3,"Rosy","fever")

hospital = Hospital("Norvic Hospital",200)
hospital.admit(patient1)
hospital.admit(patient2)
hospital.admit(patient3)
hospital.patientInfo()
hospital.discharge(1)
hospital.patientInfo()

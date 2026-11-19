
import pyvisa

#Create Resource Manager
rm = pyvisa.ResourceManager("@py")

print("Resource Manager created successfully")

#Display VISA backend
print("Backend:", rm.visalib)

#Check backend type
print("Backend Type:", type(rm.visalib))

#Find available instruments
devices = rm.list_resources()

print("Available Instruments:", devices)

#Close Resource Manager
rm.close()



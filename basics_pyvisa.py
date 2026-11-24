
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





sim_rm = pyvisa.ResourceManager("@sim")
print("\nSimulated Resource Manager created")

sim_devices = sim_rm.list_resources()
print("Available Simulated Instruments:", sim_devices)


instrument_address="USB0::0x1111::0x2222::0x1234::0::INSTR"
instrument = sim_rm.open_resource(instrument_address)
print("\nSimulated Instrument Opened Successfully")
print("Instrument Address:", instrument.resource_name)
print("Timeout:", instrument.timeout, "milliseconds")
instrument.close()
print("Instrument connection closed successfully!")

instrument = sim_rm.open_resource(instrument_address)
print("\nInstrument opened for command communication")

instrument.write("*RST")
print("Reset command sent successfully")

instrument.write("*CLS")
print("Clear status command sent successfully")

instrument.close()
print("Instrument connection closed")

sim_rm.close()
#Close Resource Manager
rm.close()

print("\nProgram completed successfully")




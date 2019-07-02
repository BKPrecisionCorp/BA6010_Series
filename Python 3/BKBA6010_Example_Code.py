# This is example code for the BK Precision BA6010 Series
# A programming manual for the BK Precision BA6010 Series can be found at:
# https://bkpmedia.s3.amazonaws.com/downloads/programming_manuals/en-us/BA6010_Series_programming_manual.pdf



import visa
import time     #This is used for the sleep function (Delay)



print("This Script is made for the BKBA6010 Series Battery Analyzers")
manager = visa.ResourceManager()
li = manager.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which Device?: ")
batAn=manager.open_resource(li[int(choice)]) #creates an alias (variable) for the VISA resource name of a device
# we do this so we don't have to call that constantly. This is unique to a unit and changes depending on USB port used and serial number of a unit. 
# This will automatically detect connected devices and allows you to select the one you want to run the script on.


time.sleep(0.1)
batAn.write("DISPlay:PAGE MEASurement")                     # Display the Measurement Screen
batAn.write("function:impedance ZTD")                       # Set it to measure Impedance and Angle (In Degrees)
batAn.write("Func:IMP:RANG:auto on")                        # Auto ranges the impedance
batAn.write("function:vdc:range:auto on")                   # Auto ranges the voltage
batAn.write("aper fast,100")                                # Sets it to FAST read mode
batAn.write("TRIG:SOUR internal")                           # Sets to trigger mode to internal so it automatically takes measurements
time.sleep(1)

# Lets Set Up a BIN
batAn.write("DISPLAY:PAGE binsetup")                        # Display the Bin Setup Screen
batAn.write("BINSETUP: binmode abs")                        # Set binmode to absolute value mode
batAn.write("BINSETUP: compA on; COMPAREB ON")              # Turn on comparison of BINA and BINB, in this case, it's impedance and angle (degrees)
                                                            # These parameters and the accepted ranges below will change depending on mode set via the
                                                            # function:impedance command
batAn.write("binset:bina 1:1,-1")                           # Set BINA slot 1 to a maximum of 1 ohm and a minimum of -1 ohm
batAn.write("binsetup:BINB 1:80,60")                        # Set BINB slot 1 to a maximum of 80 degrees and a minimum of 60 degrees
batAn.write("binset:bina 2:15,-15")
batAn.write("binsetup:BINB 2:160,60")
batAn.write("binset:bina 3:5,0")
batAn.write("binsetup:BINB 3:190,175")                      # We set up 3 Bins, now lets use the compare mode.

batAn.write("DISPLAY:PAGE bcomp")                           # Display the Bin Compare Screen
batAn.write("Comp:bee off")                                 # Turn off terrible beeping
batAn.write("comparator:compmode compare")                  # set to compare mode
batAn.write("comp:loadbinno bin1")                          # load bin1
batAn.write("comp:stat on")                                 # enable
#----------------------------------------------------------------
# Calculate Series Resistance Given Each Load's Resistance
#----------------------------------------------------------------
'''
Series resistance is the sum of all resistors i.e. 25 + 25 + 10 = 60 ohms
'''

#----------------------------------------------------------------
# IMPORTS
#----------------------------------------------------------------
import sys


#----------------------------------------------------------------
# VARIABLES
#----------------------------------------------------------------
series_resistance = 0 
run = True

#----------------------------------------------------------------
# MAIN PROGRAM
#----------------------------------------------------------------

while run:
    try:
        resistorCount = int(input("Number of resistors: "))
        for x in range(resistorCount):
           resistor_value = int(input("Resistor Value: "))
           series_resistance = series_resistance + resistor_value
        print("Series Resistance = " , series_resistance , "Ohms")
        run_again = str(input("Run Again? Y/N   ").lower())
        if run_again == "n":
            run = False
        else:
            continue
    except KeyboardInterrupt:
        print("\nProgram Stopped")
        sys.exit()

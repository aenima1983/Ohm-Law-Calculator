#pvir calculator
#coded by aenima1983
import math
import time
def vir_calc():
    solve_for = input("which do you want to solve for?\n1. voltage\n2. resistance\n3. current\n4. equivalent resistance\n5. circuit\n\t> ")
    if solve_for == "voltage":
        current = float(input("current? "))
        resistance = float(input("resistance? "))
        voltage = resistance * current
        print(f"{voltage} volts\n")
    elif solve_for == "resistance":
        current = float(input("current? "))
        voltage = float(input("voltage? "))
        resistance = float(voltage / current)
        print(f"\n{resistance} Ohms\n")
        time.sleep(2)
    elif solve_for == "current":
        voltage = float(input("voltage? "))
        resistance = float(input("resistance? "))
        current = float(voltage / resistance)
        print(f"{current} amps\n")
        time.sleep(2)
    elif solve_for == "equivalent resistance":
        question = input("parallel or series? ")
        if question == "series":
            j = int(input("how many resistors, bro? "))
            resistorslist = []
            for i in range(0,j):
                resistorslist.append(int(input(f"resistor{i + 1} ")))
            #print(resistorslist)
            print(f"{math.fsum(resistorslist)} Ohms\n")
            time.sleep(2)
            return resistorslist
        elif question == "parallel":
            j = int(input("how many resistors, bro? "))
            resistorslist = []
            for i in range(0,j):
                resistorslist.append(1/(float(input(f"resistor{i + 1} "))))
            #print(resistorslist)
            print(f"{(math.fsum(resistorslist))**-1} Ohms\n")
            time.sleep(2)
    elif solve_for == "circuit":
        nopowersource = int(input("how many power sources are there? "))
        if nopowersource == 1:
            powervolt = int(input("how many volts? "))
            ire = input("any parallel resistors? ")
            if ire == "yes":
                d = True
                resistorlist = []
                eri = int(input("how many resistors? "))
                for i in range(0,eri):
                    resistorlist.append(1/(float(input(f"resistor{i + 1} "))))
                #print(resistorlist)
                use = ((math.fsum(resistorlist))**-1)
            else:
                d = False
                print("\n")
            eir = input("any resistors in series? ")
            if eir == "yes":
                c = True
                resistlist = []
                eee = int(input("how many resistors? "))
                for i in range(0,eee):
                    resistlist.append(float(input(f"resistor{i + 1} ")))
                #print(resistlist)
                use2 = math.fsum(resistlist)
            else:
                c = False
                print("\n")
            if c == True and d == True:
                resistance = use + use2
            elif c == False and d == True:
                resistance = use
            elif c == True and d == False:
                resistance = use2
            else:
                print("\n")
            print(f"\nequivalent resistance is {resistance} Ohms\n")
            time.sleep(2)
            question2 = input("what do you want to know about the circuit? ")
            if question2 == "current":
                question5 = input("through a resistor or the entire circuit? ")
                if question5 == "entire circuit":
                    current2 = powervolt / resistance
                    print(f"the current through the entire circuit is {current2} amps\n")
                    time.sleep(2)
                elif question5 == "resistor":
                    if ire == "yes" and eir == "no":
                        djj = int(input("which resistor? "))
                        resistuse = (resistorlist[djj-1])**-1
                        #print(resistuse)
                        powerresist = (powervolt**2)/resistuse
                        print(f"\n\nCurrent through resistor {djj} ({resistuse} Ohms) is {(((powerresist)/resistance)**.5)} Amps\n")
                    elif ire == "no" and eir == "yes":
                        djj = int(input("which resistor? "))
                        resistuse = (resistlist[djj-1])
                        #print(resistuse)
                        powerresist = ((powervolt/resistance**2)*(resistuse))
                        print(f"Current through resistor {djj} ({resistuse} Ohms) is {((powerresist)/resistance)**.5} Amps\n")
                    elif ire == "yes" and eir == "yes":
                        djkkk = input("from a parallel set or a series set? ")
                        if djkkk == "parallel":
                            current1 = powervolt/resistance
                            voltage1 = powervolt - (use2*current1)
                            djj = int(input("which resistor? "))
                            resistuse = (resistorlist[djj-1]**-1)
                            #print(resistuse)
                            powerresist = (voltage1**2)/resistuse
                            print(f"\n\nCurrent through resistor {djj} is {((powerresist/resistance)**.5)} Amps\n")
                            time.sleep(2)
                        elif djkkk == "series":
                            current1 = powervolt/resistance
                            voltage2 = powervolt - (use*current1)
                            djj = int(input("which resistor? "))
                            resistuse = (resistlist[djj-1])
                            #print(resistuse)
                            powerresist = (current1**2)*(resistuse)
                            print(f"\n\nCurrent through resistor {djj} is {((powerresist/resistuse)**.5)} Amps\n")
                            time.sleep(2)
            elif question2 == "power":
                if ire == "yes" and eir == "no":
                    djj = int(input("which resistor? "))
                    resistuse = (resistorlist[djj-1]**-1)
                    #print(resistuse)
                    powerresist = (powervolt**2)/resistuse
                    print(f"\n\nPower through resistor {djj} ({resistuse}) is {powerresist} watts\n\n")
                    time.sleep(2)
                elif ire == "no" and eir == "yes":
                    djj = int(input("which resistor? "))
                    resistuse = (resistlist[djj-1])
                    #print(resistuse)
                    powerresist = ((powervolt/resistance)**2)*(resistuse)
                    print(f"\nPower through resistor {djj} ({resistuse} Ohms) is {powerresist} watts\n\n")
                    time.sleep(2)
                elif ire == "yes" and eir == "yes":
                    djkkk = input("from a parallel set or a series set? ")
                    if djkkk == "parallel":
                        current1 = powervolt/resistance
                        print(f"Total current through the circuit is {current1} amps")
                        voltage1 = powervolt - (use2*current1)
                        djj = int(input("which resistor? "))
                        resistuse = (resistorlist[djj-1]**-1)
                        #print(resistuse)
                        powerresist = (voltage1**2)/resistuse
                        print(f"\n\nPower through resistor {djj} ({resistuse}) is {powerresist} watts\n\n")
                        print(f"\n\nCurrent through resistor {djj} is {((powerresist/resistance)**.5)} Amps")
                        time.sleep(2)
                    elif djkkk == "series":
                        current1 = powervolt/resistance
                        print(f"Total current through the circuit is {current1} amps")
                        voltage2 = powervolt - (use*current1)
                        djj = int(input("which resistor? "))
                        resistuse = (resistlist[djj-1])
                        #print(resistuse)
                        powerresist = (current1**2)*(resistuse)
                        print(f"\n\nPower through resistor {djj} ({resistuse}) is {powerresist} watts\n\n")
                        print(f"\n\nTherefore, current through resistor {djj} is {((powerresist/resistuse)**.5)} Amps")
                    
            
        
        

z = True
while z:
    try:
        vir_calc()
    except Exception as ValueErr:
        print(f"\n{ValueErr}\n")
    

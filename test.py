#Gas: Argon

exit_prog = False 
a = 1.355
b = 0.03201
R = 0.0821

def compute_pressure():
    temp = input("Input the temperature in Kelvin: ")
    Vm = input("Input the molar volume in L/mol: ")

    P = ((R * float(temp)) / (float(Vm) - b)) - (a / float(Vm)**2)

    print("Pressure: ", P,"atm","\n")

def compute_temp():
    P = input("Input the pressure in atm: ")
    Vm = input("Input the molar volume in L/mol: ")

    temp = ((P + (a / float(Vm)**2)) * (float(Vm) - b))  / R

    print("Temperature: ", temp,"K","\n")
    
def compute_molar_volume():
    P = input("Input the pressure in atm: ")
    temp = input("Input the temperature in Kelvin: ")

    Vm_old = (R * float(temp)) / float(P)
    Vm_new = 0.0
    i = 0
    i_max = 1000
    tolerance = 1e-6

    while i < i_max:
        Vm_new = (R * float(temp)) / (float(P) + (a / (float(Vm_old)**2))) + b

        if abs(Vm_new - float(Vm_old)) < tolerance:
            break

        Vm_old = Vm_new
        i += 1

    if i == i_max:
        print("Iteration did not converge within the limit")

    print("Molar Volume: ", Vm_new,"L/mol", "\n")

def exit_program():
    print("Are you sure you want to quit the program?")
    print("Press 'Y' if yes, press 'N' if no")
    
    choice = input("Input choice: ")
    
    if choice.upper() == "Y":
        print("Exiting the program...")
        return True
        
    elif choice.upper() == "N":
        print("Returning to main menu...")
        return False
        
    else:
        print("Invalid input, please try again")
        exit_program()

while not exit_prog:
    print("Welcome to Van der Waals Argon Calculator!")
    print("What shall we compute today?")
    print("1 - Pressure\n2 - Temperature\n3 - Molar Volume\n4 - Exit Program")

    choice = input("Input choice: ")

    if choice == "1":
        compute_pressure()
    elif choice == "2":
        compute_temp()
    elif choice == "3":
        compute_molar_volume()
    elif choice == "4":
        exit_prog = exit_program()
    else:
        print("Invalid input, please try again.")








    
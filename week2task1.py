def celsius_to_fahrenheit(degreeC):
    return (degreeC*(9/5))+32

def meters_to_feet(meters):
    return meters * 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms*2.205

while True:
    print("Choose an option:")
    print("1. celsius to fahrenheit ")
    print("2. meters to feet  ")
    print("3. Kilograms to Pounds ")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        degreeC = float(input("Enter temperature in celsius: "))
        FarenheitF = celsius_to_fahrenheit(degreeC)
        print(f"{degreeC} is equal to {FarenheitF}  ")
    elif choice == '2':
        meters = float(input("Enter meters: "))
        feet = meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet} feet.")
    elif choice == '3':
        kilograms = float(input("Enter Kilograms: "))
        pounds = kilograms_to_pounds(kilograms)
        print(f"{kilograms} kgs is equal to {pounds} pounds.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

number_gas = 0
number_oil = 0

print("***Welcome to Gas Station Program!***")
print("Please select the type of purchase:")
option = input("G: Gas \nO: Oil\n>>> ")

option = option.lower()

if option not in ("g", "o"):
  print("Invalid input, you should enter g/G or o/O")
  exit()

if option == "g":
  number_gas = int(input("Enter the number of liters of gas: "))
  if number_gas < 0:
    print("Number of gas liters shoulds be > 0")
    exit()
  else:
    province_gas = input("Please enter the 2 letters province abbreviation: ")

if option == "o":
  number_oil = int(input("Enter the number of cases of Oil: "))
  if number_oil < 0:
    print("Number of oil cases should be > 0")
    exit()
  else:
    province_oil = input("Please enter the 2 letters province abbreviation: ")
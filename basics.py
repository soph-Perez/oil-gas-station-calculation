import constants

number_gas = 0
number_oil = 0
gst = 0

print("\n***Welcome to Gas Station Program!***")
print("Please select the type of purchase:")
option = input("G: Gas \nO: Oil\n>>> ")

option = option.lower()

if option not in ("g", "o"):
  print("Invalid input, you should enter g/G or o/O")
  exit()

if option == "g":
  number_gas = int(input("Enter the number of liters of gas: "))
  if number_gas <= 0:
    print("Number of gas liters shoulds be > 0")
    exit()

  province_gas = input("Please enter the 2 letters province abbreviation: ").upper()
  before_discount_gas = constants.GAS_LITRE*number_gas

  if number_gas > 4000:
    price_per_litre_gas = constants.GAS_LITRE - (constants.GAS_LITRE*.10)
  else:
    price_per_litre_gas = constants.GAS_LITRE

  match province_gas:
    case "AB" | "BC" | "MB" | "NT" | "NU" | "QC" | "SK" | "YT":
      gst_gas = constants.GST_ONE/100
    case "ON":
      gst_gas = constants.GST_TWO/100
    case _:
      gst_gas = constants.GST_THREE/100

  after_discount_gas = price_per_litre_gas*number_gas
  gst_gas_final = gst_gas*after_discount_gas
  total_gas = after_discount_gas + gst_gas_final

  print(f"{'Product':<10} {'# of Litres':^15} {'Price Before Discount':^22} {'Price After Discount':^22} {'GST':^15} {'Total Price':^15}")
  print(f"{'Gas':<10} {number_gas:^15.1f} {before_discount_gas:^22.1f} {after_discount_gas:^22.1f} {gst_gas_final:^15.2f} {total_gas:^15.2f}")

if option == "o":
  number_oil = int(input("Enter the number of cases of Oil: "))
  if number_oil <= 0:
    print("Number of oil cases should be > 0")
    exit()
  
  province_oil = input("Please enter the 2 letters province abbreviation: ").upper()
  cases_to_liters = number_oil*12
  before_discount_oil = cases_to_liters*constants.OIL_CASES

  if number_oil > 8:
    price_per_litre_oil = constants.OIL_CASES - (constants.OIL_CASES*.10)
  else:
    price_per_litre_oil = constants.OIL_CASES

  match province_oil:
    case "AB" | "BC" | "MB" | "NT" | "NU" | "QC" | "SK" | "YT":
      gst_oil = constants.GST_ONE/100
    case "ON":
      gst_oil = constants.GST_TWO/100
    case _:
      gst_oil = constants.GST_THREE/100

  after_discount_oil = cases_to_liters*price_per_litre_oil
  gst_oil_final = gst_oil*after_discount_oil
  total_oil = gst_oil_final + after_discount_oil

  print(f"{'Product':<10} {'# of Litres':^15} {'Price Before Discount':^22} {'Price After Discount':^22} {'GST':^15} {'Total Price':^15}")
  print(f"{'Oil':<10} {cases_to_liters:^15.1f} {before_discount_oil:^22.1f} {after_discount_oil:^22.1f} {gst_oil_final:^15.2f} {total_oil:^15.2f}")



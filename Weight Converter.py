weight = float(input("Weight: "))
unit = input("Type 'k' for kg and 'l' for lbs: ")

if unit.upper() == "L":
    converted = weight * 0.45359237
    print("Weight in kg: " + str(converted))
else:
    converted = weight / 0.45359237
    print("Weight in lbs: " + str(converted))

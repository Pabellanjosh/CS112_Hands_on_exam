Prompt = int(input("Type 1 for Base 10 to Base\nType 2 for Base 10 to Base 8\n Type 3 for base 10 to Base 16:"))

if Prompt == 1:
    Dec = int(input("Enter a Decimal Number:"))
    print(format(Dec, "b"))
elif Prompt == 2:
    Oct = int(input("Enter a Decimal Number:"))
    print(format(Oct, "o"))
elif Prompt == 3:
    Hex = int(input("Enter a Decimal Number:"))
    print(format(Hex, "x"))
else:
    print("Invalid Input, Please Try Again")
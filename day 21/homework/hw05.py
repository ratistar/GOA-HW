last_name = input("Please enter last name: ")
convert = input("Do you want to convert your last name to uppercase? (yes/no): ")

if convert.lower() == "yes":
    print(last_name.upper())
else:
    print(last_name)
# მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ როგორ უნდა რო შეიცვალოს მის
# ი გვარის ასოები, თუ გიპასუხებთ "upper" გადაიყვანეთ მთლიანი გვარი დიდ ასოებად, თუ გიპასუხებთ 
# "lower" გადაიყვანეთ მთლიანი გვარი პატარა ასოებად და თუ
# გიპასუხებთ "capitalize" გადაიყვანეთ გვარის მხოლოდ პირველი ასო დიდ ასოდ.

surname = input("enter your surname")
change = input("how would u like to change ur surname")

if change == "upper":
    print(surname.upper())
elif change == "lower":
    print(surname.lower())
elif change == "capitalize":
    print(surname.capitalize())
else:
    print("invalid input")
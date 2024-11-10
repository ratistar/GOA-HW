my_name = "rati"
my_age = 14

# მომხმარებლისგან მიიღეთ ინფორმაცია
user_name = input("please enter your name: ")
user_age = int(input("please enter your age : "))

# შემოწმება, თუ სახელი და ასაკი ემთხვევა
if user_name == my_name and user_age == my_age:
    print("Twins")
else:
    print("Not Twins")
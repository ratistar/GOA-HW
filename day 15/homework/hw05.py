original_password = "correct_password"

while True:
    user_password = input("please enter your pass: ")
    
    if user_password == original_password:
        print("correct")
        break  
    else:
        print("how can u forget your password bro?.")
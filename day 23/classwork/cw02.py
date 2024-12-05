# 2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ, თუ გვარის პირველი ასო არის დიდი ასო, მაშინ დაუბეჭდეთ "Hello", თუ
#  არ არის მაშინ დაუბეჭდეთ "Bye"

last_name = input("enter ur last name: ")   
if last_name[0].upper():
    print("Hello")
else:
    print("Bye")
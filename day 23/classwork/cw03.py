# მომხმარებელს შემოატანინეთ სახელი, შემდეგ შემოატანინეთ ასო და თუ ამ სახელში ეს
# ასო არიქნება, მაშინ გამოუტანეთ "Can't find character", თუ იქნება მაშინ გამოუტანეთ "found it" და გვერდზე მიუწერეთ ამ ასოს ინდექსი

name = input("enter ur name: ")
character = input("enter ur character: ")
if character in name:
    index = name.find(character)
    print("found it: ")
else:
    print("Can't find character")

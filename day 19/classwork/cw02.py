#შექმენით სია რომელიც შედგება 5 რიცხვისგან, გადაუარეთ ამ სიას for ციკლით და შეაჯამეთ თითოეული რიცხვი,
#ბოლოს გამოიტანეთ ამ რიცხვების ჯამი (დაგჭირდებათ ერთი დამატებითი დამთვლელი ცვლადი (ჯამის ცვლადი, რომელსაც თითოეული
#რიცხვი დაემატება ყოველ იტერაციაზე))

numbers = [7, 5, 14, 4, 8]
total_sum = 0

for number in numbers:
    total_sum += number

print("Sum of numbers:", total_sum)
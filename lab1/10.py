#10. Calculate the number of digits and letters in a string

x = input("Enter a string: ")
letters = 0
digits = 0
for i in x:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
print("Letters:", letters)
print("Digits:", digits)

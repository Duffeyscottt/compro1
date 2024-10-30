eggs = int(input("Enter number of eggs to purchase: "))

if eggs <= 48:
    pricePerEgg = .5/12
elif eggs > 48 and eggs <= 72:
    pricePerEgg = .45/12
elif eggs > 72 and eggs <= 132:
    pricePerEgg = .4/12
elif eggs > 132:
    pricePerEgg = .35/12
    
bill = eggs * pricePerEgg
recipt = "The bill is equal to: $" + str(bill)
print(recipt)

input()
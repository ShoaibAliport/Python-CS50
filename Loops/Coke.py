amount = 50
while amount > 0:
    print("Amount Due: ",amount)
    coin = int(input("Insert coin: "))
    if coin in [5,10,25]:
        amount -= coin
change = abs(amount)
print("Change Due: ",change)


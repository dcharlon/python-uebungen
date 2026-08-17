amount_due = 50
while amount_due > 0:
    coins_paid = int(input("Insert coin: "))
    if coins_paid == 5 or coins_paid == 10 or coins_paid == 25:
        amount_due -= coins_paid
    if amount_due > 0:
        print("Amount due:", amount_due)
    else:
        print("Change owed:", -amount_due)

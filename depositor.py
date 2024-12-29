cash = 2088.23
def depositor():
    global cash
    while True:
        try:
            deposit = float(input("How much you wanna deposit: "))
            if deposit > cash:
                print("Not enough Money!")
            else:
                cash -= deposit
                return cash
        except ValueError:
            print("Please Enter a valid number")
depositor()
print(cash)

while True:
    amount = input("please enter your amount: ")
    if amount.isdigit():
        amount = int(amount)
        while True:
            tax = input("Please enter tax rate: ")
            if tax.isdigit():
                tax = int(tax)
                if 1 < tax < 99:
                    print("=== === === === === ===")
                    print(f'AMOUNT: {amount}$')
                    print(f"TAX: {tax}%")
                    print("=== === === === === ===")
                    print(f"TAX: {(tax/100)*amount}$")
                    print(f"NET: {amount-(tax/100)*amount}$")
                    print("=== === === === === ===")
                    while True:
                        yes_no = input("DO YOU WANT TO CONTINUE? [Y/N]")
                        if yes_no=='Y':
                            break
                        elif yes_no=='N':
                            exit()
                        else:
                            print("Sorry i don't understand!!!!")

                else:
                    print("Number is incorrect, Please try again!!!!!")
            else:
                print("Number is incorrect, Please try again!!!!!")
    else:
        print("Number is incorrect, Please try again!!!!!")
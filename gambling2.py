import random
money = 100

class bank:
    bank_money = 0
    def menu(self):
        global money
        print(f"\n<< Welcome to Bank >>\n1) Deposit Money\n2) Withdraw Money\n3) Bank Balance")
        choice = int(input("\nEnter Choice: "))
        if(choice==1):
            amount = int(input("\nEnter amount you want to deposit: "))
            if(amount>money):
                    print(f"\nAmount cannot be higher than balance!")
                    amount = 0
            elif(amount<=0):
                print(f"\nAmount cannot be 0 or negative!")
                amount = 0
            else:
                money = money-amount
                bank.bank_money += amount
                print(f"\nDeposit of {amount}$ successful!")
                amount = 0
        elif(choice==2):
            print(f"\nBank Balance: {bank.bank_money}$")
            amount2 = int(input("\nEnter amount you want to withdraw: "))
            if(amount2>bank.bank_money):
                print(f"\nAmount cannot be higher than bank balance!")
                amount2 = 0
            elif(amount2<=0):
                print(f"Amount cannot be 0 or negative!")
                amount2 = 0
            else:
                bank.bank_money -= amount2
                money += amount2
                print(f"\nWithdrawal of {amount2}$ is successful.")
                amount2 = 0
        elif(choice==3):
            print(f"\nYou're bank balance is {bank.bank_money}$")
        else:
            print(f"\nInvalid Choice!!")


while True:
    print("\n<< Gambling v2 >>\n1) Balance\n2) Bet Money\n3) Bank\n4) Exit Game")
    choice2 = int(input("\nEnter your choice: "))
    if(choice2==1):
        print(f"\nYour balance is: {money}$")
    elif(choice2==2):
        bet = int(input("\nEnter amount you want to bet: "))
        if(bet>money):
            print(f"\nAmount cannot be higher than money!")
            bet = 0
        elif(bet<=0):
            print(f"\nAmount cannot be zero or negative!")
            bet = 0
        else:
            wol = random.randint(1,2)
            if(wol==1):
                print(f"\nYou won {bet}$! Congo.")
                money = money+bet
                bet = 0
            elif(wol==2):
                print(f"\nYou lost {bet}$! So sad.")
                money = money-bet
                bet = 0
    elif(choice2==3):
        banker = bank()
        banker.menu()
    elif(choice2==4):
        print(f"\nYou're exiting the game...")
        break
          

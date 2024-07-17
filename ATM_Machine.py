import time
class ATM:
    def __init__(self,pin):
        self.pin = pin
        self.balance = 5000
        self.Mini_Statement = []
    
    def display_menu(self):
        print("ATM Menu Options:")
        print("1) Mini Statement")
        print("2) WithDraw")
        print("3) Deposit")
        print("4) Check Balance")
        print("5) Change Pin")
        print("6) Quit")
    
    def show_Mini_Statement(self):
        print("Transaction History:")
        if(self.Mini_Statement==[]):
            print("Transcation History is Empty")
        else:
            for transaction in self.Mini_Statement:
                print(transaction)
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.Mini_Statement.append((f"Rs {amount} has been debited from your account."))
            print(f"Rs {amount} has been Debited from your account")
        else:
            print("Invalid amount or insufficient balance")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.Mini_Statement.append((f"Rs {amount} has been Credited into your account."))
            print(f"Rs {amount} has Been Credited in your account")
        else:
            print("Invalid amount.")
    
    def check_balance(self):
        print(f"Your Current Balence is Rs {self.balance} ")
    
    def change_pin(self):
        pin1=input("Enter New Pin: ")
        pin2=input("ReEnter New Pin: ")
        if pin1==pin2:
            self.pin=pin
            print("Pin Has Been Changed ")
        else:
            print("Pin Not Matched Try Again..!!")
    
    def run(self):
        print("\nWelcome to the ATM Machine!")
        entered_pin = input("Please Enter Your PIN: ")
        print("=======================================\n")
        
        if entered_pin == self.pin:
            while True:
                self.display_menu()
                choice = input("Enter Your Choices (1,2,3,4,5): ")
                
                if choice == "1":
                    self.show_Mini_Statement()
                    print("=======================================\n")

                elif choice == "2":
                    amount = float(input("Enter the Amount to WithDraw: "))
                    self.withdraw(amount)
                    print("=======================================\n")
                    
                elif choice == "3":
                    amount = float(input("Enter the Amount to Deposit: "))
                    self.deposit(amount)
                    print("=======================================\n")

                elif choice == "4":
                   self.check_balance()
                   print("=======================================\n")
                
                elif choice == "5":
                   self.change_pin()
                   print("=======================================\n")

                elif choice == "6":
                    print("Thank You And Have a Nice Day!!!")
                    print("=======================================\n")
                    break
              
                else:
                    print("Invalid Choice. Please Try Again.")
                    print("=======================================\n")
        else:
            print("Incorrect PIN. Access Denied.")
            
print("Please Insert Your Card ")
time.sleep(1)
print("Please Wait For A While....!")
time.sleep(3)
pin = input("\nSet Your PIN First: ")
atm = ATM(pin)
atm.run()
import csv
from login import Login

class Banking:

    information = []
    
    
    def __init__(self,Bank,Customer_name,Balance,account_num,pin,account_type):
        self.Bank = Bank
        self.Customer_name = Customer_name
        self.Balance = Balance
        self.account_num = account_num
        self.pin = pin
        self.account_type = account_type

        Banking.information.append(self)


    def __repr__(self):
        return f"({self.Bank} : {self.Customer_name} , {self.Balance} , {self.account_num} , {self.pin} , {self.account_type})"

    #Use this method function to transfer money from your account
    def transfer_money(self):
        account_number  = int(input("Enter the account number of the reciever :"))
        amount = int(input("Enter the amount want to transfer :"))
        card_holder = input("Enter the name of the card holder :")
        
        i = 3

        while i != 0:
            code = int(input("Enter your pin :"))
            if code == self.pin:
                
                if amount >= self.Balance:
                    print("\nInsufficient Balance.")
                else:
                    print("Payment sucessfully transfered.")
                    self.Balance = self.Balance - amount
                    print("\nRs.",amount," is debited from",self.Bank,"a/c",self.account_num,"to",card_holder,",availabe balance :",self.Balance)
            else:
                print("\nInvalid pin try again.")

            i-=1
            if i == 0:
                print("\nLimit reached.")

    #Use this function to Check your account balance
    def check_balance(self):
        return {self.Balance,"is the Available Balance."}


    #Use this function to create object in the csv file
    @classmethod
    def creating_obj(cls):
        Customer_name = input("Enter your name :")
        Balance = int(input("Enter your amount :"))
        account_num = int(input("Enter your account number :"))
        Bank = input("Enter the name of your bank :")
        pin = int(input("Enter your pin :"))
        account_type = input("Enter your account type :")
        all_info = [Bank,Customer_name,Balance,account_num,pin,account_type]
        with open ("Customer_id.csv","a") as info:
            csv_writer = csv.writer(info)
            csv_writer.writerow(all_info)

    #Use this funtion to intantiate from csv
    @classmethod
    def intantiating_object(cls):
        with open ("Customer_id.csv","r") as a:
            csv_reader = csv.DictReader(a)
            info = list(csv_reader)

        for x in info:
            Banking(
                    Customer_name = x.get('Customer_name'),
                    Balance = x.get('Balance'),
                    account_num = x.get('account_num'),
                    Bank = x.get('Bank'),
                    pin = x.get('pin'),
                    account_type = x.get('account_type')
            )




# Banking.intantiating_object()
# print(Banking.information)
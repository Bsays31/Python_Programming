from login import Login
import csv
class verification(Login):

    
    def verify_phone(self):
        number = int(input("Enter your phone number :"))
        if number in Login.data:
            
                        








    # @classmethod
    # def Intantiating_object(cls):
    #     with open('Login_id.csv', 'r') as ola:
    #         csv.reader = csv.DictReader(ola)
    #         a1 = list(csv.reader)

    #     for a in a1:
    #         verification(
    #             Phonenumber
    
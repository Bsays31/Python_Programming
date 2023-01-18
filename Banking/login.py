import csv
class Login:

    data = []

    def __init__(self,Name : str,Age,Email,Password,Phonenumber):
        
        self.Phonenumber = Phonenumber
        self.Name = Name
        self.Age = Age
        self.Email = Email
        self.Password =Password
        
        Login.data.append(self)

    @classmethod
    def Intantiating_from_csv(cls):
        with open('Login_id.csv','r') as a:
            csv_reader = csv.DictReader(a)
            info = list(csv_reader)
        
        for x in info:
            Login(
                    Name =str( x.get('Name')),
                    Age = x.get('Age'),
                    Email = x.get('Email'),
                    Password = x.get('Password'),
                    Phonenumber = x.get('Phonenumber')
                )

    @classmethod
    def creating_object(cls):
        Name = input("Enter your name :")
        Age = int(input("Enter your age :"))
        Email = input("Enter your email :")
        Password = input("set a password : ")
        Phonenumber = int(input("Enter your phome number :"))
        customer_data = [Name,Age,Email,Password,Phonenumber]
        with open("Login_id.csv","a") as f :
            csv_writer = csv.writer(f)
            csv_writer.writerow(customer_data)

    def __repr__(self):
        return f"({self.Name} , {self.Age} , {self.Email} , {self.Password} , {self.Phonenumber})"



client = Login("Bishesh_gurung",22,"bsaysgurung31@gmail.com","ulalal123",7365020554)
# client = Login("Bikash_gurung",34,"gurung31@gmail.com","herdim234",9002424414)

Login.creating_object()
# Login.Intantiating_from_csv()
# print(Login.data)
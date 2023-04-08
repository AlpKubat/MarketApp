import csv

PRODUCT_CSV = "Product.csv"
USERS_CSV = "Users.csv"

authLoginStatus = False
authName = ""
authSurname = ""
authAuthority = 0

def mainScreen():
    print("Welcome to the MARKET\n**********************************\n\n")
    print("For Sign in Enter '1' : \n")
    print("For Sign up Enter '2' : \n")
    print("For Showing the Product List Enter '3' : \n")
    decisions = ["1","2","3"]
    decision = input("")

    while(decision not in decisions):
        print("You entered wrong number please try again!\n")
        decision = input("")

    if(decision == "1"):
        signIn()

    elif(decision == "2"):
        pass
        #signUpForCustomer()

    elif(decision == "3"):
        pass
        #showProductList()

def signIn():
    global authAuthority
    global authLoginStatus
    global authName
    global authSurname
    while(not authLoginStatus):
        userName = input("UserName = ")
        password = input("Password = ")

        with open(USERS_CSV,"r") as user_file:
            userDict = csv.DictReader(user_file)

            for line in userDict:
                if(line["UserName"] == userName and line["Password"] == password):
                    authLoginStatus = True
                    authName = line["Name"]
                    authSurname = line["Surname"]
                    authAuthority = line["Authority"]

            if(not authLoginStatus):
                print("Wrong UserName or Password please Enter again!!\n")
                


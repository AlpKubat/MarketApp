import csv

PRODUCT_CSV = "Products.csv"
USERS_CSV = "Users.csv"
BILLS_CSV = "Bills.csv"

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
        if(authLoginStatus):
            buyProduct()
        

    elif(decision == "2"):
        signUpForCustomer()

    elif(decision == "3"):
        showProductList()

def signIn():
    global authAuthority
    global authLoginStatus
    global authName
    global authSurname
    while(not authLoginStatus):
        userName = input("UserName = ")
        password = input("Password = ")

        with open(USERS_CSV,"r",encoding="utf-8") as user_file:
            userDict = csv.DictReader(user_file)
            

            for line in userDict:
                if(line["Username"] == userName and line["Password"] == password):
                    authLoginStatus = True
                    authName = line["Name"]
                    authSurname = line["Surname"]
                    authAuthority = line["Authority"]
                    return True

            if(not authLoginStatus):
                print("Wrong UserName or Password please Enter again!!\n")



def showProductList():

    with open(PRODUCT_CSV,"r",encoding="utf-8") as product_file:
        productDics = csv.DictReader(product_file)

        print("Name \t Price \t Amount")
        for line in productDics:
            print(line["Name"],"\t",line["Price"],"\t",line["Amount"])
                


def signUpForCustomer():

    dics = []
    dic = {}
    usedUserNames = []
    with open(USERS_CSV,"r",encoding="utf-8") as users_file:
        userdics = csv.DictReader(users_file)

        for line in userdics:
            dics.append(line)
            usedUserNames.append(line["Username"])

    with open(USERS_CSV,"w",encoding="utf-8") as user_file:
        fieldnames = ["Authority","Name","Surname","Username","Password"]
        userwriter = csv.DictWriter(user_file,fieldnames=fieldnames)

        dic["Authority"] = 1
        dic["Name"] = input("Name = ")
        dic["Surname"] = input("Surname = ")
        dic["Username"] = input("Username = ")
        while(dic["Username"] in usedUserNames):
            print("your userName is used. Please change it! \n")
            dic["Username"] = input("Username = ")

        dic["Password"] = input("Password = ")

        dics.append(dic)
        userwriter.writeheader()
        for line in dics:
            userwriter.writerow(line)


def takeOrder():
    orderName = input("Please Enter product name = ").capitalize()
    return orderName


def totalPrice(dicarr):
    totalPrice = 0.0
    for order in dicarr:
        totalPrice += order["Price"]
    return totalPrice


def displayBill(bill):
    print(authName,authSurname,"your bill is:")
    print("Name \t Amount \t Price\n")
    for line in bill:
        print(line["Name"],"\t",line["Amount"],"\t",line["Price"])
    print("\nTotal cost = ",totalPrice(bill))


def buyProduct():

    if(not authLoginStatus):
        print("You are not logged in! please sign in")
        if(signIn()):
            buyProduct()
    
    if(authAuthority != 1):
        print("Please login with customer account!")
        if(signIn()):
            buyProduct()

    showProductList()

    with open(PRODUCT_CSV,"r", encoding = "utf-8") as product_file:
        productReader = csv.DictReader(product_file)

        productNames = []
        products = []
        bill = {}
        for line in productReader:
            productNames.append(line["Name"])
            products.append(line)

    
    print("To exit Enter 'Q', To Display Bill Enter 'Bill'\n")
    orderName = takeOrder()

    cart = []

    while(orderName != "Q"):

        if(orderName == "Bill"):
            displayBill(cart)
            orderName = takeOrder()
            continue

        elif(orderName not in productNames):
            print("Given Product name does not exist Please enter again = ")
            orderName = input("")
            continue
        
        orderAmount = float(input("Please enter amount of order = "))

        for product in products:
            if(product["Name"] == orderName):
                while(orderAmount > float(product["Amount"]) or orderAmount < 0):
                    print("to buy another product please enter '0'")
                    orderAmount = float(input("you entered amount wrong!\n Please enter Again = "))
                break
        if(orderAmount == 0):
            orderName = takeOrder()
            continue
        

        for product in products:
            if(product["Name"] == orderName):
                orderPiece = product.copy()
                orderPiece["Amount"] = orderAmount
                orderPiece["Price"] = float(orderPiece["Price"]) * orderAmount
                product["Amount"] = float(product["Amount"]) - orderAmount
                cart.append(orderPiece)

        orderName = takeOrder()

    if(len(cart) < 1):
        print("you are not buying anything! You are directing to MainMenu")
        mainScreen()
        return
    
    displayBill(cart)

    
                

        









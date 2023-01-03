class MiniBank:
    main_userInfo: dict = {}
    balance = 0
   
    def firstOption(self):
        option : int = int(input("Press 1 : to login : \nPress 2 : to Register : "))
        if option == 1:
            self.Login()
        else:
            self.register()

    def returnId(self,transfer_username):
        userInfo_length : int = len(self.main_userInfo)
        for i in range(1,userInfo_length+1):
            if self.main_userInfo[i]['r_username'] == transfer_username :
                return i
        return None

    def updateAccount(self,LoginId):
        print("UserId",LoginId)
        del self.main_userInfo[LoginId]
        r_username : str = input("Please enter username to register : ")
        r_passcode1 : int = int(input("Please enter passcode to register : "))
        r_passcode2 : int = int(input("Please enter again passcode : "))
        r_amount : int = int(input("Enter amount : "))
        if(r_passcode1 == r_passcode2):
            id : int = self.checkingUserCount()
            userInfoForm : dict = {id: {"r_username" : r_username,
                                        "r_passcode" : r_passcode2,
                                        "Amount"     : r_amount
                                    }}
            self.main_userInfo.update(userInfoForm)
        print(self.main_userInfo)

       

    def withdraw(self,LoginId):
        for(LoginId,value) in self.main_userInfo.items():
            print(f"The value of {LoginId} is {value} ")
        self.balance = int(input("User -r_amount "))
        print("Before withdraw,user balance",self.balance)
        amount:int = int(input("Enter to be withdraw :  "))
       
           
        if self.balance >= amount:
            self.balance-=amount
           
            print("\n You withdraw : ",amount)
            print("\n Your balance : ",self.balance)
        else:
            print("\n Insufficient balance.")


    def menu(self,LoginId):
        menu_input = int(input("Press1: to Transfer : \nPress2 : to Windraw : \nPress3 : to update user data :"))
        print(menu_input)
        if menu_input == 1:
            transfer_username :str = input("Please enter username to transfer")
            transfer_id : int = self.returnId(transfer_username)
            print("\n\n We get to Transfer id : ",transfer_id)
            print("myId",LoginId)
            Amount : int = int(input("Enter amount to transfer {0} : ".format(self.main_userInfo[transfer_id]["r_username"])))
            print("Amount is : ", Amount)

        elif menu_input == 2:
            print("Withdrawuser : ",LoginId)
           
            # if id in self.main_userInfo:
            #     withdraw = int(input("How much money would you like to withdraw ? "))
            #     balance : int = self.main_userInfo[id][self.main_userInfo["Amount"]]
            #     if withdraw<balance:
            #         balance-=withdraw
            #         print("Your Balance : ",balance)
            self.withdraw(LoginId)

        elif menu_input==3:
            self.updateAccount(LoginId)
        else:
            print("You can choice : 1\2\3")
       

   
    def Login(self):

        print("\n----------- This is from Login -----------\n")
        L_username:str = input("Please enter user name to login : ")
        L_userpasscode:int =int(input("Please enter passcode to login : "))
        exitUser = self.exitUser(L_username,L_userpasscode)
       
        if(exitUser):
            print("\n\n-----Login Successful-----\n\n")
            LoginId = self.returnId(L_username)
            self.menu(LoginId)
           
        else:
            print("You can't login")

    def exitUser(self,L_username,L_userpasscode):
        user_count = len(self.main_userInfo)
        for i in range(1,user_count+1):
            if self.main_userInfo[i]["r_username"]==L_username and self.main_userInfo[i]["r_passcode"]== L_userpasscode :
                return True
        return False
   
    def register(self):
        print("\n----------This is from register--------\n")
        r_username : str = input("Please enter username to register : ")
        r_passcode1 : int = int(input("Please enter passcode to register : "))
        r_passcode2 : int = int(input("Please enter again passcode : "))
        r_amount : int = int(input("Enter amount : "))
        if(r_passcode1 == r_passcode2):
            id : int = self.checkingUserCount()
            userInfoForm : dict = {id: {"r_username" : r_username,
                                        "r_passcode" : r_passcode2,
                                        "Amount"     : r_amount
                                    }}
            self.main_userInfo.update(userInfoForm)

    def checkingUserCount(self):
        count = len(self.main_userInfo)
        return count+1

if __name__ == "__main__":
    miniBank: MiniBank = MiniBank()

    while True:
        miniBank.firstOption()
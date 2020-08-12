class main:
    
    def createAccount(self, *args):
        self.username = args[0]
        self.password = args[1]
        with open("accounts.txt","a") as fp:
            self.details = f"{self.username} {self.password}\n"
            fp.write(self.details)
            

    def LogintoAccount(self, *args):
        self.username = args[0]
        self.password = args[1]
        with open("accounts.txt","r") as fp:
            content = fp.readlines()
            for i in range(len(content)):
                user = content[i].split(" ")
                if user[0] == self.username:
                    if user[1].rstrip() == self.password:
                        return "Logged in Successfully!"
                    else:
                        return "Sorry Incorrect password"
                elif i == len(content)-1:
                    return "Sorry incorrect username."


    def updateAccount(self, *args):
        self.username = args[0]
        self.password = args[1]
        self.newPassword = args[2]
        fp =  open("accounts.txt","r+")
        content = fp.readlines()
        for i in range(len(content)):
            user = content[i].split(" ")
            if user[0] == self.username:
                if user[1].rstrip() == self.password:
                    user[1] = self.newPassword
                    newAccount = ' '.join(user)
                    content[i] = newAccount
                    fp.close()
                    fp = open("accounts.txt", "w")
                    newAccounts = "".join(content)
                    fp.write(newAccounts)
                    fp.write("\n")
                    fp.close()
                    return "Password changed successfully"
                else:
                    return "Sorry Incorrect Password entered"
            elif i == len(content)-1:
                return "Sorry Incorrect username"


    def deleteAccount(self, *args):
        self.username = args[0]
        self.password = args[1]
        fp = open("accounts.txt","r+")
        content = fp.readlines()
        print(content)
        for i in range(len(content)):
            user = content[i].split(" ")
            if user[0] == self.username:
                if user[1].strip() == self.password:
                    print(content.pop(i))
                    fp.close()
                    fp = open("accounts.txt","w")
                    accounts = "".join(content)
                    fp.write(accounts)
                    fp.close()
                    return "We are sorry to see you go!, Your Account has been successfully deleted"
                else:
                    return "Sorry incorrect password"
            elif i == len(content)-1:
                return "Incorrect username"






print("Select the apt. option before the operation you want to perform:\n 1. SignUp\n 2. Login\n 3. Update Password\n 4. Delete Account")
choice = int(input("Enter your choice: "))

obj = main()

if choice == 1:
    username = input("Enter username you want to have: ")
    password = input("Enter password: ")
    confirmPassword = input("Enter password to confirm: ")
    if password == confirmPassword:
        details = [username, password, confirmPassword]
        obj.createAccount(*details)
        print("Successfully signed up.")
    else:
        print("Passwords don't match.")

elif choice == 2:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    details = [username, password]
    print(obj.LogintoAccount(*details))

elif choice == 3:
    username = input("Enter username: ")
    password = input("Enter current password: ")
    newPassword = input("Enter new password: ")
    details = [username, password, newPassword]
    print(obj.updateAccount(*details))

elif choice == 4:
    username = input("Enter username: ")
    password = input("Enter password: ")
    details = [username, password]
    choice = input("Are you sure you want to delete your account?('y' for yes 'n' for no) ")
    if choice.lower() == 'y':
        print(obj.deleteAccount(*details))
    else:
        print("Please enter 'y' or 'n'")

else:
    print("Please enter a valid choice")

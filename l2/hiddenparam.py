class User:
    __password = "abc123"

    def __init__(self, name, email, user):
        self.name = name
        self.email = email
        self.user = user

    def getPassword(self):
        return self.__password
    
    def setPassword(self):
        oldPassword = input("enter old password: ")
        if oldPassword == self.__password:
            newPassword = input("enter your new password: ")
            self.__password = newPassword
            print("password successfully changed!")
        else:
            print("incorrect password. please try again")

u1 = User("sana khan t", "sana123@gmail.com", "sana")
print(u1.email)
print(u1.getPassword())
u1.setPassword()
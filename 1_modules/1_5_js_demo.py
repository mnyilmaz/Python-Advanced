# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.5: Json Demo 
# python 1_5_js_demo.py
import email, json, os
blank = "----------------------"

class User:
    # In this class you may check if length of input is correct or mail if is in a correct form
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

##############################################################################################################

class User_Repo:
    def __init__(self):
        self.users = []
        self.is_logged = False
        self.current_user = {}

        # load users from.json file
        self.load()

##############################################################################################################

    def load(self):
        if os.path.exists("user.json"):
            with open("user.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    new_user = User(username = user["username"], password = user["password"], email = user["email"])
                    self.users.append(new_user)
            print(self.users) 

##############################################################################################################

    def register(self, user: User):
        self.users.append(user)
        self.save()
        print("User added to the system.\n")

##############################################################################################################

    def login(self,username,password):
        if self.is_logged:
            print("User has already logged into the system")
            
        for user in self.users:
            if user.username == username and user.password == password:
                self.is_logged = True
                self.current_user = user
                print("Login successfully")
                break        

##############################################################################################################

    def log_out(self):
        self.is_logged = True
        self.current_user = {}
        print("Logged out successfully")
        
    def identification(self):
        if self.is_logged:
            print(f"username: {self.current_user.username}")
        else:
            print("Please login first")


##############################################################################################################

    def save(self):
        # JSON cannot convert or process class file it needs string so with that we're getting a list for json
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__)) # turn into dict

        with open("user.json", "w") as f:
            json.dump(list, f)

##############################################################################################################

repository = User_Repo()

while True:
    print("Menu".center(50,"*"))
    choice = input("1 - Register\n2 - Login\n3 - Logout\n4 - Identitfication\nQ - Exit\nYour choice: ")
    if choice == "Q":
        break
    else:
        if choice == "1":
            # register
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            email = input("Please enter your email: ")

            user = User(username = username, password = password, email = email) 
            repository.register(user)
            # print(repository.users)

        elif choice == "2":
            # login
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            repository.login(username, password)

        elif choice == "3":
            # logout
            repository.log_out()
            
        elif choice == "4":
            repository.identification()

        else:
            print("Incorrect")
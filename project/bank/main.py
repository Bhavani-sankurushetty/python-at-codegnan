# Data base
"""
users = {
            Account:{
                    'name':username,
                    'Email': user email,
                    'balance':5000,
                    'password':password
            }
}
"""
users = {
    1001:{'name':Bhavani,'Email': bhavanisankurushetty@gmail.com,'balance':5000,'password':1001},
    1002:{'name':lakshmi,'Email': bhavanisankurushetty123@gmail.com,'balance':1000,'password':1002},
}


# register functions
def register(username:str,email:str,balance:int,password:str)->str:
    pass


# login function
def login(account:int,passowrd:str)->bool:
    pass

#get balance
def balance(account:int)->str:
    pass

#get withdraw
def withdraw(account:int,balance:int)->int:
    pass

#get deposite
def deposite(account:int,balance:int)->int:
    pass

# get mini statement
def mini_statement(account:int,balance:int)->int:
    pass

#get logout
def logout(account:int,)->str:
    pass


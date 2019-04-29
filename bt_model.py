import json
import os

PATH = os.path.dirname(__file__)
DATA = "acc_data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH, "r") as file_object:
        data = json.load(file_object)
        #print(data)

def save():
    with open(DATAPATH, "w") as file_object:
        json.dump(data, file_object, indent=2)

def create_account(f_name, l_name, pin):
    #Retrieve the max account_number and add one to it
    account_number = retrieve_max_account()
    account_number = str(int(account_number)+1) 
    data[account_number] = {"first_name": f_name, "last_name": l_name,
                            "pin": pin, "balance": 0.00}
    return account_number

def retrieve_max_account():
    max_account = 0
    for x in data:
        if int(x) > int(max_account):
            max_account = x
    return max_account

def validate_account(account, pin):
    if account in data:
        if int(data[account]['pin']) == int(pin):
            return data[account]['first_name']+" "+data[account]['last_name']
        else:
            return "xxx"
    else:
        return "xxx"

def get_bal(account):
    return float(data[account]['balance'])

def withdraw(account, amount):
    if float(data[account]['balance']) - float(amount) <0:
        return "xxx"
    else:
        data[account]['balance'] = float(data[account]['balance']) - float(amount)
        return float(data[account]['balance'])

def deposit(account, amount):
    data[account]['balance'] = float(data[account]['balance']) + float(amount)
    return float(data[account]['balance'])





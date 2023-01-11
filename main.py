from flask import Flask, jsonify, request
import json

from Account import *
from AccountHandler import *
account_handler = AccountHandler()

app = Flask(__name__)


#Beispiel
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})
    if(request.method == 'POST'):
        data = "test komplett...."
        #Daten vom Post holen:
        print(request.get_data())
        return jsonify({'data2': data})

@app.route('/printAccounts', methods = ['GET', 'POST'])
def printAccounts():
    if(request.method == 'POST'):
        account_handler.printAccounts()
    return jsonify({'Status': "1"})

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        json_object = request.get_json()
        tmp_username = json_object['username']
        tmp_password = json_object['password']
        print("Username: {0}".format(tmp_username))
        print("Password: {0}".format(tmp_password))
        if account_handler.checkAccount(Account(tmp_username, tmp_password)):
            return jsonify({'login': "Success!"})
        else:
            return jsonify({'login': "Failed!"})

@app.route('/newAccount', methods = ['GET', 'POST'])
def newAccount():
    if(request.method == 'POST'):
        json_object = request.get_json()
        tmp_username = json_object['username']
        tmp_password = json_object['password']
        new_acc = Account(tmp_username, tmp_password)
        #account_handler.addAccount(new_acc)
        account_handler.addAccountSQL(new_acc)
        return jsonify({'accountStatus': "Created new Account!"})

@app.route('/getDays', methods = ['GET', 'POST'])
def getDays():
    if(request.method == 'POST'):
        print("Client asked for days: {0}".format(request.remote_addr))
        json_object = request.get_json()
        tmp_userid = json_object['userid']
        current_days = account_handler.getDays(tmp_userid)
        return jsonify({'days': "{0}".format(current_days)})

@app.route('/updateDays', methods = ['GET', 'POST'])
def updateDays():
    if(request.method == 'POST'):
        json_object = request.get_json()
        tmp_userid = json_object['userid']
        tmp_days = json_object['days']
        if account_handler.updateDays(tmp_userid, tmp_days):
            return jsonify({'status': "Updated Accounts!"})
        else:
            return jsonify({'status': "Failed!"})



@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

if __name__ == '__main__':
        app.run(debug = True, port=13500, host="0.0.0.0")
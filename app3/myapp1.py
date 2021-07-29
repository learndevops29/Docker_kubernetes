import os , sys 
from flask import Flask

appsname=os.environ["APP_SERVER"]
appsport=os.environ["APP_PORT"]
app=Flask(__name__)

@app.route("/")
def index():
    return "AppID %s : external port %s"  %(appsname,appsport)

@app.route("/home")
def home():
    return "Home AppID %s:external Port %s" %(appsname,appsport)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=appsport)


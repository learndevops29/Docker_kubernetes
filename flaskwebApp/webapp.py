import socket 
from flask import Flask

app=Flask(__name__)

hostn=socket.gethostname()
@app.route("/")
def index():
    return f"hello from {hostn}"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

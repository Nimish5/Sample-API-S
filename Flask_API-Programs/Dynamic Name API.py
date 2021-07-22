# from flask import Flask

# app = Flask(__name__)

# @app.route("/home/<string:name>/user")
# def an_api(name):
#     return "Hello, I am " + name

# # app.run(port=5000)
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask

app = Flask(__name__)

@app.route("/home/users/<string:name>/posts/<int:num>")
def Baba_(name, num):
    return "Hello, " + name + " your id is: " + str(num)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route('/home/<string:name>/user/<int:num>/logout')
# def baba_(name, num):
#     return "Hello ", name, "you have visited this website", str(num), "times!"

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route('/Login/<string:data>/dashboard/<string:data1>')
# def login_(data, data1):
#     return "Please enter your credentials, ", data, "You may leave the website", data1 

# if __name__ == "__main__":
#     app.run(debug=True)



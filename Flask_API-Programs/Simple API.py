# from flask import Flask

# app = Flask(__name__)

# @app.route("/home/<string:name>/user")
# def an_api(name):
#     return "Hello, I am " + name

# # app.run(port=5000)
# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route("/home/users/<string:name>/posts/<int:num>")
# def Baba_(name, num):
#     return "Hello, " + name + " your id is: " + str(num)

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route('/home/<string:name>/user/<int:num>/logout')
# def baba_(name, num):
#     return "Hello " + name + " you have visited this website, " + str(num) + " times!"

# if __name__ == "__main__":
#     app.run(debug=True) 


# from flask import Flask

# app = Flask(__name__)

# @app.route('/Login/<string:data>/dashboard/<string:data1>')
# def login_(data, data1):
#     return "Please enter your credentials, " + data + "You may leave the website" + data1 

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask

app = Flask(__name__)

@app.route('/login/<string:user_name>/home/hut/<int:id>/<string:name>')
def home_alone(user_name, id, name):
    return "Hello, " + user_name + " thank you for login, your login id is: " + str(id) + "! Thanks, I am " + name + ", leaving this web page"

@app.route('/home/<string:name>')
def function_(name):
    return "Thanks for visiting this web page, " + name + " you will be logout in 5 mins!"

# app.run(port=5000)
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/Hello')
def HW():
    return 'Hello World!'


# https://www.kite.com/python/answers/how-to-get-parameters-from-a-url-using-flask-in-python
@app.route('/check_palindrome')
def check_palindrome():
    s = request.args.get("str") 
    list1 = list(s)
    # print(list1)
    list1.reverse()
    list2 = []
    for letter in list1:
        list2.append(letter)
    x = ''.join(list2)

    if x == s:
        return "True"
    else:
        return "False"

app.run(debug=True)

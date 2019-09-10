from flask import Flask
from werkzeug.routing import BaseConverter
app = Flask(__name__)


#@app.route('/<user_name>')
#@app.route('/')
#def home(user_name):
#    return 'hello user! {}'.format(user_name)


#@app.route('/<int:num1>/<int:num2>')
#def home(num1, num2):
#    return 'sum number {}'.format(num1 + num2)


@app.route('/<str1>/<str2>/<str3>')
def home(str1, str2, str3):
    vol = []
    for x in str1, str2, str3:
        vol.append(x)
    return 'Самая длинная строка: {}'.format(max(vol, key=len))


if __name__ == '__main__':
    app.run()




















# @app.route('/<user>')
# def username(user):
#     return 'hello, user: ' + user
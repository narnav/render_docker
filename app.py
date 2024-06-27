from flask import Flask
api = Flask(__name__)




@api.route('/')
def hello():
    return 'Hello, World!'




if __name__ == '__main__':
    api.run(debug=True,host='0.0.0.0',port=5000)
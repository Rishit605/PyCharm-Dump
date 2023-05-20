from flask import Flask # First we import our Flask library.

app = Flask(__name__)

@app.route('/')

def fl_api():
    return 'This is a Basic FLask API program'

if __name__ == '__main__':
    app.run()
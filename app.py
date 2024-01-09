from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():

    return 'Electric Hacker'

if __name__ == "__main__":

    app.run()

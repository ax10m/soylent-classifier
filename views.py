import classifier
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/<some_text>')
def classify(some_text):
    return classifier.classify(some_text)




if __name__ == '__main__':
    app.run(debug=True)
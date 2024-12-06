# instruction will below. 
# Import Flask from the flask libary
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"
if __name__ == '__main__':
    app.run(debug = True)

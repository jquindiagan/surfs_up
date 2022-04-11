# import dependencies
from flask import Flask

# create app
app_practice = Flask(__name__)

# create route
@app_practice.route('/')
def hello_world():
    return 'Hello world'

if __name__=="__main__":
    app_practice.run(debug=True)
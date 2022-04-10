# import dependencies
from flask import Flask

# create app
app = Flask(__name__)

# create route
@app.route('/')
def hello_world():
    return 'Hello world'

if __name__=="__main__":
    app.run(debug=True)
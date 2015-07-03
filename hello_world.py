# ---- Flask Hello Wolrd ---- #

# import Flask class from flask moduel
from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorators to link the function to url
@app.route("/")
@app.route("/hello")

# define the vew using a fuction, which returns a string
def hello_world():
	return "Hello, World!"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()

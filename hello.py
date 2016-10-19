from flask import Flask

app = Flask(__name__) 

@app.route("/") 
def hello(): 
  return "Hello World!" 

@app.route('/greeting/<username>')
def profile(username):
  return "Hope you have a great day %s" %username

@app.route('/longday/<lastname>')
def night(lastname):
  return "Hope you are doing good. How was your day %s" %lastname

if (__name__ == "__main__"):
  app.run(debug = True)
 

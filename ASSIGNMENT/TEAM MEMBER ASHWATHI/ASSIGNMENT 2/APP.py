from urllib import request
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('registration.html')
    
@app.route('/success',methods=['POST'])
def home():
    name  = request.form.get("username")
    return "<h1>Welcome to Personal Blog!!</h1>"+name+" Thanks for registering..<br>Get Started"

if __name__=='__main__':
    app.run(debug=True)

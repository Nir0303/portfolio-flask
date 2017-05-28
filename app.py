from flask import Flask,render_template,url_for,request,session,redirect,send_file


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return "ok"
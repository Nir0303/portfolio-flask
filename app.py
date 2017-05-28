from flask import Flask,render_template,url_for,request,session,redirect,send_file
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',home=True)


@app.route('/blog')
def blog():
	return render_template('blog.html',blog=True)


@app.route('/project')
def project():
	return render_template('project.html',project=True)

@app.route('/resume')
def resume():
	return send_file('static/files/Niranjan Addanki Resume.pdf')

app.run()
from flask import Flask, render_template, url_for, request, session, redirect, send_file
import os
import argparse

app = Flask(__name__)


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--local', action='store_true', help='if mentioned run in local env')
    args = parser.parse_args()
    return args


@app.route('/')
def index():
    return render_template('index.html', home=True)


@app.route('/blog')
def blog():
    return render_template('blog.html', blog=True)


@app.route('/project')
@app.route('/projects')
def project():
    return render_template('project.html', project=True)


@app.route('/resume')
def resume():
    return send_file('static/files/Niranjan Addanki Resume.pdf')


if __name__ == '__main__':
    args = parse()
    if args.local:
        app.run(debug=True, host="0.0.0.0", port=8000)
    else:
        app.run()

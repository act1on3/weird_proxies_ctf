from flask import Flask, Response, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return Response("<html><div>Hello? My name is gunicorn and I have a friend called Nginx. We are really weird couple: proxy and backend :)</div><div>Can you find something behind /admin?</div></html>")

@app.route("/admin")
def admin():
    # TODO: change random location to step2
    return Response("Hello, admin! Go here /c7f5472b-4e09-4997-9eff-e1b7442b8b91/"), 200
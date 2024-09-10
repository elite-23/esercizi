from flask import Flask, render_template

api=Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@api.route('/pippo', methods=['GET'])
def pippo():
    return render_template("pippo.html")

api.run(host="0.0.0.0",port=8085)

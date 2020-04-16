import flask

app = flask.Flask(__name__)

@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def test(path):
    print(path)
    return '{}'

app.run(host='127.0.0.1',port=80)

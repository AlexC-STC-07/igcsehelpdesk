from flask import Flask

app = Flask(__name__)

@app.route('/', index_page)
def index_page():
    return "test flask shit"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



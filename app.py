from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


# if __name__ == "__main__":
#     app.run(debug=True)

# not sure why i cant run localhost 3000 without this code below
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)  
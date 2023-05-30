from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html', title = "Welcome to Simple Flask")



@app.route('/guess', methods=['GET'])
def guess():
    return render_template('index.html', title = "Welcome to Guess page")



@app.route('/blog', methods=['GET'])
def blog():
    return render_template('index.html', title = "Welcome to Blog Page")


if __name__ == "__main__":
    app.run(debug=True)
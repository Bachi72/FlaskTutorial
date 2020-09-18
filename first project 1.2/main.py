from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/C:/Users/Jens/PycharmProjects/WebDevelopment/first project 1.2/static')


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
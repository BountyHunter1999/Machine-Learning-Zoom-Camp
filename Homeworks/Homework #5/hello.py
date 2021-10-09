from flask import Flask

app = Flask("demo")

@app.route("/ping")
def ping():
    return "<h1>PONG!</h1>"

if __name__ == "__main__":
    app.run(DEBUG=True)


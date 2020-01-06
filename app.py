from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '欢迎来到我的 Watchlist！'


if __name__ == "__main__":
    app.run()

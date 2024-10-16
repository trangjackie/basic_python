from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(port=5080)  # Thay đổi cổng mặc định từ 5000 sang 8080

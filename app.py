from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Haha!'

if __name__ == '__main__':
    # Flask auf allen Schnittstellen lauschen lassen und Port 8080 verwenden
    app.run(host='0.0.0.0', port=8080)

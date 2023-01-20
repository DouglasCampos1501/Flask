from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Olá Mundo.. agora em Flask"

@app.route('/get_service', methods=['GET'])
def get_service():
    return "Isto é um GET"

@app.route('/post_service', methods=['POST'])
def post_service():
    return "Isto é um POST"

@app.route('/html')
def html():
    return "<html><body><h1>Olá mundo em FLASK agora com H1</h1<</body></html>"

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello" + name

app.run(debug=True)
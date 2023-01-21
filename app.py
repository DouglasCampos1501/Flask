from flask import Flask
from flask import request
from flask import Response


app = Flask(__name__)

@app.route('/')
def index():
    return "Olá Mundo.. agora em Flask"

@app.route('/get_service', methods=['GET'])
def get_service():
    return Response(response = "Isto é um GET",
        status = 200, mimtype="application/html")

@app.route('/post_service', methods=['POST'])
def post_service():
    return "Isto é um POST"

@app.route('/html')
def html():
    return "<html><body><h1>Olá mundo em FLASK agora com H1</h1<</body></html>"

#@app.route('/hello/<name>')
@app.route('/hello/<string:name>')
def hello_name(name):
    return "Hello " + name

@app.route('/soma/<int:num>')
def soma(num):
    return "Seu número mais 1 é " + str(num+1)

@app.route('/hello/<string:name>/lastname/<sobrenome>')
def hello_name_sobrenome(name,sobrenome):
    return "hello " +name + " " + sobrenome

@app.route('/soma/<int:num1>/<int:num2>')
def soma1(num1,num2):
    return "somou:" + str(num1+num2)
app.run(debug=True)

@app.route('/subtract')
def subtrair():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return str(num1 - num2) 

app.run(debug=True)
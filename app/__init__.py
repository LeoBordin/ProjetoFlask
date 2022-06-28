from flask import Flask, render_template
app = Flask(__name__) #instanciando classe Flask

#Endereço do site
@app.route('/') #Rota principal
@app.route('/index') #Rota alternativa
def index():
    #return "Hello World"
    nome = "Leo B" #Variavel
    dados = {"profissao": "SRE", "cidade" : "Santa Rosa" } #Variavel Lista
    return render_template('index.html',nome=nome, dados=dados)

from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Parte de la pagina Web -------
app = Flask(__name__)

'''
@app.route('/')
def principal():
    return "bkslndkjas "

@app.route('/Preguntas')
def preguntas():
    return "Esta es la pagina de consulta y preguntas"
'''

@app.route('/')
def principal():
    return render_template('b-index.html')

@app.route('/preg')
def preguntas(): # ES POSIBLE QUE USEMOS BASE DE DATOS SQL
    ques = ("Donde esta cafeteria","Donde esta mi profe","Que hago")
    return render_template('c-index.html', ques=ques)

@app.route('/boti')
def bott():
    return render_template('d-index.html')

if __name__ == '__main__':
    app.run(debug=True)


# Parte del bot -----------------------


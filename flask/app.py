import os
from flask import Flask, render_template

app = Flask(__name__)

# definindo a variavel de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# configurando o modo de depuracao com base..
app.debug = os.environ.get('FLASK_DEBUG') == 'True'


@app.route('/')
def ola():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
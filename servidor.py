from flask import Flask, jsonify
from viernes_3 import administrador
app = Flask('inicio')

@app.route('/usuario')
def usuario():
    admin = administrador()
    data = admin.mostrar()
    resp = jsonify(data)
    print(data)
    return resp

app.run()

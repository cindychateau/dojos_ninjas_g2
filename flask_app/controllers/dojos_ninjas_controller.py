from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    todos_dojos = Dojo.get_all()
    return render_template('index.html', todos_dojos=todos_dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #request.form = {name: "Colombia"}
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/new/ninja')
def new_ninja():
    todos_dojos = Dojo.get_all()
    return render_template('new.html', todos_dojos=todos_dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    #request.form = {Diccionario con todos los campos del formulario}
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>') #/dojo/1
def show_dojo(id): #id = 1
    data = {"id": id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('dojo.html', dojo=dojo)

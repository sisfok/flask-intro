from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class MyForm(FlaskForm):
    content = StringField('content', validators=[DataRequired()])

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r> ' % self.id

@app.route('/', methods=['GET'])
def index():
    tasks = Todo.query.order_by(Todo.data_created).all()
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['GET','POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error when add data'

        return redirect('/')
    return render_template('add.html', form=form)

@app.route('/show/<int:id>')
def show(id):
    task_to_show = Todo.query.get_or_404(id)
    return render_template('show.html', task = task_to_show)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    form = MyForm(obj=task)
    
    if request.method == 'POST' and form.validate_on_submit():
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error when add data'
    else:
        return render_template('update.html', task=task, form=form)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error when delete data'

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('192.168.0.103', 27017, username='nik', password='password')
db = client.flask_db
todos = db.todos

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        content = request.form['content'] 
        degree = request.form['degree'] 
        
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, redirect, render_template, request, url_for
from pymongo import MongoClient
from bson.json_util import dumps
import hash

app = Flask(__name__)

client = MongoClient('192.168.0.103', 27017, username='nik', password='password')
db = client.flask_db
login_info = db.login_info

@app.route('/')
def index():
    
    creds = login_info.find_one({'email': 'test@test.com'})
    print(creds['email'])
    print(login_info.find_one({'email': 'test@test.com'})['passwd_hash'])
    
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        passwd_hash = hash.hash_creds(email, password)
        if passwd_hash == login_info.find_one({'email': email})['passwd_hash']:
            return "success"
        else:
            return "nope!"
    return render_template('index.html')
        
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_info.find_one({'email': email})['email']
            return "email already exists"
        except TypeError:
            passwd_hash = hash.hash_creds(email, password)
            login_info.insert_one({'email': email, 'passwd_hash': passwd_hash})
        
        return redirect(url_for('index'))
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
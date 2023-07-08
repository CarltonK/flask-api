from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message = 'Aloha')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'Hawks' and password == 'password':
            return render_template('login.html', message = username)
        else:
            error_message = 'Wrong password combination'
            return render_template('error.html', message = error_message)

@app.route('/structure', methods = ['GET'])
def work():
    return render_template('structure.html')

if __name__ == '__main__':
    app.run(debug = True)
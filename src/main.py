# An intentionally vulnerable Python program
import logging
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pwd = request.form.get('pwd')
    if doLogin(user, pwd):
        logging.info('%s logged in successfully with password: %s' % (user, pwd))
        return render_template('index.html', user)
    else:
        logging.info('%s failed to log in with password: %s' % (user, pwd))
        return 'Failed to log in'

# An intentionally vulnerable Python program.
#
# Let's try and game the system.

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
        logging.warn('%s failed to log in' % (user,))
        return 'Failed to log in'

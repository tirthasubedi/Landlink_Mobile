from flask import Flask, request, render_template
app = Flask(__name__)

from sampleQuestion import *
from about import *
from index import *
from forgotPassword import *
from confirmedSent import *
from createAccount import *
from accountCreated import *

if __name__ == '__main__':
    app.secret_key="Secret key"
    app.run(debug = True)

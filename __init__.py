from flask import Flask, render_template
app = Flask(__name__)

from sampleQuestion import *
from about import *
from index import *


if __name__ == '__main__':
    app.secret_key="Secret key"
    app.run(debug = True)

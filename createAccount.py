from app import *

@app.route('/createAccount')
def createAccount():
    return render_template("createAccount.html")

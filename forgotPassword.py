from app import *

@app.route('/forgotPassword')
def forgotPassword():
    return render_template("forgotPassword")

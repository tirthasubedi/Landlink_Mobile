from app import *

@app.route('/confirmedSent')
def about():
    return render_template("confirmedSent.html")
